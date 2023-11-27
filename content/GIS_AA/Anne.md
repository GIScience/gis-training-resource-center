
## Trigger Statement

When ICPAC issues a SPI-12 forecast of less than -1 for a district AND the current FEWSNET food insecurity projection reaches at least 0.7 in its 
derived population weighted index in the same district, then we will act in this district. We expect the lead-time to be 90 days.


##  Trigger Input Data

The drought trigger mechanism is based on two datasets: The SPI-12 forecast produced by ICPAC and the Food Insecurity projection produced by FEWSNET. 
The SPI-12 is used to capture hazard forecast while the Food Insecurity Projection captures the dynamic vulnerability. 
In this way upcoming drought events (SPI) that most probably will lead to food insecurity (IPC) will be captur



### What is the Standarized Precipitation Index (SPI-12)?

The Standardized Precipitation Index (SPI) is a widely used index to characterize meteorological drought.
The Standarized Precipitation Index (SPI-12) compares the total rainfall received at a particular location during the 
last 12 months with the long-term rainfall mean (42 years) for the same period of time at that location.




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

IPC 1 = 0

IPC 2 = 0

IPC 3 = 1 

IPC 4 = 3

IPC 4 = 6 



The IPC Index represents low-population districts equal to high-population districts. No underrepresentation of high food insecurity of small districts occurs.





### Trigger Input Data Download

The current plans provide that ICPAC will monthly provide the SPI-12 Forcast whereas the IPC data will be pulled from the FEWSNET website. FEWS NET publishes IPC data on its website. 
The main publications plus the updates of the IPC data amount to the publication of new data almost monthly.

__SPI-12 Data__


ICPAC will provide the SPI-12 forecasts on their FTP (File Transfer Protocol). There are different ways to access the FTP-Server. We recommend to install and once set up [FileZilla](https://filezilla-project.org/download.php?platform=win64).




HOST: 197.254.13.228

USER: ftpuser

PASS: ftp#234

PORT: leave blank



__IPC Data__

The IPC Projection data is provided and regulary updated on the [FEWSNET Website](https://fews.net/).
On the website you will have to click on Somalia to acess the data. Alternativley, you can  navigate through Data --> Acute Food Insecurity Data and enter „Somalia". In the menu you will see different dataformats for different timestamps. Once you find out which timestamp is the most current one find the ZIP download. We need the data in shapefile (.shp) format, which is only included in the ZIP file and not provided as single download file. 


```{figure} /fig/IPC_Projections_website.png
---
height: 100px
name: FEWSNET IPC - Download IPC Projections
align: center
---
```

Once downloaded the ZIP folder, right click on it and unzip it. You will see various datasets. We are interested in the ML1 and ML2 projections. The filename is composed of "SO" for Somalia, year and month of the report month of the respective projection


"SO_202308_ML1.shp"

"SO_202308_ML2.shp"


On the [main FEWSNET page](https://fews.net/) you can also sign up for information on latest updates via email. For this option scroll down to the end of the page and click on "Sign up for Emails". You will then get the option to choose updates only for Somalia.

```{figure} /fig/IPC_Newsletter.png
---
height: 100px
name: FEWSNET Newsletter
align: center
---
```


