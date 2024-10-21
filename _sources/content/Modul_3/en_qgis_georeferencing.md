# Georeferencing 

Georeferencing in QGIS is the process of aligning a raster image, such as a scanned map or aerial photograph, to a 
known coordinate system so that it can be used in spatial analysis. This involves assigning real-world coordinates to 
the image by identifying control points on the raster that correspond to known locations on the earth, often using 
existing vector layers or coordinate grids as a reference.

In many cases, governmental institutions publish maps only as PDFs, without public access to the underlying data. In 
these cases, knowing how to correctly georeference a map allows you to access and use the information in your GIS 
analyses. In the case below, the soil degradation map of Somalia is only available in a pdf report. In order to use the 
information in a GIS analysis, we can use the georeferencer to assign geographic coordinates to the pixels of the 
image. After georeferencing the image, the result is a raster file (`.tiff`). This dataset can be vectorized 
(converted into vector data) or joined with other raster data, to gain additional information.

Georeferencing is the process of giving each pixel on a map geographic coordinates. This is done by selecting points on 
a map, and assigning them a geographic coordinate, either by enter the coordinates manually, or selecting the corresponding
point in the QGIS map canvas. These points serve as reference points for the georeferencing algorithm to add geographic 
coordinates to each pixel in the raster. 


```{figure} /fig/example_georefencing_hague.png
---
width: 750 px
name: example_georeferenced_map
---
A digitised old map of the Hague (Source: [Kokoalberti](https://kokoalberti.com/articles/georeferencing-and-digitizing-old-maps-with-gdal/))
```


<!--ADD: Pictures of maps available in pdf reports-->
## Georeferencing in QGIS

In QGIS, the Georeferencer tool is used for this process. Users manually place control points on the raster image and 
match them to corresponding locations in a reference dataset. The software then uses these points to transform the 
image, adjusting its scale, rotation, and position to accurately overlay it with other geospatial layers. Georeferenced 
images become valuable for digitizing features and conducting spatial analyses within a GIS.

There are several transformation algorithms available in QGIS to gereference a map. If the map is in the same CRS and only needs to be rotated, 
a __linear__ transformation is sufficient. However, if the image or map is in a different CRS or is visibly skewed, a __polynomial__ transformation 
is needed. The more complex the transformation algorithm is, the more Ground Control points you need. 


```{figure} /fig/en_georef_transformations.png
---
width: 600 px
name: 
---
Different transformation types: linear (left), polynomial 2nd degree (middle), polyonmial 3rd degree (right) (Source: [ESRI](https://pro.arcgis.com/en/pro-app/latest/help/data/imagery/overview-of-georeferencing.htm))
```

### Transformation types

:::::{dropdown} Transformation types (from the  [QGIS Documentation](https://docs.qgis.org/3.34/en/docs/user_manual/working_with_raster/georeferencer.html))
## Linear
The Linear algorithm is used to create a world file and is different from the other algorithms, as it does not actually 
transform the raster pixels. It allows positioning (translating) the image and uniform scaling, but no rotation or other 
transformations. It is the most suitable if your image is a good quality raster map, in a known CRS, but is just missing 
georeferencing information. At least 2 GCPs are needed.

## Polynomial 1
The Polynomial 1 algorithm allows a more general affine transformation, in particular also a uniform shear. Straight lines 
remain straight (i.e., collinear points stay collinear) and parallel lines remain parallel. This is particularly useful for 
georeferencing data cartograms, which may have been plotted (or data collected) with different ground pixel sizes in different 
directions. At least 3 GCP's are required.

## Polynomial 2-3
The Polynomial algorithms 2-3 use more general 2nd or 3rd degree polynomials instead of just affine transformation. This allows 
them to account for curvature or other systematic warping of the image, for instance photographed maps with curving edges. At 
least 6 (respectively 10) GCP's are required. Angles and local scale are not preserved or treated uniformly across the image. 
In particular, straight lines may become curved, and there may be significant distortion introduced at the edges or far from 
any GCPs arising from extrapolating the data-fitted polynomials too far.

## Helmert
The Helmert transformation also allows rotation. It is particularly useful if your raster is a good quality local map or 
orthorectified aerial image, but not aligned with the grid bearing in your CRS. At least 2 GCPs are needed.

## Projective
The Projective algorithm generalizes Polynomial 1 in a different way, allowing transformations representing a central 
projection between 2 non-parallel planes, the image and the map canvas. Straight lines stay straight, but parallelism 
is not preserved and scale across the image varies consistently with the change in perspective. This transformation 
type is most useful for georeferencing angled photographs (rather than flat scans) of good quality maps, or oblique 
aerial images. A minimum of 4 GCPs is required.

## Thin Plate Spline (TPS)
The Thin Plate Spline (TPS) algorithm “rubber sheets” the raster using multiple local polynomials to match the GCPs 
specified, with overall surface curvature minimized. Areas away from GCPs will be moved around in the output to 
accommodate the GCP matching, but will otherwise be minimally locally deformed.  TPS is most useful for georeferencing 
damaged, deformed, or otherwise slightly inaccurate maps, or poorly orthorectified aerials.  It is also useful for 
approximately georeferencing and implicitly reprojecting maps with unknown projection type or parameters, but where 
a regular grid or dense set of ad-hoc GCPs can be matched with a reference map layer. It technically requires a minimum 
of 10 GCPs, but usually more to be successful.

:::::

### How to Georeference in QGIS

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_3.36_georeferencing_howto.mp4"></video>

In order to georeference a PDF map, you need to follow the following steps:

1. The first step is to export the Map from the PDF as an image. For example, you can take a screenshot using the 
`Snipping Tool` on Windows, or by pressing <kbd>Shift</kbd> + <kbd>Command</kbd> + <kbd>4</kbd> on MacOS. Name and save 
the screenshot.
2. In your QGIS window, add a basemap using the [QuickMapServices Plugin](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_basemaps_wiki.html). 
Ideally, use a basemap where you can identify exact locations on both the basemap and the map you want to georeference.
3. Open the Georeferencer by navigating to the Top Bar > `Layer` > `Georeferencer` (see {numref}`open_georeferencer`)

```{figure} /fig/en_3.36_open_georefencer.png
---
name: open_georeferencer
width: 500 px
---
Opening the Georeferencer in QGIS 3.36
```

4. A new window will open. This is the __georeferencer__. To add an image to georeference, click on ![](/fig/3.36_add_raster_georef.png) `Open Raster`.
5. Select the image of the map you want to georeference. Click `Open`.
6. The image will appear in the middle of the georeferencer window. Click on ![](/fig/3.36_georef_transformation_settings.png) `Transformation settings...`.
7. A new window will open. Here you can set the transformation type and the target CRS. Below, you can set the name and save location of the file. Make sure that the `Load in project when done` is checked. 



::::{margin}

```{note}
In most cases, you can leave the transformation type on `linear`. Regional maps are usually in a conformal projection (i.e. the angles are preserved). Satellite imagery as well. If you realise that the angles are not true, or the map is deformed, you may need to choose `polynomial` as transformation type. 
```

::::

8. Click on `Ok`. 
9. Once you have set the transformation type, you can start adding Ground Control Points (GCP) by clicking on ![](/fig/3.36_georef_add_point.png) `Add Point`. Ground Control Points are points that you ascribe specific geographic coordinates. 
10. Click on a point on the map image. This will be the precise location that you can identify on both the basemap and the map you wish you georeference. 
11. Once you clicked on a position, a new window will appear. Here, you add the coordinates to the point you selected. There are two options to do this:  
    - Enter the coordinates manually. You will need to know the exact coordinate. Sometimes, you have a coordinate grid on maps where you can 
    - Select the points ![](/fig/en_3.36_georef_select_from_canvas.png). This mode will minimize the georeferencer and open the QGIS Map canvas. Zoom to the same location you selected on the non-georeferenced map and Click once.
    - Once the coordinates are entered, click `Ok`
12. The georeferencer window will open again. This time, below the map image, you can see a point in the table. These are the Ground Control Points. Continue adding more GCP. Spread them out over the entire map. Make sure that the `Mean error` in the bottom right corner of the georeferencer window is as low as possible (below 5 is ideal). 

```{figure} /fig/en_3.36_georef_dialogue_GCP.png
---
width: 700 px
name: georeferencer_dialogue
---
Georeferencer dialogue in QGIS 3.36
```

13. Once you have added enough points, click on ![](/fig/3.36_start_georef.png) `Start Georeferencing`. QGIS will use the Points you added to transform the image into a georeferenced image, where every pixel has GPS coordinates ascribed to it. 
14. You can close the georefencer window. Decide wether you want to save the GPC points in a file. If you are not sure if your georeferencing accuracy was precise enough, save the GPC points so you don't have to do all the work again. 
15. Congratulations, the georeferenced map will now appear as a raster layer in your QGIS-project


```{figure} /fig/en_3.36_finished_georef.png
---
width: 700 px
name: Som_georef_map
---
A georeferenced map of Somalia in the QGIS Map Canvas
```



<!--Choose an appropriate CRS-->

<!--What errors to avoid-->

<!--TIPS and TRICKS
Avoid QGIS Bug, Dock the georef window,...?-->