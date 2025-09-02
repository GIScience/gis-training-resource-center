# Picture upload and management: AILAS Project

This documentation provides instructions on how to upload and manage street-level images that are captured in the framework of the AILAS project.

## Background: Panoramax

<!-- Screenshot Panoramax -->

```{figure} /fig/AILAS_screenshot_panoramax.png
---
name: Screenshot Panoramax
width: 400px
---
Screenshot of a street level image displayed on Panoramax
```

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

The API of the AILAS Panoramax instance runs on a server that is only accessible from within our own network. Images and derivates are stored in a private MinIO bucket. The website and the API that allow access to the images and the data currently run on a closed network.

## Picture upload
🚧 The process described here is a temporary solution and due to change. 🚧

### 1. Remove the SD card from the camera.

::::{grid} 2
:::{grid-item}

```{figure} /fig/AILAS_slide_lid.jpg
---
name: Slide lid
width: 375 px
---
Slide open the lid 
```

:::

:::{grid-item}

```{figure} /fig/AILAS_push_card.jpg
---
name: push card
width: 375 px
---
Gently push the SD card to remove it
```

:::
::::

### 2. Insert into card reader and connect to computer.

```{figure} /fig/AILAS_insert_card.jpg
---
name: insert card
width: 400 px
---
Insert the SD card into the card reader
```

With the SD card inserted, connect the card reader to a computer.

### 3. Sign in to upload bucket

```{figure} /fig/AILAS_bucket_login.png
---
name: login bucket
width: 400 px
---
Sign in to upload bucket
```

Open the [upload bucket](https://warm.storage.heigit.org/ui/browser/heigit-hum-panoramax-temp) in your browser and log in with the credentials provided to you.

### 4. Upload images

1. Choose the correct upload folder. The folder name should correspond to the label on your camera. Click the folder to open it.

```{figure} /fig/AILAS_choose_upload_folder.png
---
name: upload folder
width: 400 px
---
Open the correct one of the available upload folders.
```

```{figure} /fig/AILAS_camera_label.jpg
---
name: camera name
width: 400 px
---
The folder name should correspond to the label on your camera.
```

2. Click the upload button in the top right and select "Upload file".

```{figure} /fig/AILAS_upload_button.png
---
name: upload button
width: 400 px
---
Click the upload button and select "Upload file"
```
3.  A file browser will open. Select and open all the images on the SD card in the folder `/DCIM/100GOPRO`.

:::{admonition} Dealing with multiple image folders
:class: tip
If you captured more than a thousand images, the images are saved in several subfolders of `DCIM` called `100GOPRO`, `101GOPRO`, etc. Repeat steps 2 to 4 of this section for all the subfolders.
:::

```{figure} /fig/AILAS_select_files.png
---
name: select files
width: 400 px
---
Select the image files
```
4. Wait until the upload status of all image files is at 100 %. Scroll down the upload status menu to verify.

```{figure} /fig/AILAS_upload_completed.png
---
name: upload completed
width: 400 px
---
Wait until the upload of all files is completed
```

### 5. Delete images

Once you have successfully uploaded the images, delete them from the SD card.

### 6. Re-insert sd card into camera

Safely remove the SD card reader from your computer, and re-insert the card into the camera.

## Picture exploration on Panoramax
🚧 Information will follow. 🚧