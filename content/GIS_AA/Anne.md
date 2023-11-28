# Drought Trigger Somaliland Somalia

The main parameters chosen for the trigger based on the historical impact assessment are the twelve month Standard Precipitation Index (SPI12) and the IPC acute food insecurity classification. The exact data used are the documented and forecasted SPI12 (source: ICPAC) and the forecasted IPC classification (8 month forecast, source: FEWSNET), that is used to calculate a population weighted index of food insecurity. The trigger thresholds for both components were optimised towards the most favourable proportion of hit rate and false alarm rate. The emerging thresholds were <-1 for the SPI12 and >=0,7 for the IPC based index. The triggering is done on district level and per district just one trigger initiation per year is possible.

# Trigger Statement

When ICPAC issues a SPI-12 forecast of less than -1 for a district AND the current FEWSNET food insecurity projection reaches at least 0.7 in its 
derived population weighted index in the same district, then we will act in this district. We expect the lead-time to be 90 days.


##  Trigger Input Data

For the trigger mechanism to work properly we currently use different datasets: data that we assume to be fixed in the near term, and variable data which describe the datasets that will be checked for triggering on a monthly base. 

## Fixed Data

By fixed data we mean datasets that are needed for the trigger to work, that will most probably not change in the near term. In the long term these datasets can be adapted easily.

| Dataset| Source | Description |
| ----- | --- | --- |
|Adminstrative bounderies | [HDX](https://data.humdata.org/dataset/cod-ab-som?) |The administrative bounderies on level 0-2 for Somalia and Somaliland can be accessed via HDX. For this trigger mechanism we provide the administrative bounderies on level 2 (district level) as a shapefile. We have added the population number for each district derived from Worldpop.|
|Population Counts| [Worldpop](https://hub.worldpop.org/doi/10.5258/SOTON/WP00534) |The worldpop dataset in .geotif rasterformat provides population estimates per hectar for the year 2020 |



## Monitoring Data

The drought trigger mechanism is based on two variable monitoring datasets updated monthly: The SPI-12 forecast produced by ICPAC and the Food Insecurity projection produced by FEWSNET. The SPI-12 is used to capture hazard forecasts while the Food Insecurity Projection captures the dynamic vulnerability. 
In this way upcoming drought events (SPI) that most probably will lead to food insecurity (IPC) will be captured.

| Dataset| Source | Description |
| ----- | --- | --- |
|SPI-12 forecast| [ICPAC](https://www.icpac.net/) |meteorological drought indicator to monitor precipitation anomalies over 12-month accumulation periods|
|IPC Projections| [FEWSNET](https://fews.net/) | five-phase scale providing common standards for classifying the severity of acute or anticipated acute food insecurity. |





### What is the Standarized Precipitation Index (SPI-12)?

The Standardized Precipitation Index (SPI) is a widely used index to characterize meteorological drought.
The Standarized Precipitation Index (SPI-12) compares the total rainfall received at a particular location during the last 12 months with the long-term rainfall mean (42 years) for the same period of time at that location.




### What is IPC Food Security Projection Data?
 
The IPC is a commonly acceepted measure and classification to describe the current and anticipated severity of acute food insecurity. 
The classification is based on a convergence of available data and evidence, including indicators related to food consumption, livelihoods, malnutrition and mortality. Food Insecurity is one of the prioritized impacts of droughts in Somalia which is why it is also used for the triggering mechanism, in a population-weighted index. 



```{figure} /fig/IPC_classes.png
---
height: 100px
name: QGIS LTR Version
align: center
---
```

__IPC Food Security Projection:__

Three times a year (February, June, and October) FEWSNET estimates most likely IPC classes for the upcoming 8 month (near-term and mid-term projection), available from 2019-current. The near-term projection is called ML1 and is a projection for the upcoming 4 month, the mid-term projection is called ML2 and projects the IPC classes for the 4 subsequent months. For the triggering ML1 (near-term) as well as ML2 (mid-term) projections will be considered. 

Outlook updates are produced almost every month and are also taken into account.


__IPC-Population Weighted Index__

To better operationalise the IPC data a simple population-weigthed index was developed. Relative population numbers are weighted based on the respective IPC class they fallin, in order to give the amount of people in a certain IPC class the importance instead of the IPC class only.
Furthermore, population located in a higher IPC class is more important than population located in a lower class. The index is calculated as follows:

$ IPC\ Index =  Weights \times \frac{District\ Pop\ per\ IPC\ Phase}{Total\ District\ Pop}$

Where the weights are defined as:

IPC 1 = 0\
IPC 2 = 0\
IPC 3 = 1\
IPC 4 = 3\
IPC 4 = 6 



The IPC Index represents low-population districts equal to high-population districts. No underrepresentation of high food insecurity of small districts occurs.



### Trigger Input Data Download

The current plans provide that ICPAC will monthly provide the SPI-12 Forcast whereas the IPC data will be pulled from the FEWSNET website. FEWS NET publishes IPC data on its website. 
The main publications plus the updates of the IPC data amount to the publication of new data almost monthly.

__SPI-12 Data__


ICPAC will provide the SPI-12 forecasts on their FTP (File Transfer Protocol). There are different ways to access the FTP-Server. We recommend to install and once set up [FileZilla](https://filezilla-project.org/download.php?platform=win64). This will make your work easily repeatable on a monthly basis.

1. Download Filezilla [here](https://filezilla-project.org/download.php?platform=win64).
2. Install the `.exe` file you have downloaded 
3. Open FileZilla


4. Establish a connection to the FTP Server by insterting the credentials you have been passed (Host, Username and Password) and clicking "Quickconnect".


In FileZilla you have four windows. On the left hand side you will see the folder on your computer in the upper window. By clicking on a folder, the documents in the folder will be shown in the lower left window.
On the right hand side, you will see in the upper window the FTP data folder and by clicking on it, the data will be shown in the lower right window.

In order to pass the data from the FTP Server to your own machine you can simply drag and drop the folder or data from the righthandside windows (FTP-Server) to the lefthandside windows (your Computer). To do so, firstly navigate to your folder where you wneed the latest SPI-12 data to be located `.../FbF_Drought_Monitoring_Trigger/Monitoring/Year_Month_template/SPI_12`. Then drag and drop the latest SPI-12 into the folder.



```{figure} /fig/FileZilla.PNG
---
height: 400px
name: FileZilla Interface
align: center
---
```

__IPC Data__

The IPC Projection data is provided and regulary updated on the [FEWSNET Website](https://fews.net/).
On the website you will have to click on Somalia to acess the data. Alternativley, you can  navigate through `Data` -> `Acute Food Insecurity Data` and enter „Somalia". In the menu you will see different dataformats for different timestamps. Once you find out which timestamp is the most current one find the ZIP download. We need the data in shapefile (.shp) format, which is only included in the ZIP file and not provided as single download file. 


```{figure} /fig/IPC_Projections_website.png
---
height: 400px
name: FEWSNET IPC - Download IPC Projections
align: center
---
```

Once downloaded the ZIP folder, right click on it and unzip it. You will see various datasets. We are interested in the ML1 and ML2 projections. The filename is composed of "SO" for Somalia, year and month of the report month of the respective projection and _ML1 or _ML2 forn the respective projection. This is what the the dataname for ML1 and ML2 projections published in August would look like:

`"SO_202308_ML1.shp"`,
`"SO_202308_ML2.shp"`

You can then copy the respective shapefiles to you folder 

`.../FbF_Drought_Monitoring_Trigger/Monitoring/Year_Month_template/IPC_ML1` and
`.../FbF_Drought_Monitoring_Trigger/Monitoring/Year_Month_template//IPC_ML2`

Remember that you need to copy over all components that the respective [shapefile](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_geodata_types_wiki.html#vector-data) is composed of. Most probably it has 5 components: .cpg, .dbf, .prj, .shp, and .shx.


```{figure} /fig/IPC_zip.PNG
---
height: 400px
name: Content of .zip file downloaded containing ML1 and ML2 IPC projections
align: center
---
```

```{tip}
On the [main FEWSNET page](https://fews.net/) you can also sign up for information on latest updates via email. For this option scroll down to the end of the page and click on `Sign up for Emails`. You will then get the option to choose updates only for Somalia.

```{figure} /fig/IPC_Newsletter.png
---
height: 60px
name: FEWSNET Newsletter
align: center
---
```



## Making print map

In order to easily visualize the outout of the trigger analysis we provide you with a 
[map template](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html#map-templates) that you can be used as a base for your visualization.

Check [here](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html#map-templates) how to open templates and how to use them in QGIS.

You can also adapt the template to your needs and preferences. You can find help [here](https://giscience.github.io/gis-training-resource-center/content/Modul_4/en_qgis_map_design_2.html#print-layout).
