🏘 High-density housing (Mapflow Web)
-------------------------------------------

Our “high-density housing” AI model is designed for areas with terraced or otherwise densely built buildings, common in the Middle East, parts of Africa, etc. This model, just like the regular building model, detects the building roofs.

Firstly, the building blocks are segmented as a whole, and then each block is divided into individual houses with rectangular grid or Voronoi diagram, based on the detected individual roof markers.

**Processing results samples**

Processing result sample for dense urban development area (Tunisia, Africa):

.. figure:: _static/processing_result/high-density_housing_1.jpg
   :alt: Processing result of high-density housing model
   :align: center
   :width: 15cm
   :class: with-border no-scaled-link
   
   Standard model for buildings segmentation, with polygon simplification
.. figure:: _static/processing_result/high-density_housing_2.jpg
   :alt: Processing result of high-density housing model
   :align: center
   :width: 15cm
   :class: with-border no-scaled-link
   
   High density buildings model