# QGIS common errors and issues

Here we are collecting common QGIS errors and issues as general QGIS training support.

## Common QGIS errors

(Note: Alphabetisch sortieren?)

- Different QGIS Versions
  - Main items

(Welche Beispiele dazu? Unterschiedliche Displays, etc.) 

- A layer is not displayed in QGIS. 

  - Solution: 
  Right click on the corresponding layer and activate the *Zoom to layer* function in the pop-up window. 

```{figure} /fig/en_layer_display.png
---
width: 75%
name: en_layer_display
---
Screenshot of Zoom to Layer function
```
- A layer window has disappeared in QGIS.

  - Solution:

 Open in the main tab *View*, in the pop-up window select *Panels* and in the sub-window activate *Browser*.   

```{figure} /fig/en_closed_layer_view.png
---
width: 75%
name: en_closed_layer_view
---
Screenshot of Closed Layer View
```

- Layers that should actually be in the same position are not on top of each other.

  - Solution:

These sort of problems are usually due to a) mismatching KBS in layers and project, or b) an incorrect reprojection. 

 a) First check the layer properties (right-click on the corresponding layer, select in the pop-up window *Properties*, in the next pop-up-window select *Information* and check which projection is defined there under the entry *Coordinate Reference System (CRS)* and additionally in the status bar at the bottom right which project KBS/CRS is set there. Then correct any discrepancies by reprojecting the layers or changing the setting of the KBS/CRS project. 

b) When reprojecting, follow exactly the procedure described in the Wiki under Projections (ergänzen). Errors often occur if KBS is set and no reprojection tool is used. If you suspect that your reprojection has gone wrong, delete all affected layers from GIS, reload the data and then reproject. 


```{figure} /fig/en_CRS_projection_check.png
---
width: 75%
name: en_CRS_projection_check.png
---
Screenshot of RS Projection Check
```


- Missing Processing Tools in the Panels Tool and incomplete Vector Tab.

  - Solution:
  
  It may happen that the *Processing Tools Tab* is missing and also that the *Vector Tab Display* is incomplete. Then you may activate them by going to *Plugins* and *Manage and install Plugins* and selecting *All* and rehooking the Processing function in the corresponding list.
  
```{figure} /fig/en_missing_processing_tools.png
---
width: 75%
name: en_missing_processing_tools.png
---
Screenshot of Missing Processing Tools
```
 
- Missing Toolbox.
  - Solution:

 It may happen that the *Toolbox* (small gear wheel) is missing. To reactivate it, just click on the *View Tab*, select in the pop-up window *Panels* and in the following pop-up window set a hook for the *Processing Toolbox*.  

```{figure} /fig/en_missing_toolbox.png
---
width: 75%
name: en_missing_toolbox.png
---
Screenshot of Missing Toolbox
```


--------------------------------------------
  
 ## Common questions and issues
  - (Note: weiteren Content übertragen)

  

## QGIS training support

(Nach Kapiteln sortieren?)

### (Modul 1 - Introducing QGIS)
#### (Understanding the Interface Exercise:)

### Modul 2 - Working with Geodata
#### Geodata Concept Exercise: 
#### Basic Geodata processing Exercise:
#### Data resources Exercise:
#### The World Exercise:

### Modul 3 - Basic GIS operations
#### Digitization Exercise 1:
#### Digitization Exercise 2:
#### Geodata Classification Exercise: 
#### Geodata Selection and Queries Exercise: 
#### Nigeria Floods Exercise:

- Sometimes the reference is not really clear in the exercise text: goes it to the attribute table of the layer or to the PDF table concerning the areas affected by the flood.

- After each important exercise step a visualization of the result may be helpful, f. ex. for visualizing the mentioned point layer. 

### Modul 4 - Representation
#### Visualization Exercise:
#### (Ghana) Map making Exercise:  

- The North arrow ist not syncing with the corresponding map.

There are two places where you have to define with which map the N arrow should rotate with.

First it is in the *Layout Tab* for the image under *General Settings*, make sure that the reference map has the right map selected. Then go to *Properties*, expand *Image Rotation*, select the *Sync with map option* and define here which map it should be.

  - (image ergänzen)

### Modul 5 - Intermediate GIS operation
#### Healthsite distribution in Saint Louis region Exercise:
#### Calculate vulnerability index Exercise:
#### Disaster effects in different regions of Senegal Exercise:
#### Calculate vulnerability index Exercise:
#### Risk assessment -  Calculate vulnerability index Exercise: 
#### Risk assessment - Risk calculation Exercise:
#### Trigger & Intervention Map for Forecast-based-Action Exercise:

- I could make sense to place the reference to the coding a little bit earlier in the text to avoid that it is not overlooked or "forgotten" during the exercise.
- There are two variants of *Join attributes by location* in the toolbox, so may help to enter a note here. 
- When converting tables to csv, it could make sense to add a note in the text whether you are converting for Mac or Win computers and that from a multi-page Excel only the first page will be read out. 

----------------------------------------------

To add?

- Invalid Geometry

If the error message *Invalid Geometries* appears, it may be that vector files have "slipped" during the processing or downloading process (e.g. the lines of polygons no longer fit together exactly). These errors in the geometries can be corrected by selecting *Fix Geometries* in the Processing Toolbox.


- Issues with Georeferencing


### Modul 6 - Data analysis with QGIS - Exercise:
### (Modul 9 - Network Analysis in QGIS)