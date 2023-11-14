# Geoprocessing
## Subsection to be created:
* Clip
* Buffer
* Dissolve
* ....

## Buffer
- Calculate a ![](/fig/mAlgorithmBuffer.png) `buffer` with a defined distance
- Dissolve: if 2 or more buffer areas overlap, they can be combined.

```{Attention}
The unit of distance depends on the projection of the layer. For buffering you usually need a __metric coordinate system__ such as UTM (Universal Transverse Mercator).
```

:::{dropdown} Example: Which regions fall within a 100-kilometer radius of major cities?
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_buffer_wiki.mp4"></video>
:::

```{Hint}
If you're dealing with really large "megabuffers" or if you can only choose buffer distances in degrees instead of meters, it might mean there's __no metric coordinate system__, or it was __incorrectly reprojected__. The unit of the buffer __depends__ on the __coordinate reference systems of the layer__.
```

## Clip
- With the ![](/fig/mAlgorithmClip.png) `Clip` tool you can extract and retain the spatial extent of one vector layer based on the boundaries of another layer. 
- `Input Layer`: refers to the specific __layer to be clipped__, for instance, a road network.
- `Overlay Layer`: e.g. a polygon layer of the region (e.g. borders of Heidelberg)

:::{dropdown} Example: Extract the rail network of Germany
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_clip_wiki.mp4"></video>
:::

## Dissolve
- The ![](/fig/mAlgorithmDissolve.png) `dissolve` tool aggregates geometries with the same attribute values
- When 2 or more buffer areas overlap, they can be combined using dissolve

:::{dropdown} Example: Extract the rail network of Germany
:open:
<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/en_qgis_dissolve_wiki.mp4"></video>
:::

```{Attention}
In QGIS, only the attributes selected for the dissolve operation will receive the accurate attribute, while the remaining attributes remain unaggregated; hence, in this example, the name is not accurately represented (e.g. the name for Western Europe might be mistakenly assigned as "Netherlands").
```
