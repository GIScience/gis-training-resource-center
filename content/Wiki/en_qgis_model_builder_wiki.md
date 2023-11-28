# The QGIS Model Designer
The Model Designer is a visual tool that allows users to create and edit a workflow with all tools available in QGIS that can be used repeatedly in a simple and time-efficient manner. It provides a graphical interface to build workflows by connecting geoprocessing tools and algorithms. The user can define inputs, outputs, and the flow of data between different processing steps.

### Using the Model Designer
Open the tool under "Processing > Model Designer".

Give the model file a name and save it on you Computer.

You can also open a existing model via "Model > Open Model" and navigating to the model file

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_modelbuilder_open.mp4"></video>

### Model Components
**Inputs/Outputs**: The model starts with input data and produces output filesi
**Algorithms**: Algorithms or Tools are specific geoprocessing steps that perform specific tasks, such as clipping, reprojecting or buffering.

### Create and save model
#### Add Inputs and Processing Steps
You can add Spaces for input files via the "Inputs" Window on the left. Expand "Parameters" and choose the kind of Input type you need. For example "Vector Layer" for a layer with administrative districts or "CRS" for a coordinate refernece system that is needed for multiple reprojections in the model.

Addition if inputs is possible by double clicking or via drag and drop.

#### Add Processing Steps:
In the "Algorithms" panel on the left hand side you can choose procesing steps out of the QGIS toolbox. For example the "buffer" tool for buffering all administrative distrits of a input layer by 5 km.

Addition of algorithms is possible double clicking or via "drag and drop".

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_modelbuilder_model.mp4"></video>

#### Run the Model
To run the model click the green arrow in the top bar and enter your inputs in the apperaing console and click "Run". Output layers are automatically added to you QGIS project interface.

**Export the Model**
Models can be exported as an image (e.g. in png format), PDF, SVG and as a Python Script. Exporting the model can be benefical for documenting your work steps or to intergrate it in a Python based workflow.

Export the model via Model > Export > Export as Image/PDF/SVG Python Script

<video width="100%" controls src="https://github.com/GIScience/gis-training-resource-center/raw/main/fig/qgis_modelbuilder_export.mp4"></video>
