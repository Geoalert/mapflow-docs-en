The core of the Mapflow are the Mapping Models. Mapflow enables to detect and extract features in satellite and aerial images powered by semantic segmentation and other deep learning techniques. 

Mapping Models
==============

|:house:| **Buildings** 
Extracting of roofprints of buildings from imagery of high resolution

Additional options:

* **Classification by types of buildings** – typology of buildings is represented by the main classes (see `reference <https://mapflow.ai>`_)

* **Building heights**
Building height estimation by the length of the shadow and the visible part of the wall.
Shift to the building footprint

|:christmas_tree:| **Forest** 
Extracting the forest masks from RGB images of high resolution (2 meters) without classification by type, density and heights

Additional options:

* **Classification by heights** – classification the areas of vegetation and shrub vegetation by height classes according to the specified thresholds: by default 0-4 m, 4-10 m, 10+ m. Forest areas of each height class are polygonized in separate features, the height class is indicated in its properties

* **Classification by overgrowth density** – classification of the area of vegetations and shrub vegetation into classes according to the density and height: high forest, low (growing) forest, open woodland, shrub.

|:red_car:| **Roads** 
Extracting the road mask from satellite images of high spatial resolution

Additional options:

* Classification by road pavement
* Transfomation into graph


|:building_construction:| **Construction** 
Detection of the construction sites by classification of tiles of hi-resolution satellite images


Models reference
================


Buildings
"""""""""

   .. tabularcolumns:: |p{2cm}|p{5cm}|p{3cm}|

   .. csv-table::
      :file: _static/csv/buildings.csv 
      :header-rows: 1 
      :class: longtable
      :widths: 1 1 1


Forest
""""""

   .. tabularcolumns:: |p{2cm}|p{3cm}|p{3cm}|

   .. csv-table::
      :file: _static/csv/forest.csv 
      :header-rows: 1 
      :class: longtable
      :widths: 1 1 1


Roads
"""""

   .. tabularcolumns:: |p{5cm}|p{7cm}|p{7cm}|

   .. csv-table::
      :file: _static/csv/roads.csv 
      :header-rows: 1 
      :class: longtable
      :widths: 1 1 1


