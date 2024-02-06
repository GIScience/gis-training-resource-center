# Spatial Network Analysis Theory


## Understanding Networks: Analysis and Insights
Networks serve as simplified representations of real-world systems. A network comprises nodes and edges, representing entities and their relationships respectively. Rather than being defined by coordinates, positions within a network are determined by connectivity. In GIS (Geographic Information Systems), networks play integral roles in transportation modeling and supply chain networks such as water and energy distribution. Additionally, they are utilized for analyzing the service areas of healthcare facilities. For instance, analyses can assess areas vulnerable to flooding to ascertain the potential impact on healthcare services during a disaster.


 Creating a graph involves defining its nodes (vertices) and edges (connections between nodes). 
 
 **Defining Nodes:** entities, objects, locations **&rarr;** Features in OpenStreetMap (hospitals, schools etc.)

 **Identifying Edges:** roads or pathways between locations **&rarr;** Ways in OpenStreetMap (roads, paths, cicleways)

 Edges can be endowed with diverse weights. OpenStreetMap features tags such as road type, segment length, speed limit, and surface condition, which can be interpreted as weight attributes. Depending on your requirements, you can compute the shortest route or opt for the route with minimal elevation gain.
 
  <div style="text-align:center;">
  <img src="/fig/Network.png" width="500" height="370">
  </div>

### Where Lies the Analysis?
You can determine directions or standard routes, which unveil the shortest path between two points. Isochrones offer insight into the area accessible within a specified time or distance threshold. Additionally, generating a matrix enables the assessment of time or distance between predefined locations. Alternatively, graphs facilitate travel optimization by computing the most efficient sequence for visiting a given set of points.


This module deals with isochrones and shows a network analysis in QGIS in two different ways.


bit stuff here:

https://gitlab.gistools.geog.uni-heidelberg.de/giscience/disaster-tools/gis-in-anticipatory-humanitarian-action/-/blob/main/0318_network.pdf
