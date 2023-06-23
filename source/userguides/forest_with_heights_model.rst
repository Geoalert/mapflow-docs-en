🌲↕️ Forest with heights (Mapflow API/QGIS only)
-------------------------------------------------

This model is not available in Mapflow Web. Use `Mapflow QGIS` or API to get access to forest height estimation.

Forest Segmentation follows the usual forest segmentation model, with additional separation of forest height classes.
Additionally we use models for density and height estimation, dividing the forested area into the following classes:

* Shrubs lower than 4 meters;
* Forest from 4 to 10 meters high;
* Forest more than 10 meters high;

This model can be used as a decision support for the forest growth clearing.

This postprocessing is available for processings 50 sq.km and more.

**Processing results samples**

.. figure:: _static/processing_result/forest_model_2.png
   :alt: Processing result of forest model
   :align: center
   :width: 18cm
   
   Processing results for central Russia (Tatarstan)