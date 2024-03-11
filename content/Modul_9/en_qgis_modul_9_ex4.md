# Task 4: Something something capacity?

## STEP 1: Data Preparation

1. download population density layer here: https://hub.worldpop.org/geodata/summary?id=49708  and open in QGIS.

The units are the number of people per pixel. Country totals have been adjusted to match the corresponding official United Nations population estimates produced by the Population Division of the  Economic and Social Affairs Department of the United Nations Secretariat (2019 Revision of World Population Prospects). "NoData" values represent areas that have been mapped unpopulated. This was done based on building footprints from the Digitize Africa project by Ecopia.AI and Maxar Technologies (2020).


2. Create a vector grid

-  make sure to change the coordinate system so that you can enter the data in meters instead of degrees  
        https://mangomap.com/robertyoung/maps/69585/what-utm-zone-am-i-in-# here you are able to calculate the specific UTM zone
        https://projectionwizard.org/ if you zoom into the respective region you will get the appropriate projection

-  Create a vector grid with 1000m resolution by using the tool create grid

         Grid type: rectangle (Polygon)
         Gird extent - calculate from layer - ....
         Horizontal spacing: 1000m
         Vertical spacing: 1000m
         Run


3. Join the grid and the population layer by using the tool zonal statistics

    Input layer: Grid Networkanalysis - Hospital Accessibility, Rwanda.zip
    Raster layer: Population layer
    statistics to calculate: sum


4. Cut the Grid along the border of Rwanda by using the tool select by location to make sure that we just work with the objects with the country border. Administrative boundaries can be downloaded here: https://www.naturalearthdata.com/

    extract features from: zonal statistic layer (Grid)
    where the features: intersect
    by comparing to the features from: Rwanda border layer

ADDIT: In addition it makes sense to have a look on the a basemap like OSM to check if there are any big water surfaces etc. Herefore you can also use the tool QuickOSM and use the name of the water body. If so, you should cut them out, as water areas are uninhabited (population layer). Use the tool select by location.


4. Creation of hospital layer by using the the tool QuickOSM

    key = amenity … value = hospital … in … Rwanda → Result: point-, line- & polygonlayer

    using the tool „select by location“ we can check if there are objects from the polygon or line layer that are not included in the point layer

    if so; we need to convert them into points

    by using the tool centroids, which creates a new point layer with the points representing the centers of the geometries of the input layer

    by using the tool „merge vector layers“ we merge the first point layer and the new point layer


## STEP 2: Isochrone generation

by using the tool ORS tools we calculate the isochrones for the hospitals

        click on Isochrones on layer

        provider = openrouteservice

        travel mode = driving car

        input layer = schools

        dimension= time

        comma – separated ranges (min) = 10, 30, 60



## STEP 3: Merge Population and Isochrones

    Since we want to show how many cells are inside which isochrones, we need to split the isochrones layer
    Join the Grid with the isochrones by using the tool join by location (summary). Repeat the process with the second isochrones and the joined layer instead of the first Grid.
        Join to features in: Grid
        where the features: intersect
        By comparing to: Isochrones_10min

ADDIT: Remember to rename the layers to keep the overview. The attribute tables should also be clear. Delete irrelevant columns and rename columns if necessary.


## STEP 4: Calculate available hospitals in 60 Min.

Open the attribute table of the final and use the field calculator.

    select: create new field
    select: integer
    name it: hospital_capacity
    enter: "population"/"hospitals"



## Step 5 Analysis of potential patient volume (lower level)

1: Create a new ID for the hospitals

    Add a field to contain the feature id, say "FID", of type Whole number (integer).
    Open Layer Properties (right-click on the layer and choose Properties... or double-click the layer), click on the Attributes Form tab, then under General uncheck Editable and under Defaults in the field Default value type:  maximum("FID") + 1
2: Export the final grid as Excel File

Export the layer final grid as MS Office Open XMP Spreadsheet [XLSX)

3: Open file and insert pivot table

    Drag the hospital IDs into the row field and the capacity into the data field.
    Save the pivot table as a new file.

4: Join

    Open the Excel file in your QGIS project
    Click on your hospital layer → properties → Joins →
    Join Layer: Excel File
    Join Field: Hospital ID
    Target Field: Hospital ID
