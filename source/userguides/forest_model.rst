🌲 Forest and trees
----------------------

Forest Segmentation. The model is trained on high-resolution data (0.6 m) for different areas and climate zones.

The result includes all areas covered with tree and shrub vegetation, including sparse forest and shrublands.

Model resolution allows to detect small group of trees and narrow tree lines.

The model is robust to region change, and performs well in most environments, including urban. The image should be taken in active vegetation period, because leafless trees or vegetation covered with snow are not target class.


.. hint::
   This model can be used to speed up trees detection and area estimation in forest inventory assessment.


.. figure:: _static/processing_result/forest_model_3.jpg
   :alt: Processing result of forest model
   :align: center
   :width: 15cm
   :class: with-border no-scaled-link
   
   Sample of processing results for solid **Forest** mask

**Additional options:**

* *Height estimation* – forest mask classification by height classes
* *Tree crown polygons* - extracts tree crowns from forest vegetation as well as free-standing trees, provides them as polygons
* *Tree crown points* - extracts tree crowns from forest vegetation as well as free-standing trees, provides them as points

.. note::
   Forest Height classification follows the following classes:

   * Shrubs lower than 4 meters;
   * Forest from 4 to 10 meters high;
   * Forest more than 10 meters high;

   This classification is used as a decision support for the vagatation management in powerline zones, etc. See the `professional solutions by Geoalert <https://geoalert.io/solutions/power>`_. But the tresholds can be customized depending on the requirements.


**Processing results samples**

.. figure:: _static/processing_result/output-crowns.gif
   :alt: Processing result of forest model (Tree crowns, points)
   :align: center
   :width: 15cm
   :class: with-border
   
   Sample of results for **Tree crowns, points**


.. figure:: _static/processing_result/forest_w_heights_model.jpg
   :alt: Processing result of forest model (Heights)
   :align: center
   :width: 15cm
   :class: with-border no-scaled-link
   
   Sample of results for **Forest with heights** mask (raster output)