# Spatial Geodataprocessing
**Competences:**

## Clip



* Clip, Buffer, Dissolve
* Spatial joins
* Clip by extent & mask

## Clip vector by extent

This operation clips any vector file to a given extent. This clip extent will be defined by a bounding box that should be used for the vector output file. It also has to be defined in the target CRS coordinates. There are different methods to define the bounding box of which the following is the most prominent:
* Calculate from a layer: this uses the extent of a layer loaded into the current project

# DROPDOWN HERE OR TABS
Other option are:
* Calculate from layout map: uses the extent of a layout map item in the active project
* Calculate from bookmark: uses the extent of a saved bookmark
* Use map canvas extent
* Draw on canvas: click and drag a rectangle delimiting the area to take into account
* Enter the coordinates as xmin, xmax, ymin, ymax

## Clip vector by mask layer

This operation uses a mask polygon layer to clip any vector layer.

# AUCH FÜR RASTER DATEN??