Forest
=======

Forest Segmentation. The model is trained on high-resolution data (2m ) for central and boreal Russia in summer period.

The result includes all areas covered with tree and shrub vegetation, including sparse forest and shrublands. Model resolution does not allow it to detect individual trees and narrow tree lines, and draw a strict border for the forested areas, but suits well for building a general analytical map.

The model is robust to region change, and performs well not only for Russia, but also in other countries and continents. The image should be taken in active vegetation period, because leafless trees or vegetation covered with snow are not target class.
Postprocessing:

Additionally we use models for density and height estimation, dividing the forested area into the following classes:

* Shrubs lower than 4 meters high(sparse or dense);
* Forest from 4 to 10 meters high, sparse;
* Forest from 4 to 10 meters high, dense;
* Forest more than 10 meters high, sparse;
* Forest more than 10 meters high, dense.

This model can be used as a decision support for the forest growth clearing.

This postprocessing is available for processings 50 sq.km and more.

**Processing results samples**

.. figure:: ../_static/processing_result/forest_model_2.png
   :alt: Processing result of forest model
   :align: center
   :width: 18cm
   
   Processing results for central Russia (Tatarstan)