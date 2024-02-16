# Historical Impact Assessment (HIA) for Flood in Sudan
In 2023, the Sudan Red Cresent (SRCS), German Red Cross (GRC),  the Red Cross Red Crescent Climate Center (RCRCCC) and the Heidelberg Institute for Geoinformation Technology (HeiGIT) worked on an Early Action Protocol (EAP) for riverine floods along the River Nile in Sudan.
One of the fundamental tasks while working on an EAP is to conduct a Historical Impact Assessment (HIA), for the particular hazard. The team of HeiGIT was responsible for this particular task and this article will tell the story of how they tackled the task.
Due to the outbreak of hostilities in Sudan in 2023, the team could only rely on public data from the internet and some reports and data provided by SRCS.
By the end of 2023, the team had collected, 3.204 rows of data from 60 sources, covering the timeframe from 2012 to 2023.

## Why is a Historical Impact Assessment (HIA) Important?
A HIA has two purposes. First, understanding in detail what kind of problems are caused by a particular hazard, allows people to make informed decisions on the selection of early actions to counter those problems.
Secondly, without a good understanding of which magnitude of flood causes significant humanitarian impact, one can not adjust trigger levels accordingly to tackle those significant events.

## Task
Conduct an HIA to gain a detailed understanding of the impact of past flood events on the highest spatial and temporal resolution possible.

## Challenges

What were the main problems and challenges we faced while conducting the HIA?

### Challange 1: Scatert information on flood impacts
The one BIG challenge in this case was that there are no good datasets on flood impacts in Sudan. Practically, all information is scattered across a huge number of reports, maps, tables, dashboards and newspaper articles. Such documents can be found for example on RelifeWeb.
### Challange 2: How to get diverse data in one easy-to-use data format
Since all information about flood impacts is contained in such a diverse range of documents and formats, it is difficult to bring the information together in one dataset.
### Challange 3: Differentiating between riverain flood impacts and flash flood impacts
Ricereich and flash floods often occur at the same time in the same place, so it is almost impossible to state what was the exact cause of the impact. 
And even when there was a single flash flood event, in reports it is often referred to as a flood. Hence, there is the real risk that impacts caused by flash floods are listed as river flood impacts.
## Key concept of our methodology
Our goal was to store all available impact information in one table or dataset. If we would use a classic weight table we would end up with a super clumsy table since there are so many different types of impacts a flood can cause. To avoid that we decided to use a long table.
The advantages of a long table over a classic wider table in this context are:

| Advantages          |                                                                                             |
|---------------------|---------------------------------------------------------------------------------------------|
| Flexibility         | Long tables can accommodate a variable number of attributes, making them suitable for diverse datasets. |
| Scalability        | They can handle large datasets efficiently, making them suitable for compiling extensive information. |
| Ease of Integration | Simplifies the integration of data from various sources, providing a consistent structure. |
| Compatibility      | Many analysis tools work well with long-format data, making it easier to analyze and derive insights. |




```{figure} /fig/key_value_concept.drawio.svg
---
name: 
align: center
---
```


## Step by Step HIA Sudan

```{figure} /fig/14022024_Sudan_HIA.drawio.svg
---
name: 
align: center
---
```

### Step 1: Area of Interest
The Area of Interest (AOI) for the HeiGIT team was formally limited to Khartoum, Northern, White Nile and Sennar. However, the analysis and data collection were conducted for all states of Sudan.


```{figure} /fig/Sudan_AOI_HIA.jpg
---
name: 
width: 500px
align: center
---
```
### Step 2. Finding Flood Disaster Timeframes

We want to tie single pieces of information like impacts, to knowen flood events in Sudan. Thus we first need a comprehensive list of such events. In the case of Sudan, there are two sources, EM-DAT and RelifeWeb. EM-DAT is a disaster database that lists events above a certain severity. 
RelifeWeb is actually an information platform for humanitarian response. But it has a list of active and past disasters as well. 
Both databases list the same events for the most part. By comparing the two datasets and only selecting unique events, we receive a list of all significant flood events in Sudan and the timeframes of all events.

* EM-Dat lists 21 flood events in Sudan from 2000 to 2024
* Relief Web lists 29 events between 1988 and 2024

In total, there were 35 flood events reported between 1988 and 2021
In some cases, the start and end dates cannot precisely be identified. This is not a problem, we only want to have a rough overview about when there have been floods. 

```{dropdown} Flood Events List

| Start Year | Start Date | End Date   |
|------------|------------|------------|
| 1988       | 1988-08-06 | 1988-09-15 |
| 1994       | 1994-09-20 | 1988-10-21 |
| 1996       | 1996-08-12 | 1996-10-23 |
| 1998       | 1998-09-04 | 1998-10-15 |
| 2001       | 2001-08-06 | 2001-09-13 |
| 2002       | 2002-08-03 | 2002-08-03 |
| 2003       | 2003-07-28 | 2003-08-21 |
| 2005       | 2005-08-29 | 2005-09-06 |
| 2005       | 2005-07-14 | 2005-07-15 |
| 2006       | 2006-08-13 | 2006-09-26 |
| 2006       | 2006-08-07 | 2006-08-07 |
| 2007       | 2007-07-03 | 2007-10-08 |
| 2009       | 2009-08-16 | 2009-08-26 |
| 2010       | 2010-07-10 | 2010-07-15 |
| 2010       | 2010-07-01 | 2010-10-07 |
| 2012       | 2012-08-01 | 2012-08-12 |
| 2013       | 2013-08-01 | 2013-08-21 |
| 2014       | 2014-07-25 | 2014-09   |
| 2015       | 2015-08-08 | 2015-08-09 |
| 2017       | 2017-06-30 | 2017-08-14 |
| 2018       | 2018-06-18 | 2018-06-27 |
| 2018       | 2018-07-23 | 2018-07-30 |
| 2019       | 2019-06-08 | 2019-06-18 |
| 2020       | 2020-06   | 2020-09-09 |
| 2021       | 2021-07-20 | 2021-09-24 |
```

### Step 3: Selecting datasets 

Now we search for datasets and other information for each of the flood events identified in step 2. Naturally, it will be much easier to find information on more recent events. This process can take a lot of time and sometimes needs multiple iterations.

There are three principal sources of datasets. The Sudan Red Cresent Society (SRCS), RelifeWeb and Floodlist.

<style>
  .container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }

  .organization {
    width: 50%; 
  }

  .logo {
    width: 35%; 
    text-align: right;
  }
  
  .bold-header {
    font-weight: bold;
  }
</style>


<div class="container">
  <div class="organization">
    <p><strong>Sudan Red Crescent Society (SRCS)</strong><br>
      SRCS has documentation about flood impacts and past operations. Furthermore, SRCS was able to source some datasets from the Sudan National Council for Civil Defence (NCCD)  and the Sudan Humanitarian Aid Commission (HAC).
    </p>
  </div>

  <div class="logo">
    <img src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/Sudan_SRCS_logo.png" alt="Sudan Red Crescent Society (SRCS) Logo">
  </div>
</div>


<div class="container">
  <div class="organization">
    <p><strong>ReliefWeb</strong><br>
      ReliefWeb is the largest database for humanitarian reports and bulletins. The datasets are very conveniently organized based on specific flood events. This makes it easy to match information with an event.
    </p>
  </div>

  <div class="logo">
    <img src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/RelifeWeb_Logo_short.png" alt="ReliefWeb Logo">
  </div>
</div>

<div class="container">
  <div class="organization">
    <p><strong>Flood List</strong><br>
      Floodlis is a news portal all about floods. The articles are ordered chronologically.
    </p>
  </div>

  <div class="logo">
    <img src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/floodlist-logo-1101.png" alt="Floodlist Logo">
  </div>
</div>


Of course, much information from the different sources is redundant. A significant part of the work is to sift through the datasets and identify unique information. 


#### Datasets

We use the term data set to refer to all types of publications from which we can obtain data.
In the table below we list typical datasets used in the Sudan HIA. Remember, we can pull all kinds of information out of a dataset. It does not have to be quantitative or in table format or anything like that. It can also be info directly from texts or graphics.


| Typical Publishing Organisation (Examples) | Type                         | Example                                                              | Typical Features                                    |
|--------------------------------------------|------------------------------|----------------------------------------------------------------------|-----------------------------------------------------|
| IFRC                                       | Emergency Plan of Action    | [Emergency Plan of Action (EPoA) Sudan: Floods 2018](https://reliefweb.int/report/sudan/sudan-floods-2018-emergency-plan-action-epoa-dref-operation-n-mdrsd026)                  | Tables; Graphics; Maps; Info directly from texts   |
| IFRC                                       | Flood Interagency Assessment Reports | Not public                                                       | Tables; Graphics; Maps; Info directly from texts   |
| IFRC                                       | Government Datasets         | Not public                                                           | Tables in many different forms                     |
| UN OCHA                                    | Humanitarian Bulletins      | [Sudan Humanitarian Bulletin Issue 18/ 8 October – 4 November 2018](https://reliefweb.int/report/sudan/sudan-humanitarian-bulletin-issue-18-8-october-4-november-2018-enar) | Tables; Graphics; Maps; Info directly from texts   |
| UN OCHA                                    | (Flood) Situation Reports  | [SUDAN Situation Report 13 Nov 2020](https://reliefweb.int/report/sudan/sudan-situation-report-13-nov-2020-enar)                                  | Tables; Graphics; Maps; Info directly from texts   |
| UN OCHA                                    | Humanitarian Snapshots      | [Sudan: Humanitarian Snapshot - September 2021 (as of 18 October 2021)](https://reliefweb.int/report/sudan/sudan-humanitarian-snapshot-september-2021-18-october-2021) | Tables; Graphics; Maps; Info directly from texts   |
| UN OCHA                                    | Dashboards                  | [Sudan Floods: People & areas affected 25 October 2022](https://app.powerbi.com/view?=eyJrIjoiZWVmMmU3YzMtNGNkMC00NDU3LWFmOTItM2ZmMjc3YjZhOGI2IiwidCI6IjBmOWUzNWRiLTU0NGYtNGY2MC1iZGNjLTVlYTQxNmU2ZGM3MCIsImMiOjh9)              | Data in Excel or CSV data format                   |
| World Bank                                 | Large Reports               | [Sudan Rapid Post Disaster Needs and Recovery Assessment (Rapid PDNRA)](https://reliefweb.int/report/sudan/sudan-rapid-post-disaster-needs-and-recovery-assessment-rapid-pdnra) | Tables; Graphics; Maps; Info directly from texts   |
| Floodlist                                  | Newspaper Articles          | [Sudan – North Darfur Town Devastated by Rains, Flash Floods](https://floodlist.com/africa/sudan-north-darfur-floods-october-2019)                                                                     | Info directly from texts                            |


##### Data selection parameters

In general, we can use any kind of dataset e.g. reports, maps, bulletins, tables…. However, we do not need to check all datasets available for one event. The selection of datasets is based on two principal parameters. 


##### Currentness

The assumption is that later after the event, the picture of what happens becomes clearer, thus the data report is more reliable.
This means., if you have multiple similar datasets containing similar data, chose the newer one.

In this example, the later map from the [13th of November](https://reliefweb.int/report/sudan/sudan-situation-report-13-nov-2020-enar) shows more affected people for instance in Central Darfur the the map publihsed on the [9th of November](https://reliefweb.int/report/sudan/sudan-situation-report-9-nov-2020-enar).


::::{grid} 2
:::{card} SUDAN Situation Report 09 Nov 2020
```{figure} /fig/Map_affected_pop_20201109.png
---
name: 
width: 4500px
---
```
:::
:::{card} SUDAN Situation Report 13 Nov 2020
```{figure} /fig/Map_affected_pop_20201113.png
---
name: 
width: 4500px
---
```
:::
::::

##### Uniqueness
It is important to not only use data from one source becaus of confience. 
The assumption is that different organisations have different capacities and work in different areas, thus they may have better information in some locations of sectors than other organisations.

#### Dataset ID
When selecting datasets it is important to save the datasets on your computer. To be able to later retrace which piece of information was taken from which datasets, we have to give the datasets unique identification codes.
In the Sudan project, we used the simple structure year of the flood the document is referring to (for example 2019), the publishing organisation (for example IFRC) and the publishing date (for example 20191003).

```{figure} /fig/Sudan_HIA_ID.drawio.svg
---
name: 
width: 8000px
---
```

#### Step 3: Outcome 
At the end of the selection process, you should have multiple relevant datasets with IDs for every event, covering all relevant areas and sectors.


```{figure} /fig/Sudan_HIA_dataset_typ_overview.drawio.svg
---
name: 
align: center
---
```
```{dropdown} All datasets with ID used by HeiGIT
| 2012                      | 2013                      | 2014                      | 2016                      | 2017                      |
|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|
| 2012_IFRC_20120531.pdf       | 2013_Floodlist_20130816.pdf  | 2014_Floodlist_20140801.pdf  | 2016_IFRC_20160902.pdf       | 2017_floodlist_20170825.pdf  |
| 2012_IFRC_20120910.pdf       | 2013_Floodlist_20130827.pdf  | 2014_Floodlist_20140804.pdf  | 2016_OCHA_20160828.pdf       | 2017_floodlist_20170829.pdf  |
|                               | 2013_IFRC_20131010.pdf       | 2014_Floodlist_20140814.pdf  |                               | 2017_floodlist_20170905.pdf  |
|                               | 2013_OCHA_20130915.pdf       | 2014_Floodlist_20140920.pdf  |                               | 2017_floodlist_20170906.pdf  |
|                               | 2013_OCHA_20130919.pdf       | 2014_IFRC_20140925.pdf       |                               | 2017_HAC_20170919.pdf        |
|                               | 2013_OCHA_20130930.pdf       | 2014_OCHA_20140909.pdf       |                               |                               |
|                               | 2013_OCHA_HAC_20130902.pdf   | 2014_OCHA_20140914.pdf       |                               |                               |
|                               |                               | 2014_RelifeWeb_20140915.pdf  |                               |                               |
|                               |                               | 2014_RelifeWeb_20141009.pdf  |                               |                               |
|                               |                               | 2014_SRCS_20140903.pdf       |                               |                               |

| 2018                      | 2019                      | 2020                      | 2021                      | 2022                      | Extra                   |
|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-----------------------------|
| 2018_floodlist_20180625.pdf  | 2019_ECHO_20190906.pdf       | 2020_OCHA_20201025.pdf       | 2021_OCHA_20211011.xlsx      | 2022_OCHA_20221025.xlsx      | HAC_1_affected.pdf         |
| 2018_floodlist_20181105.pdf  | 2019_floodlist_20190613.pdf  | 2020_PDNRA_20210531.pdf      | 2021_OCHA_20211018.pdf       |                               | Interagency_mission2022.pdf|
| 2018_floodlist_DG_ECHO_20180824.pdf | 2019_floodlist_20190816.pdf  |                               |                               |                               | NCCD_1_Impact.xlsx          |
| 2018_IFRC_20180813.pdf       | 2019_floodlist_20190821.pdf  |                               |                               |                               |                           |
| 2018_OCHA_20180819.pdf       | 2019_floodlist_20190901.pdf  |                               |                               |                               |                           |
| 2018_OCHA_20181104.pdf       | 2019_floodlist_20191008.pdf  |                               |                               |                               |                           |
|                               | 2019_OCHA_20191003.pdf       |                               |                               |                               |                           |
|                               |                               |                               |                               |                               |                           |
|                               |                               |                               |                               |                               |                           |
|                               |                               |                               |                               |                               |                           |
```
### Step 4: Preparing Excel table Structure
Before we can start compiling data, we need to prepare the table structure we will use. The table needs to accommodate four components. __Date__, __data source__, __location__,and __impact information__.

#### Date
The date information must accommodate the flood event information from the list of flood events prepared in Step 2. And potential dates of specific impact information. 
The date portion of the whole Excel table would look like this:



| Start Year | Start Date | End Date   | Date       |
|------------|------------|------------|------------|
| 2018       | 2018-07-01 | 2018-08-29 | 2018-07-12 |
| 2019       | 2019-06-01 | 2019-06-31 |  |
|2020      | 2020-07-20 | 2020-08-11 | |

#### Data source
This section is simply one column with the ID of the dataset from which the particular information was taken.

|source_ID|
|---------|
|2018_OCHA_20180819.pdf  |
|2019_floodlist_20190613.pdf|
|2020_PDNRA_20210531.pdf|

#### Location
Practical all impact information refers to state, locality, town or refugee/IDP camp level. This means we need a column for each of these levels and one column to indicate the level the information is referring to. In this way, we can later filter for all information on for example locality level.

|admin_level | admin_1 | admin_2 | admin_3 | admin_camp|
|------------|---------|---------|---------|------------|
|      State      |    West Kordofan      |       |         |           |
|       Locality    |     South Darfur    |Beliel         |         |           |
|          Camp  |    South Darfur     |    Beliel     |         |       Kalma Camp    |

#### Impact information
The actual impact information consists of two parts. One part is always the impact type. This explain what happened. For example, people were affected by the flood, the cholera broke out or schools got damaged. 

The other part is either the impact quantity or the impact quality. It can not be both! 
The impact quantity describes simply how many of something. How many people have been affected? How many schools got damaged?

The impact quality is used if something cannot be described with numbers. For example, there was a disease outbreak of cholear. Cholera is not a number. Or a locality was affected -> Yes the locality was affected.

Hence we need three columns to describe impacts: impact_typ, impact_quality and impact_quantity.

| impact_typ | impact_quality | impact_quantity |
|------------|----------------|-----------------|
| houses_damaged_totaly           |   2500             |                 |
|      deaths      |              6    |               |
|      disease_outbreak      |               |         Cholera         |

It makes sense to list some of the basic impact types we are interested in or which are very commonly reported. Such as affected people or deaths. The list of impact types can be extended on the fly. It is however important to stay consistent.
The HeiGIT team used 75 different impact types. You can find the whole list below.


```{dropdown} Impact taypes used in Sudan HIA
| Impact Type                               | Description                                            |
|-------------------------------------------|--------------------------------------------------------|
| Affected                                  |                                                        |
| Agricultural_land_affected                |                                                        |
| Agriculturalsectors_fedan                 |                                                        |
| Agriculture_Affected                      |                                                        |
| Agriculture_Bananplantation_damged_totally|                                                        |
| Agriculture_crops_damaged                 |                                                        |
| Agriculture_Livestock_crops_damaged       |                                                        |
| Deaths                                    |                                                        |
| Diseases                                  |                                                        |
| Economic                                  |                                                        |
| Evacuation                                |                                                        |
| Event                                     |                                                        |
| Eviromental_sanitation                    |                                                        |
| Flooding                                  |                                                        |
| Foodprice_increas                         |                                                        |
| Healt_center_affected                     |                                                        |
| Health_damaged_partially                  |                                                        |
| Health_damaged_totally                    |                                                        |
| HH_Affected                               |                                                        |
| HH_displaced                              |                                                        |
| Houses_damaged_partially                  |                                                        |
| Houses_damaged_totally                    |                                                        |
| Infrastructure_damaged_partially          |                                                        |
| Infrastructure_electricity_damaged_partially|                                                      |
| Injuries                                  |                                                        |
| Institutions_damaged_partially            |                                                        |
| Institutions_damaged_totally              |                                                        |
| Livestock_Cattle                          |                                                        |
| Livestock_Deaths                          |                                                        |
| Livestock_Goats                           |                                                        |
| Livestock_Poultry                         |                                                        |
| Livestock_Sheep                           |                                                        |
| Mosques_damaged_partally                  |                                                        |
| Mosques_damaged_totally                   |                                                        |
| Mosquitos                                 |                                                        |
| Others                                    |                                                        |
| Pop_affected                              |                                                        |
| Pop_displaced                             |                                                        |
| Problem_Health_access                     |                                                        |
| Problem_Water_access                      |                                                        |
| Protection_Issus                          |                                                        |
| Public_facilities_damaged_partially       |                                                        |
| Public_facilities_damaged_totally         |                                                        |
| Public_facilities_damged_partially        |                                                        |
| Public_facilities_damged_totally          |                                                        |
| Public_facilities_schools_affected        |                                                        |
| Sanitation_partially                      |                                                        |
| School_dropout                            |                                                        |
| Schools_affeacted                         |                                                        |
| Schools_damaged_partially                 |                                                        |
| Schools_damaged_totally                   |                                                        |
| Schools_Primary_damaged_partially         |                                                        |
| Schools_Primary_damaged_totally           |                                                        |
| Schools_Secondary_damaged_partially       |                                                        |
| Schools_Universities_damaged_partially    |                                                        |
| Shelter                                   |                                                        |
| Shops_damaged_partally                   |                                                        |
| Shops_damaged_totally                     |                                                        |
| Villages_affacted                         |                                                        |
| WASH_damaged_partally                    |                                                        |
| WASH_damaged_totally                     |                                                        |
| WASH_drinking_river                       |                                                        |
| WASH_home_latrines_damaged_partially     |                                                        |
| WASH_latriens_damaged_totally            |                                                        |
| WASH_latrines_affected                   |                                                        |
| WASH_latrines_damaged_partially          |                                                        |
| WASH_latrines_damaged_partially          |                                                        |
| WASH_Latrines_damaged_totally            |                                                        |
| WASH_latrines_damaged_totaly             |                                                        |
| WASH_open_defecation                     |                                                        |
| WASH_sewage_damaged_totally              |                                                        |
| WASH_Water_station_affected              |                                                        |
| WASH_Water_station_source_damaged_partially|                                                      |
| WASH_Water_station_source_damaged_totally |                                                        |
| WASH_watersource_contaminated            |                                                        |

```
### Step 4: Outcome
Now we have your final table structure. We can put ALL information from the selected datasets we deem relevant into this table structure thus creating a consistent historical impact dataset.


| Start Year | Start Date | End Date   | Date       | source_ID              | admin_level | admin_1        | admin_2 | admin_3 | admin_camp   | impact_typ           | impact_quality | impact_quantity |
|------------|------------|------------|------------|------------------------|-------------|----------------|---------|---------|--------------|----------------------|----------------|-----------------|
| 2018       | 2018-07-01 | 2018-08-29 | 2018-07-12 | 2018_OCHA_20180819.pdf | State       | West Kordofan  |         |         |              |  disease_outbreak                     |     Cholera            |                 |
| 2019       | 2019-06-01 | 2019-06-31 |            | 2019_floodlist_20190613.pdf | Locality    | South Darfur   | Beliel  |         |              |          deaths             |                |       6          |
| 2020       | 2020-07-20 | 2020-08-11 |            | 2020_PDNRA_20210531.pdf | Camp        | South Darfur   | Beliel  |         | Kalma Camp   | houses_damaged_totaly |            |     2500            |
|            |


### Step 5: Data compiling

During the data compilation, we simply identify the relevant information in the dataset and transfer it into the table. Below you can find some examples of the process.

::::{grid} 1
:::{card} 

#### Emergency Plan of Action (EPoA) Sudan: Floods 2018

This is a small extract from Emergency Plan of Action (EPoA) Sudan: Floods 2018 page 4.

```{figure} /fig/2018_IFRC_20180813_snap_shot.png
---
width: 600px
name: 
align: center
---
```


```{dropdown} Data extracted from dataset
| Year | Start_Date | End_Date | Date       | source_ID            | admin_level | admin_1       | admin_2 | admin_3 | admin_camp | Impact type                | Impact_quantity | Impact_quality |
|------|------------|----------|------------|----------------------|-------------|---------------|---------|---------|------------|----------------------------|-----------------|----------------|
| 2018 | 23/07/2018 | 30/07/2018 | 23/07/2018 | 2018_IFRC_20180813  | Locality    | West Kordofan | Elnohoud|         |            | houses damaged_totaly      | 2500            |                |
| 2018 | 23/07/2018 | 30/07/2018 | 23/07/2018 | 2018_IFRC_20180813  | Locality    | West Kordofan | Einhoud |         |            | houses_damaged_partially  | 1500            |                |
| 2018 | 23/07/2018 | 30/07/2018 | 23/07/2018 | 2018_IFRC_20180813  | State       | West Kordofan |         |         |            | deaths                     | 6               |                |
| 2018 | 23/07/2018 | 30/07/2018 | 23/07/2018 | 2018_IFRC_20180813  | State       | West Kordofan |         |         |            | missing people             | 3               |                |
| 2018 | 23/07/2018 | 30/07/2018 | 23/07/2018 | 2018_IFRC_20180813  | State       | West Kordofan |         |         |            | Injured                    | 49              |                |
| 2018 | 23/07/2018 | 30/07/2018 | 23/07/2018 | 2018_IFRC_20180813  | State       | West Kordofan |         |         |            | livestock deaths           | 121             |                |
| 2018 | 23/07/2018 | 30/07/2018 | 23/07/2018 | 2018_IFRC_20180813  | State       | West Kordofan |         |         |            | water infrastructure_damage| 3               |                |
```

:::

::::{grid} 1
:::{card} 
#### SUDAN FLOOD RESPONSE HUMANITARIAN PARTNERS UPDATE BY STATE #3 (as of 19 Oct, 2020)

The map on the first page shows affecte population per state. This information can be extracted.

```{figure} /fig/UN_OCH_MAP_2021.png
---
width: 600px
name: 
align: center
---
```

```{dropdown} Data extracted from dataset

| Year | Start_Date | End_Date | Date         | source_ID          | admin_level | admin_1    | admin_2 | admin_3 | admin_camp | Impact type | Impact_quantity | Impact quality |
|------|------------|----------|--------------|--------------------|-------------|------------|---------|---------|-------------|-------------|-----------------|----------------|
| 2020 | 07/2020    | 09/2020  | 2020 OCHA 20201025 | State  | Northern    |          |         |          |  | pop_affected | 125660  |      |          
| 2020 | 07/2020    | 09/2020  | 2020 OCHA 20201025 | State  | River Nile  |          |         |           | | pop_affected | 33225   |                |
| ...  | ...        | ...      | ...          | ...                | ...         | ...        | ...     | ...     | ...         | ...         | ...             |            
```
:::

::::{grid} 1
:::{card} 
#### Humanitarian Bulletin Sudan Issue 35 | 22 - 28 August 2016

```{figure} /fig/2016_OCHA_20160828_snapshot.png
---
width: 600px
name: 
align: center
---
```


```{dropdown} Data extracted from dataset
| Year | Start_Date | End_Date | Date         | source_ID          | admin_level | admin_1        | admin_2 | admin_3 | admin_camp | Impact type | Impact_quantity | Impact quality |
|------|------------|----------|--------------|--------------------|-------------|----------------|---------|---------|-------------|-------------|-----------------|----------------|
| 2016 | 06/2016    | 09/2016  | 2016 OCHA 20160828 | State  | Kassala        |          |         |            | |affected    | |yes       |                 |
| 2016 | 06/2016    | 09/2016  | 2016 OCHA 20160828 | State  | South Darfur   |          |         |            | |affected    | |yes       |                 |
| 2016 | 06/2016    | 09/2016  | 2016 OCHA 20160828 | State  | Al Gezira      |          |         |            || affected    || yes       |                 |
| 2016 | 06/2016    | 09/2016  | 2016 OCHA 20160828 | State  | Sennar         |          |         |            | |affected    | |yes       |                 |
| ...  | ...        | ...      | ...          | ...                | ...         | ...        | ...     | ...     | ...         | ...         | ...             | ...            |

```
:::

::::{grid} 1
:::{card} 

#### Sudan Floods Countinue (FloodList)

The quote below is just one bit of relevant information from the flood list article. 
```{figure} /fig/2013_Floodlist_20130816_snapshot.png
---
width: 800px
name: 
align: center
---
```

```{dropdown} Data extracted from dataset
| Year | Start_Date  | End_Date  | Date        | source_ID             | admin_level | admin_1        | admin_2 | admin_3 | admin_camp | Impact type          | Impact_quantity | Impact quality |
|------|-------------|-----------|-------------|-----------------------|-------------|----------------|---------|---------|-------------|----------------------|-----------------|----------------|
| 2013 | 01/08/2013  | 21/08/21  | 11/08/2013 | 2013 Floodlist 201308 | Camp        | South Darfur   | Bellel  |         | Kalma Camp  | deaths               | 14              |                |
| 2014 | 01/08/2014  | 21/08/22  | 11/08/2014 | 2014 Floodlist 201308 | Camp        | South Darfur   | Bellel  |         | Kalma Camp  | houses_damaged_totaly| 874             |                |
```
:::

```{figure} /fig/20240216_Sudan_HIA_data_compiling.drawio.png
---
width: 1000px
name: 
align: center
---
```
