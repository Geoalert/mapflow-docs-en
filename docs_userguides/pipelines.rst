The core of the Mapflow are the Mapping Models. Mapflow enables to detect and extract features in satellite and aerial images powered by semantic segmentation and other deep learning techniques. 

AI-Mapping Models
=================

|:house:| **Buildings** 

Extracting of roofprints of buildings from imagery of high resolution.

Additional options:

* *Classification by types of buildings* – typology of buildings is represented by the main classes (see `reference <https://docs.mapflow.ai/docs_um/classes.html>`_).

* *Building heights* - building height estimation by the length of the shadow and the visible part of the wall. Shift to the building footprint.

* *Simplification* - The algorithm allows you to correct the irregularities of the contours of our model.

* *Merge with OSM* - This option allows you to replace the obtained data of our model with data from the OSM, if the polygons of the OSM buildings and the model overlap significantly (Jaccard coefficients - more than 0.7).

|:cityscape:| **High-density housing**

Our "high-density housing" AI model is designed for areas with terraced or otherwise densely built buildings, common in the Middle East, parts of Africa, etc.

|:christmas_tree:| **Forest** 

Extracting the forest masks from RGB images of high resolution (2 meters) without classification by type, density and heights.

Additional options:

* *Classification by heights* – classification the areas of vegetation and shrub vegetation by height classes according to the specified thresholds: 0-4 m, 4-10 m, 10+ m, and division of classes in 4+ m according to the density of vegetation into: dense and sparse. Forest areas of each height class are polygonized in separate features. The height class and density of vegetation are specified in the polygon properties.

|:red_car:| **Roads** 

Extracting the road mask from satellite images of high spatial resolution.

|:building_construction:| **Construction** 

Detection of the construction sites by classification of tiles of hi-resolution satellite images.


Models reference
================


Buildings
"""""""""

.. list-table::
   :widths: 10 40 10 10
   :header-rows: 1

   * - Model
     - Description
     - Model input, GSD m/px
     - Model input, zoom
   * - Segmentation
     - Extract roof contours (roofprints) from high-resolution satellite imagery
     - RGB 0.5
     - 18
   * - Classification
     - Here are the types that we currently recognize: apartment buildings; single-household dwellings; industrial; commercial; other non-residential
     - RGB 0.5
     - 18
   * - Building heights
     - For each building, model estimates its height using its wall’s and shadow’s lengths. If height detection option is selected, all roof contours are shifted accordingly, i.e. converted to building footprints
     - RGB 0.5
     - 18


Forest
""""""

.. list-table::
   :widths: 10 40 10 10
   :header-rows: 1

   * - Model
     - Description
     - Model input, GSD m/px
     - Model input, zoom
   * - Segmentation
     - Extract segmentation masks of forested areas from high-resolution RGB images
     - RGB, 2
     - 16
   * - Classification
     - Classify the areas of vegetation and shrub vegetation by height and vegetation density
     - RGB, 0.5
     - 18


Roads
"""""

.. list-table::
   :widths: 10 40 10 10
   :header-rows: 1

   * - Model
     - Description
     - Model input, GSD m/px
     - Model input, zoom
   * - Segmentation
     - Extract road mask from high-resolution satellite imagery
     - RGB, 1
     - 17



High-density housing
"""""""""""""""""""""

.. list-table::
   :widths: 10 40 10 10
   :header-rows: 1
     
   * - Model
     - Description
     - Model input, GSD m/px
     - Model input, zoom
   * - Segmentation
     - Extraction and instance detection of the building roofprints in the areas of high density housing
     - RGB 0.5
     - 18
   * - Building heights
     - For each building instance, model predicts its height. If height detection option is selected, all roof contours are shifted accordingly, i.e. converted to building footprints
     - RGB 0.5
     - 18
