🌲↕️ Forest with heights (API/QGIS)
-------------------------------------------------

This model is not available in Mapflow Web. Use `Mapflow QGIS` or API to get access to forest height estimation.

Forest Segmentation follows the usual forest segmentation model, with additional separation of forest height classes.
Additionally we use models for density and height estimation, dividing the forested area into the following classes:

* Shrubs lower than 4 meters;
* Forest from 4 to 10 meters high;
* Forest more than 10 meters high;

.. hint::
   This model can be used as a decision support for the forest growth clearing. See the `professional solutions by Geoalert <https://geoalert.io/solutions/power>`_


**Processing results samples**

.. figure:: _static/processing_result/forest_w_heights_model.jpg
   :alt: Processing result of forest model
   :align: center
   :width: 15cm
   :class: with-border no-scaled-link
   
   Sample of results for **Forest with heights** mask (raster output)