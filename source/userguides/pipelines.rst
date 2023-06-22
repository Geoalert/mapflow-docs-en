The core of the Mapflow are the Mapping Models. Mapflow enables to detect and extract features in satellite and aerial images powered by semantic segmentation and other deep learning techniques. 
See :doc:`requirements <requirements>` page to better understand what data to use with each model,
and :doc:`price list <prices>` for breakdown of the processings billing.

AI-Mapping Models
=================


|:cityscape:| :doc:`Buildings <models_changelog/buildings_model>`

Extracting of roofprints of buildings from imagery of high resolution.

Additional options:

* *Classification by types of buildings* – typology of buildings is represented by the main classes (see :doc:`reference <../um/classes>`).

* *Building heights* - building height estimation by the length of the shadow and the visible part of the wall. Shift to the building footprint.

* *Simplification* - The algorithm allows you to correct the irregularities of the contours of our model.

* *Merge with OSM* - This option allows you to replace the obtained data of our model with data from the OSM, if the polygons of the OSM buildings and the model overlap significantly (Jaccard coefficients - more than 0.7).

|:houses:| :doc:`High-density housing <models_changelog/hd_housing_model>`

Our "high-density housing" AI model is designed for areas with terraced or otherwise densely built buildings, common in the Middle East, parts of Africa, etc.

|:house:| :doc:`Buildings (Aerial imagery) <models_changelog/buildings_aerial_imagery_model>`

This model designed to detect not only big buildings, but also small buildings like garages and sheds in very high resolution aerial data.

|:evergreen_tree:| :doc:`Forest <models_changelog/forest_model>`

Extracting the forest masks from RGB images of high resolution (2 meters) without classification by type, density and heights.

|:evergreen_tree:| |:arrow_up_down:| :doc:`Forest with heights [Mapflow API/QGIS only] <models_changelog/forest_with_heights_model>`

Classification the areas of vegetation and shrub vegetation by height classes according to the specified thresholds:
0-4 m, 4-10 m, 10+ m. Forest areas of each height class are polygonized in separate features.
The height class is specified in the polygon property `class_id`.

|:red_car:| :doc:`Roads <models_changelog/roads_model>`

Extracting the road mask from satellite images of high spatial resolution.

|:building_construction:| :doc:`Construction <models_changelog/construction_model>`

Detection of the construction sites by classification of tiles of hi-resolution satellite images.

|:tractor:| :doc:`Agriculture fields <models_changelog/agriculture_fields_model>`

Extraction and instance separation of agriculture fileds from high-resolution satellite imagery.
