::::{admonition} French Translation 
:class: tip

The french version of this page can be found [here](/content/GIS_AA/fr_AILAS_madagascar_section_O.md).

La version française de cet article se trouve [ici](/content/GIS_AA/fr_AILAS_madagascar_section_O.md).

# Picture upload and management: AILAS Project

This documentation provides instructions on how to upload and manage street-level images that are captured in the framework of the AILAS project.

## Background: Panoramax

All pictures captured in the framework of the AILAS project are expected to be uploaded to a private instance of the street-level imagery platform Panoramax. This ensures that the imagery is easily available to the concerned stakeholders for the further usage in the project (labelling of training data, modelling), while being protected against access from unauthorized users.

### What is Panoramax?

[Panoramax](https://panoramax.fr) is an open, federated platform for sharing and viewing street-level imagery. Like [Google Street View](https://www.google.com/streetview/) and [Mapillary](https://www.mapillary.com), it allows users to explore places through photos taken along streets and paths. But unlike commercial platforms, Panoramax is built as a **decentralized and open ecosystem**: imagery is hosted on independent servers (run by institutions, cities, or communities) rather than a single company, and access is governed by open standards. The entire stack of Panoramax software is open source.

This means that data ownership stays with the contributors and hosting institutions, and imagery can be more easily integrated into local projects, research, or public services. Panoramax emphasizes **openness, transparency, and sovereignty** of street-level data.

### Features

#### 🌍 Core Features

* **Street-level imagery viewer** – explore panoramic or directional images along roads, paths, and places.
* **Open & federated hosting** – imagery is stored on independent servers operated by different organizations (municipalities, research centers, NGOs, etc.).
* **Open standards (STAC, OGC)** – ensures interoperability with mapping platforms, GIS tools, and data portals.
* **Contributions from multiple sources** – imagery can come from institutions, community projects, or individuals.
* **Integration into mapping workflows** – imagery can be linked with OpenStreetMap or other geospatial datasets.

#### 🔍 Privacy & Processing

* **Automatic face and license plate blurring** – built-in anonymization before imagery is published.
* **Object detections** – AI models can detect relevant features (e.g., traffic signs) within the imagery.
* **Custom detection models** – operators can run their own detection pipelines for specific use cases.
* **Metadata enrichment** – detected objects can be stored as data linked to the images, making the imagery searchable and analyzable.

#### ⚙️ Platform & Ecosystem

* **API access** – developers can query and use imagery programmatically.
* **Web-based viewer** – lightweight, embeddable viewer for public portals or project websites.
* **Community-driven** – open-source software stack, enabling transparency and extensibility.
* **Long-term data ownership** – institutions keep control over where and how their imagery is stored and shared.

### Data privacy and security

Panoramax prevents the identification of people in the imagery by blurring faces and license plates. This happens automatically on image upload and before the images are published. User can report any further issues with an image through the platform. This will cause the image to be hidden from public view until intervention from the owner of the image.

While one of the main features of Panoramax is its global public meta-catalogue that makes images from all federated instances findable, we deliberately choose not to join the federation with the Panoramax instance of the AILAS project. This means that images uploaded to our instance cannot be accessed through the global API.

The API of the AILAS Panoramax instance runs on a server that is only accessible from within our own network. Images and derivates are stored in a private MinIO bucket. Access to the website that allows upload and visual exploration of the collected imagery is password protected. 

## Picture upload

## Picture management

### Explore

###  