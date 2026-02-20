# Drought EAP for southern Madagascar: Hazard and Vulnerability analysis


:::{topic} Context
For the Drought Early Action Protocol (EAP) by the Malagasy Red Cross (CRM), we developed a hazard and vulnerability analysis. The result ware reproducible maps showing a composite drought vulnerability combining hazard recurrence (rainfall deficits) and documented humanitarian impacts (IPC phase 3 or above). The two indicators are combined and classified into three levels of drought vulnerability (High/Medium/Low).

__Geographic focus:__ Androy, Anosy, Atsimo-Andrefana

:::

:::{card}
__QGIS Project__
^^^
The QGIS project and the datasets used in this project can be found here: 
__TBA__ [MDG_DROUGHT_EAP.qgz]

Note: Copyrighted datasets (CHIRPS and IPC) must be downloaded from the respective publishers or Google Earth Engine. 

:::


## Part 1: Historical rainfall deficit recurrence map (CHIRPS-based, 2000–2024) aggregated at district level
 

__Objective:__

Show spatial recurrence of significant rainfall deficits in southern Madagascar over a long reference period (ideally 2000–2024).
Suggested approach (open to your advice):

- Use CHIRPS monthly or seasonal data.
- Calculate anomalies relative to long-term averages.
- Define a threshold for severe deficit (e.g. ≤ -30% or ≤ -40%).
- Count frequency of deficit events over the reference period.
- Aggregate at district level (ADM2).

__Output:__

- District-level choropleth (High / Medium / Low recurrence).
- Clear, simple methodological note explaining threshold and aggregation.


__Questions:__

- CHIRPS monthly or seasonal data: How to define seasons? -> look at rain seasons in mdg or simply DJF, MAM
- Should I explain my choice for `Daily_RNL` instead of `Daily_SAT`?
- Is the question: *How widespread are rainfall deficits in the districts?* OR *How widespread are rainfall deficits where livelihoods depend on rainfall?*


### Workflow: Mapping hazard recurrence

1. Use GEE to aggregate the daily CHIRPS v3 to monthly totals for the time period 2000 to 2024.
2. Calculate the monthly climatology (mean per month across all years).
3. Compute the percentage anomaly per month  %anom=100×(P−Pˉm​)/Pˉm​ (per cell)
4. Flag severe deficit months (e.g. <= -30%)
6. Count how often each district is in deficit (frequency or count) = recurrence value
7. Aggregate to admin level:
    - __Options:__
        - A: Mean pixel recurrence (can also be normalised by dividing with the total number of months -> %)
        - B: Percent of area affected (need to define a threshhold of recurring deficit months, e.g., more than 30 deficit month in time period)
            - "65% of district had more than 30 deficit months".

- Monthly rainfall totals were derived from CHIRP v3 daily data hosted on Google Earth Engine. Monthly anomalies were calculated relative to the 2000–2024 climatological mean for each calendar month. Rainfall deficit events were defined as months with precipitation ≤30% (moderate) or ≤40% (severe) below the long-term mean. The frequency of deficit events was aggregated at district (ADM2) level to characterize historical recurrence.

- Rainfall deficit recurrence was defined as the number of months between 2000 and 2024 in which monthly rainfall fell below the deficit threshold. Recurrence was first calculated at the pixel level and then spatially averaged within administrative districts to characterize the typical frequency of deficit conditions across each district.

:::{card}
__Calculated indicators__
^^^
| Level | Variable           | Interpretation                         |
| ----- | ------------------ | -------------------------------------- |
| Pixel | (D_t(x))           | Deficit this month? (0/1)              |
| Pixel | (R(x))             | # of deficit months at that location   |
| ADM2  | mean (R(x))        | Typical deficit recurrence in district |
| ADM2  | % area ≥ threshold | Spatial extent of recurrent deficits   |
:::


> We have calculated two indicators:  
> 1. Mean recurrence per adm2  
> 2. Percentage of area above threshold  
> Now we need to select the thresholds for both indicators:

8. Select thresholds for the choropleth map:
  

::::{grid} 
:::{grid-item-card} 
__Mean Recurrence per adm2:__
^^^
- quantiles: 3 classes (high/medium/low)
- absolute thresholds: 
  - Low: < 10% of months in deficit
  - Medium: 10-20% of months in deficit
  - High: > 20% of months in deficit
  - standard deviation?
:::

:::{grid-item-card}
__Percentage of area above threshold:__
^^^
- `% area with recurrence ≥ K months`
  - __define K__
  - define classes for percentages:
    - ___Data-distribution:__
      - tertiles
    - __Absolute exposure:__
      - e.g., less than 10 % -> localised/patchy
      - 10-30% -> substantial exposure
      - more than 30% -> widespread exposure
    - __sensitivity-informed__
      - examine how % area affected behaves for different thresholds 
:::
::::


__Output:__

- a district layer with fields:
    - `def_count`: number of deficit months, 2000-2024
    - `def_freq`: def count / number of months
    - maybe: counts by season (DJF, MAM, etc.)

:::{dropdown} GEE Script
```javascript
/**** CHIRPS v3 DAILY_RNL -> MONTHLY -> DEFICIT RECURRENCE (2000–2024)
 *
 * Dataset: UCSB-CHC/CHIRPS/V3/DAILY_RNL
 *
 * Outputs (3–4 tasks total):
 *  1) Madagascar ADM2 boundaries (GAUL level2) as SHP
 *  2) ADM2 indicators as CSV:
 *     - Mean recurrence count + % of months (for -30% and -40%)
 *     - % area “frequently affected” (recurrence >= K) for -30% and -40%
 *  3) Raster export A (UInt16): recurrence counts (rec30_count, rec40_count)
 *  4) Raster export B (Float32): recurrence frequency + percent (rec30_freq, rec40_freq, rec30_pct, rec40_pct)
 *
 * NOTE:
 * - Raster exports use a Madagascar bounding box region to avoid 10MB payload errors
 *   from complex dissolved polygon geometries. Clip precisely to coastline/districts in QGIS if needed.
 ****/


/**** SETTINGS ****/
var CHIRPS_DAILY_ID = 'UCSB-CHC/CHIRPS/V3/DAILY_RNL';

var startDate = ee.Date('2000-01-01');
var endDate   = ee.Date('2024-12-31'); // inclusive intent; handled via end-exclusive filter

// Deficit thresholds as ratios (stable)
// ratio <= 0.7  <=> anomaly <= -30%
// ratio <= 0.6  <=> anomaly <= -40%
var thr30 = 0.7;
var thr40 = 0.6;

// Avoid dividing by tiny baselines (mm/month)
var baselineMinMM = 5;

// Frequent-deficit cutoffs (months over full period; T should be 300)
var K30 = 30;  // ~10% of months
var K40 = 15;  // ~5% of months

// Admin boundaries (ADM2)
var ADM2 = ee.FeatureCollection('FAO/GAUL/2015/level2');

// Approx CHIRPS native resolution ~0.05° (~5–6 km)
var scaleMeters = 5500;

// Madagascar export region (bounding box; export-safe payload)
// lon_min, lat_min, lon_max, lat_max
var mdgRegion = ee.Geometry.Rectangle([43.2, -26.0, 50.6, -11.9], null, false);


/**** MADAGASCAR ADM2 ****/
var mdgAdm2 = ADM2.filter(ee.Filter.eq('ADM0_NAME', 'Madagascar'));

Map.setCenter(46.9, -19.0, 6);
Map.addLayer(
  mdgAdm2.style({color: 'FFFFFF', fillColor: '00000000', width: 1}),
  {},
  'MDG ADM2 (outline)',
  false
);


/**** EXPORT ADM2 BOUNDARIES (SHP) ****/
// (GEE does not export GeoPackage directly; convert SHP->GPKG in QGIS or ogr2ogr)
Export.table.toDrive({
  collection: mdgAdm2.select(['ADM0_NAME','ADM1_NAME','ADM2_NAME','ADM2_CODE']),
  description: 'MDG_ADM2_GAUL2015_level2',
  fileFormat: 'SHP'
});


/**** LOAD DAILY CHIRPS v3 RNL (clip to bbox region) ****/
var daily = ee.ImageCollection(CHIRPS_DAILY_ID)
  .filterDate(startDate, endDate.advance(1, 'day')) // end-exclusive
  .select(['precipitation'])
  .map(function(img){ return img.clip(mdgRegion); });

print('Daily collection:', CHIRPS_DAILY_ID);
print('Daily count:', daily.size());


/**** BUILD MONTHLY TOTALS FROM DAILY ****/
function monthlySumsFromDaily(ic, start, end) {
  var startY = ee.Number(start.get('year'));
  var endY   = ee.Number(end.get('year'));

  var years  = ee.List.sequence(startY, endY);
  var months = ee.List.sequence(1, 12);

  var startMs = start.millis();
  var endMs   = end.millis();

  var monthlyList = years.map(function(y){
    y = ee.Number(y);
    return months.map(function(m){
      m = ee.Number(m);
      var monthStart = ee.Date.fromYMD(y, m, 1);
      var monthEnd   = monthStart.advance(1, 'month');

      // Compare millis (ee.Date has no .gte/.lte)
      var ms = monthStart.millis();
      var inRange = ms.gte(startMs).and(ms.lte(endMs));

      return ee.Image(ee.Algorithms.If(
        inRange,
        ic.filterDate(monthStart, monthEnd).sum()
          .rename('precip')
          .set({
            'year': y,
            'month': m,
            'system:time_start': monthStart.millis()
          }),
        null
      ));
    });
  }).flatten();

  return ee.ImageCollection.fromImages(monthlyList)
    .filter(ee.Filter.notNull(['system:time_start']));
}

var monthly = monthlySumsFromDaily(daily, startDate, endDate);
var T = ee.Number(monthly.size());
print('Monthly images (T):', T); // should be 300 for 2000–2024


/**** MONTH-OF-YEAR CLIMATOLOGY (PIXEL-WISE) ****/
var climatologyByMonth = ee.ImageCollection(
  ee.List.sequence(1, 12).map(function(m){
    m = ee.Number(m);
    return monthly
      .filter(ee.Filter.eq('month', m))
      .mean()
      .rename('clim')
      .set({'month': m});
  })
);

// Add ratio + anomaly bands to each monthly image
function addAnomalies(img) {
  var m = ee.Number(img.get('month'));
  var clim = ee.Image(climatologyByMonth.filter(ee.Filter.eq('month', m)).first());

  // mask where climatology too small
  var valid = clim.gte(baselineMinMM);

  var P = img.select('precip').updateMask(valid);
  var C = clim.updateMask(valid);

  var ratio = P.divide(C).rename('ratio');
  var anomPct = P.subtract(C).divide(C).multiply(100).rename('anomPct');

  return img.addBands([ratio, anomPct]).updateMask(valid);
}

var monthlyWithAnoms = monthly.map(addAnomalies);


/**** DEFICIT FLAGS (0/1) PER MONTH ****/
function addDeficitFlags(img) {
  var ratio = img.select('ratio');

  var def30 = ratio.lte(thr30).unmask(0).toUint8().rename('def30');
  var def40 = ratio.lte(thr40).unmask(0).toUint8().rename('def40');

  return img.addBands([def30, def40]);
}

var flagged = monthlyWithAnoms.map(addDeficitFlags);


/**** RECURRENCE COUNTS PER PIXEL (SUM OVER MONTHS) ****/
var rec30 = flagged.select('def30').sum().rename('rec30').clip(mdgRegion);
var rec40 = flagged.select('def40').sum().rename('rec40').clip(mdgRegion);

// Optional map previews
Map.addLayer(rec30, {min: 0, max: 80}, 'Recurrence count (<= -30%)', false);
Map.addLayer(rec40, {min: 0, max: 40}, 'Recurrence count (<= -40%)', false);


/**** RASTER DERIVATIVES (COUNTS + FREQ + PCT) ****/
var t = ee.Number(T);

// Counts rasters (UInt16)
var rec30_count = rec30.rename('rec30_count').toUint16();
var rec40_count = rec40.rename('rec40_count').toUint16();

// Frequency rasters (Float32)
var rec30_freq = rec30.divide(t).rename('rec30_freq'); // 0..1
var rec40_freq = rec40.divide(t).rename('rec40_freq'); // 0..1

// Percent rasters (Float32)
var rec30_pct = rec30_freq.multiply(100).rename('rec30_pct'); // 0..100
var rec40_pct = rec40_freq.multiply(100).rename('rec40_pct'); // 0..100


/**** ADM2 AGGREGATION: MEAN RECURRENCE + AREA SHARE ****/
var pixelArea = ee.Image.pixelArea();

// “Frequently affected” masks based on pixel recurrence
var freq30 = rec30.gte(K30);
var freq40 = rec40.gte(K40);

// Area images (m²)
var totalAreaImg  = pixelArea.rename('area_total_m2');
var areaFreq30Img = pixelArea.updateMask(freq30).rename('area_freq30_m2');
var areaFreq40Img = pixelArea.updateMask(freq40).rename('area_freq40_m2');

// Mean recurrence reducers (per ADM2)
var recStack = rec30.addBands(rec40);

var recMeans = recStack.reduceRegions({
  collection: mdgAdm2,
  reducer: ee.Reducer.mean(),
  scale: scaleMeters
});

// Area sums (per ADM2)
var areaSums = totalAreaImg.addBands(areaFreq30Img).addBands(areaFreq40Img)
  .reduceRegions({
    collection: mdgAdm2,
    reducer: ee.Reducer.sum(),
    scale: scaleMeters
  });

// Join mean+area tables by ADM2_CODE
var joinKey = 'ADM2_CODE';
var joined = ee.Join.inner().apply({
  primary: recMeans,
  secondary: areaSums,
  condition: ee.Filter.equals({ leftField: joinKey, rightField: joinKey })
});

// Build final output FeatureCollection
var results = ee.FeatureCollection(joined.map(function(f){
  f = ee.Feature(f);
  var left  = ee.Feature(f.get('primary'));
  var right = ee.Feature(f.get('secondary'));

  var rec30_mean = ee.Number(left.get('rec30'));
  var rec40_mean = ee.Number(left.get('rec40'));

  var rec30_mean_pct = rec30_mean.divide(t).multiply(100);
  var rec40_mean_pct = rec40_mean.divide(t).multiply(100);

  var areaTotal  = ee.Number(right.get('area_total_m2'));
  var areaFreq30 = ee.Number(right.get('area_freq30_m2'));
  var areaFreq40 = ee.Number(right.get('area_freq40_m2'));

  var areaFreq30_pct = areaFreq30.divide(areaTotal).multiply(100);
  var areaFreq40_pct = areaFreq40.divide(areaTotal).multiply(100);

  return left.set({
    'source_daily_id': CHIRPS_DAILY_ID,
    'start': startDate.format('YYYY-MM-dd'),
    'end': endDate.format('YYYY-MM-dd'),
    'T_months': t,

    'baselineMinMM': baselineMinMM,
    'thr30_ratio': thr30,
    'thr40_ratio': thr40,
    'K30_months': K30,
    'K40_months': K40,

    'rec30_mean_count': rec30_mean,
    'rec30_mean_pct': rec30_mean_pct,

    'rec40_mean_count': rec40_mean,
    'rec40_mean_pct': rec40_mean_pct,

    'area_freq30_pct': areaFreq30_pct,
    'area_freq40_pct': areaFreq40_pct,

    'area_total_m2': areaTotal
  });
}));

print('ADM2 results sample:', results.limit(5));


/**** EXPORT RESULTS TABLE (CSV) ****/
Export.table.toDrive({
  collection: results.select([
    'ADM0_NAME','ADM1_NAME','ADM2_NAME','ADM2_CODE',
    'source_daily_id','start','end','T_months',
    'baselineMinMM','thr30_ratio','thr40_ratio','K30_months','K40_months',
    'rec30_mean_count','rec30_mean_pct',
    'rec40_mean_count','rec40_mean_pct',
    'area_freq30_pct','area_freq40_pct',
    'area_total_m2'
  ]),
  description: 'MDG_ADM2_CHIRPSv3_RNL_deficit_recurrence_2000_2024',
  fileFormat: 'CSV'
});


/**** EXPORT RASTERS (OPTION 1: SPLIT BY DATA TYPE) ****/

// A) Counts (UInt16) — 2 bands
var recCounts = rec30_count.addBands(rec40_count).clip(mdgRegion);

Export.image.toDrive({
  image: recCounts,
  description: 'MDG_CHIRPSv3_RNL_recurrence_counts_2000_2024_bbox',
  region: mdgRegion,
  scale: scaleMeters,
  crs: 'EPSG:4326',
  maxPixels: 1e13
});

// B) Frequency + percent (Float32) — 4 bands
var recFreqPct = rec30_freq.addBands(rec40_freq)
  .addBands(rec30_pct).addBands(rec40_pct)
  .toFloat()
  .clip(mdgRegion);

Export.image.toDrive({
  image: recFreqPct,
  description: 'MDG_CHIRPSv3_RNL_recurrence_freqpct_2000_2024_bbox',
  region: mdgRegion,
  scale: scaleMeters,
  crs: 'EPSG:4326',
  maxPixels: 1e13
});
```
:::


## Part 2: A recurrent IPC Phase 3+ exposure layer (if feasible)


__Objective:__ Complement meteorological layer with documented humanitarian impact evidence.

__Possible options:__
1. Overlay IPC Phase 3+ outcomes (where data available)
2. Estimate recurrence of IPC 3+ at district level across recent years.
3. If full GIS integration is complex, even a spatial proxy based on documented IPC rounds would already be extremely helpful.


__Questions:__

- What is the temporal range for recurrence at district level? IPC reports are published every few months iirc and I calculate the CHIRPS recurrence on a monthly basis. 
- how should I aggregate the IPC phases at district level if the IPC phases are not tied to admin boundaries. Area share also does not make sense because it does not show where people live. 
- To get the time resolution, I could aggregate the CHIRPS using % of months in deficit?
- ML1 oder ML2? 
- In FEWSNET or via the WorldBank

__Step 1: Downloading IPC data:__



