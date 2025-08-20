🚧This part of training platform is under ⚠️construction⚠️ and may not be shared or published! 🚧

# AI Logistic Awareness System (AILAS) Street View image collection Field Experiments
This documentation aims to consolidate all information regarding the Street View image collection field experiments for AILAS and give a consise overview over the AILAS project. It focuses on the process of collecting Street View images and is intended for use by participants in the experiments as a practical guideline.

## The AILAS Project
AILAS is a planned, weather-adaptive routing service that helps people to plan trips on unpaved roads by showing which road segments are currently passable. It combines fresh street-level images with rainfall, soil moisture, terrain and other openly available geodata, and then delivers practical route suggestions through the openrouteservice (ORS) platform. The goal is to reduce delays and risks in humanitarian operations and other logistics, especially in regions like Madagascar where many roads are unpaved. 

:::{admonition} Technical details
:class: note
To develop the system dashcams on CRM vehicles capture geotagged street-level images along planned routes. All images are uploaded a cloud storage (Panoramax), where faces/plates are blurred and standard preprocessing prepares the data for analysis.  Each image is time-stamped and linked to its OpenStreetMap road segment and then classified into different passability classes (e.g. bad passability/ medium passabilty). The classified images will be used as training data fort he development of a deep learning model, whose task will be to automatically classify passability of street level images after training. These classifications are combined with dynamic weather data and further secondary data (e.g. terrain or soil classes) to develop a model that is able to estimate passability based on current weather data/forecasts.  Finally, the results are integrated into openrouteservice to account for the passability of unpaved roads when generating routes.

```{figure} /fig/AILAS_workflow.png
---
name: AILAS workflow
width: 600px
---
Technical workflow of the AILAS project
```
:::

## In Field Acquisition of Street Level Imagery
Collecting good street-level images is essential for AILAS, because the deep learning model for road passability classification needs clear, georeferenced pictures of road conditions under different weather to learn and improve to recognize road surface properties and assign a plausible passability (See figure XX). For this, dashcams mounted on CRM vehicles record along planned routes; where helpful, openly licensed images from Mapillary can extend coverage. All images are uploaded to a Panoramax server, where privacy-preserving blurring and standard preprocessing prepare them for analysis. Reliable capture, sufficient image quality, and robust upload over unstable connections are the main practical challenges we will test in the field. 

```{figure} /fig/AILAS_model_demo.png
---
name: QR Code
width: 600px
---
Conceptual depiction of road surface properties the deep learning model could detect to accurately classify road passability
```

## Experiment Goal
This first test run in Madagascar aims to gain hands-on experience with camera handling, image quality, GPS accuracy, and the stability of the upload pipeline—then collect structured feedback from CRM teams on what works and what needs to change. We will also start building a local image base (repeated passes of the same tracks in different weather) that can be used later to train and validate the AILAS model. A secondary goal is to document a simple end-to-end workflow—from mounting the camera, driving and recording, to uploading to Panoramax and confirming that images appear correctly—so future teams can follow the same steps. The insights from this test will shape equipment choices, data volume expectations, and standard operating procedures for larger deployments and provide a first data set to develop the planned deep learning model.





## Panoramax

### What is Panoramax?
Introduction to the Panoramax platform and its role in the project (image storage, processing, etc.).


### Panoramax Features
Key features of Panoramax that are relevant for the project (e.g., image organization, access controls, and analytics).

### Data Security
Information on how Panoramax ensures the security of the collected data.





