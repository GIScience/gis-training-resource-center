# Spatial Network Analysis Theory


## Understanding Networks: Analysis and Insights
Networks serve as simplified representations of real-world systems. A network comprises nodes and edges, representing entities and their relationships respectively. Rather than being defined by coordinates, positions within a network are determined by connectivity. In GIS (Geographic Information Systems), networks play integral roles in transportation modeling and supply chain networks such as water and energy distribution. Additionally, they are utilized for analyzing the service areas of healthcare facilities. For instance, analyses can assess areas vulnerable to flooding to ascertain the potential impact on healthcare services during a disaster.

### Components of a Graph
Creating a graph involves defining its nodes (vertices) and edges (connections between nodes). 
 
**Defining Nodes:** entities, objects, locations **&rarr;** Features in OpenStreetMap (hospitals, schools etc.)

**Identifying Edges:** roads or pathways between locations **&rarr;** Ways in OpenStreetMap (roads, paths, cicleways)

**Additional Information**
Edges can be endowed with diverse weights. OpenStreetMap features tags such as road type, segment length, speed limit, and surface condition, which can be interpreted as weight attributes. Depending on your requirements, you  can compute the shortest route or opt for the route with minimal elevation gain.

 ```{figure} /fig/graph_creation.png
---
width: 700px
name: basic classification
align: center
---
```
### Dijkstra Algorithm
- E. W. Dijkstra
- Discovered 1956, published 1959
- Single pair shortest path algorithm (SPSP) - for directions / A → B routing
- Single source shortest path algorithm (SSSP) - for isochrones
- Base of a multitude of routing algorithms

 ```{figure} /fig/Gif_dijkstra.gif
---
width: 700px
name: basic classification
align: center
---
```

### Analysis
You can determine directions or standard routes, which unveil the shortest path between two points. Isochrones offer insight into the area accessible within a specified time or distance threshold. Additionally, generating a matrix enables the assessment of time or distance between predefined locations. Alternatively, graphs facilitate travel optimization by computing the most efficient sequence for visiting a given set of points.


### OpenRouteService

#### General Information
- Graphhopper based routing machine since 2008
- Completly Open-Source
- Global public API
  - Updates every week
  - more than 100GB RAM per routing profile
    >Some limitations due to computational capacities
- Can also run on your local laptop
  - A small to medium country with one profile
  - Freedom of choice on limitations
- Different routing profiles (car, hgv, bike, pedestrian, wheelchair)

#### Services
- **Directions/standard routing**: Shortest path between two locations
- **Isochrones**: Area reachable within a limit (time | distance)
- **Matrix**: Times / Distances bewteen a set of locations
- **Optimization**: Best order to visit a set of points

>This module provides an accessibility analysis based on OpenRouteService isochrones.

#### Isochrones
- Different profiles: car, pedestrian, Bike, Heavy Goods vehicles
- Avoid areas, avoid, road types
- Further dynmaic prefernces
  - Green routing
  - Noise aware routing
  - Landmark routing
  - (heat aware routing)
- Based on profile and preferences what area is reachable within a given time limit?
- Determine
  - Reachability
  - Catchment areas
-  Max. 60minutes on the public API
-  SDKs & Plugins: Python, R, JavaScript, QGIS Plugin "ORS Tools"
  

