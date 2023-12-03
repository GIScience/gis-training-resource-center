# Automatistation in QGIS

## What is the need for Automatisation?
Automation streamlines tasks by reducing the user effort and minimizing errors through less manual repetition. It allows for modularization, enhances reusability and reduces redundancy by repaatedly using a defined set of needed tools. In QGIS in can be achieved by using the "Model Designer".

## The QGIS Model Designer
The Model Designer is a visual tool that allows users to create and edit a workflow with all tools available in QGIS that can be used repeatedly in a simple and time-efficient manner. It provides a graphical interface to build workflows by connecting geoprocessing tools and algorithms. The user can define inputs, outputs, and the flow of data between different processing steps.

### Using the Model Designer/Graphical Modeler

Open the tool under `Processing` -> `Graphical Modeler`

Give the model file a name and save it on you Computer.

You can also open a existing model via `Model` -> `Open Model` and navigating to the model file


**VIDEO**

### Model Components
**Inputs/Outputs**: The model starts with input data and produces output filesi
**Algorithms**: Algorithms or Tools are specific geoprocessing steps that perform specific tasks, such as clipping, reprojecting or buffering.


### Create and save model

**Add Inputs**
You can add Spaces for input files via the "Inputs" Window on the left. Expand "Parameters" and choose the kind of Input type you need. For example "Vector Layer" for a layer with administrative districts or "CRS" for a coordinate refernece system that is needed for multiple reprojections in the model.

Addition if inputs is possible by double clicking or via drag and drop.

**VIDEO**


**Add Processing Steps:**
In the "Algorithms" panel on the left hand side you can choose procesing steps out of the QGIS toolbox. For example the "buffer" tool for buffering all administrative distrits of a input layer by 5 km.

Addition of algorithms is possible double clicking or via "drag and drop".

**VIDEO**


**Run the Model**
To run the model click the green arrow in the top bar and enter your inputs in the apperaing console and click "Run". Output layers are automatically added to you QGIS project interface.

**Export the Model**
Models can be exported as an image (e.g. in png format), PDF, SVG and as a Python Script. Exporting the model can be benefical for documenting your work steps or to intergrate it in a Python based workflow.

Export the model via Model > Export > Export as Image/PDF/SVG Python Script

**VIDEO**