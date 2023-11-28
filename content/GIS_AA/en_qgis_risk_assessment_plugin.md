# Risk Assessment QGIS Plugin


## Introduction & Purpose

In the context of the Forecast based Financing methodology the conduction of a robust risk assessment is a crucial step towards the development of an Early Action Protocol. A risk analysis serves to understand what kinds of disaster impacts can be expected from a particular type of hazard and to identify who and what is exposed and vulnerable to this hazard and why. By overlaying the information on exposure, vulnerability and lack of coping capacity, it will become clear which areas are predicted to be most severely impacted. These areas can then be targeted as priority areas for early action to ensure the most at-risk communities receive assistance before the event happens.
The collection and processing of this information varies throughout different contexts but the calculation scheme to combine the information to a risk score remains consistent. At HeiGIT we have developed a risk assessment workflow that is applicable across different countries and disaster contexts. To make the process more user-friendly, we have chosen to convert it into a QGIS Plugin. This makes it more accessible and easier to use, especially for individuals with limited technical knowledge.
The plugin automatically calculates the risk based on the exposure, susceptibility and coping capacity indicators entered by the user. Hereby the user cannot only assign different weights and directions to the indicators but also receive different population measures based on worldpop data (sex and age structures) and offset them against chosen indicators.


## Requirements & Installation

The use of the plugin requires Python pandas to be installed on your system.
You can check in QGIS directly if you have it installed or not:

1. Open the Python Console in QGIS

        - Launch QGIS
        - In the menu bar click on Plugins
        - Select Python Console

2. Check if Pandas is installed

        - In the Python Console type the following command and press ENTER:
        Import pandas


If the library is installed, this command will execute without error, and you won’t see any error messages.
If pandas is not installed, you will see error messages indicating that the respective module cannot be found. In that case, you will need to install the missing library. You can install pandas using pip:
Install pandas on Windows/ Mac:\

- Open the Command Prompt (Windows)/ Terminal (Mac)
- Install pandas by running the following command and press ENTER:
pip install pandas

__QGIS Versions__

The Plugin is available for QGIS Version 3.28 onwards.


## Getting Started

To install plugins, you need to open the Plugin Manager:
- Click on the menu item Plugins > Manage and install Plugins.
- Click on Settings and check the box “Show also experimental plugins”


```{figure} /fig/experimental_plugins.PNG
---
height: 400px
name: experimental_plugins
align: center
---
```

- In the dialog that opens, find the Risk Assessment plugin.
- Find information about the plugin by selecting it in the list.
- Install it by clicking the Install Plugin button below the plugin information panel.
- Close the dialog. The Risk Assessment plugin should now be available.

How to open the plugin interface:

- To use the Risk Assessment plugin open the Processing Toolbox.
- The Toolbox shows a list of all available algorithms.
- At the bottom it should list HeiGIT Risk Assessment.
you can also search for “Risk Assessment” using the Search function of the Processing Toolbox
- To execute the plugin, just double-click on its name.
- A dialog called Calculate Risk Assessment should appear.

For further information about installation and usage of plugins visit the [QGIS Training Platform](https://giscience.github.io/gis-training-resource-center/content/Wiki/en_qgis_plugins_wiki.html).


## User Interface

The plugin needs 7 inputs, from which 6 are csv text files and 1 is a vector file. The input of these 7 files is mandatory. The majority of the files can be produced and adjusted in Excel. This allows for flexibility to adjust input to local contexts.
The requested input information can be browsed for via the button on the right. These files need to be present on the user's computer.
It is important to follow the input file specifications exactly (see chapter 4.1.).
The plugin will provide the user with two outputs. The Risk Assessment results on the administrative boundaries as a vector file containing geometries ready to be displayed in QGIS and the Risk Assessment results in a table format. The desired data format of the vector and text outputs can be chosen during the saving process. 


```{figure} /fig/Interface.PNG
---
height: 400px
name: Interface
align: center
---
```


## Data Input

The required input files must follow a given structure. You find below  the required input files to conduct the risk assessment and specifications they must follow:

### 1. Administrative boundaries level 2

A geospatial vector format (geojson, geopackage, shapefile,…) containing the administrative boundaries on admin level 2 and P-Codes of the respective countries. These can be found on the websites of national governments or on Humanitarian Data Exchange, for example. The administrative boundary data does not require a specific coordinate reference system (CRS), but the output and result will have the same CRS as the input.

### 2. Risk Assessment indicators

For the Risk Assessment indicators the following 3 “csv”-files are mandatory:

a) __Exposure indicators:__ A "csv"-file containing a mandatory column "ADM2_PCODE" with the district codes and all columns that are included in the calculation of the exposure-indicator. All columns that are not included in the calculation must start with the expression "ADM..." (for example “ADM_NAMES”)./

b.) __Vulnerability indicators:__ A "csv"-file containing a mandatory column "ADM2_PCODE" with the district codes and all columns that are included in the calculation of the vulnerability-indicator. All columns that are not included in the calculation must start with the expression "ADM..."./

c) __Coping Capacity indicators:__ A "csv"-file containing a mandatory column "ADM2_PCODE" with the district codes and all columns that are included in the calculation of the coping-indicator. All columns that are not included in the calculation must start with the expression "ADM...".


```{figure} /fig/IIndicators_Vulnerability.PNG
---
height: 400px
name: Indicators_Vulnerability
align: center
---
```

