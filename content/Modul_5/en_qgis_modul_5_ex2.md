# Exercise: Intervantion Map

__🔙[Back to Homepage](/content/intro.md)__

🚧This training platform and the entire content is under ⚠️construction⚠️ and may not be shared or published! 🚧

## Aim of the exercise:

In this exercise, you will learn how to digitise the positions of settlements by creating new datasets. Furthermore, you will learn how to enrich the simple geodata set with additional information.

## Background 

This exercise is based on the monitoring and triggering process used by the Somalia Red Cresent Society (SRCS) in the framework of a drought Early Action Protocol (EAP).

Within this exercise, you will build a simplified version of the monitoring and trigger mechanism for FEWSNET projection pillar.  

Setting triggers is one of the cornerstones of the Forecast-based Financing system. For a National Society to have access to automatically released funding for their early actions, their Early Action Protocol needs to clearly define where and when funds will be allocated, and assistance will be provided. In FbF, this is decided according to specific threshold values, so-called triggers, based on weather and climate forecasts, which are defined for each region (see [FbF Manual](https://manual.forecast-based-financing.org/en/chapter/set-the-trigger/)).

For the development of the Somaliland-Somalia Drought Trigger mechanism various datasources were thoroughly analysed.
Finally, the main parameters chosen for the trigger based on the historical impact assessment are the twelve month Standard Precipitation Index (SPI12) and the IPC acute food insecurity classification. The exact data used are the documented and forecasted SPI12 (source: ICPAC) and the forecasted IPC classification (8 month forecast, source: FEWSNET), that is used to calculate a population weighted index of food insecurity. The trigger thresholds for both components were optimised towards the most favourable proportion of hit rate and false alarm rate. The emerging thresholds were <-1 for the SPI12 and >=0,7 for the IPC based index. The triggering is done on district level and per district just one trigger initiation per year is possible.

```{admonition} Trigger Statement
When ICPAC issues a SPI-12 forecast of less than -1 for a district AND the current FEWSNET food insecurity projection reaches at least 0.7 in its 
derived population weighted index in the same district, then we will act in this district. We expect the lead-time to be 90 days.
```



## Relevant Wiki Articles

## Data

### Food Insecurity Projection data

The drought trigger mechanism is based on two variable monitoring datasets. One of them Food Insecurity projection produced by FEWSNET which is updated ruffly every month.

| Dataset| Source | Description |
| ----- | --- | --- |
|IPC Projections| [FEWSNET](https://fews.net/) | five-phase scale providing common standards for classifying the severity of acute or anticipated acute food insecurity. |

#### What is IPC Food Security Projection Data?
 
The IPC is a commonly acceepted measure and classification to describe the current and anticipated severity of acute food insecurity. 
The classification is based on a convergence of available data and evidence, including indicators related to food consumption, livelihoods, malnutrition and mortality. Food Insecurity is one of the prioritized impacts of droughts in Somalia which is why it is also used for the triggering mechanism, in a population-weighted index. 

| Colour| Phase | Descriptions |
| ----- | --- | --- |
|![](/fig/IPC_Class_1.drawio.svg)|1. Minimal   |Households are able to meet essential food and non-food needs without engaging in atypical and unsustainable strategies to access food and income.   |
|![](/fig/IPC_Class_2.drawio.svg)|2. Stressed   |Households have minimally adequate food consumption but are unable to afford some essential non-food expenditures without engaging in stress-coping strategies.  |
|![](/fig/IPC_Class_3.drawio.svg)|3. Crisis   |Households either have food consumption gaps that are reflected by high or above-usual acute malnutrition __OR__ are marginally able to meet minimum food needs but only by depleting essential livelihood assets or through crisis-coping strategies.  |
|![](/fig/IPC_Class_4.drawio.svg)|4. Emergency|Households either have large food consumption gaps which are reflected in very high acute malnutrition and excess mortality; __OR__ are able to mitigate large food consumption gaps but only by employing emergency livelihood strategies and asset liquidation.|
|![](/fig/IPC_Class_5.drawio.svg)|5. Famine |Households have an extreme lack of food and/or other basic needs even after full employment of coping strategies. Starvation, death, destitution, and extremely critical acute malnutrition levels are evident. (For Famine Classification, area needs to have extreme critical levels of acute malnutrition and mortality.)  |


##### IPC Food Security Projection:

Three times a year (February, June, and October) FEWSNET estimates most likely IPC classes for the upcoming 8 month (near-term and mid-term projection), available from 2019-current. The near-term projection is called ML1 and is a projection for the upcoming 4 month, the mid-term projection is called ML2 and projects the IPC classes for the 4 subsequent months. For the triggering ML1 (near-term) as well as ML2 (mid-term) projections will be considered. 

Outlook updates are produced almost every month and are also taken into account.