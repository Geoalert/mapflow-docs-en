Agriculture fields
===================

Model for fields segmentation allows to detect the agricultural fields and delineate the nearby fields from each other, if there is a visual boundary (forest line, road, different crop stage). The model is trained on the high resolution data (1-1.2 m), primarily for Europe, Russia. It performs better with larger fields with active vegetation. Smaller and terrace fields (typical for Asia) are delineated not so good. Fields without vegetation, especially in winter period, are not target class.

**Processing results samples**

.. figure:: ../_static/processing_result/agriculture_fields_5.png
   :alt: Processing result of agriculture fields model
   :align: center
   :width: 18cm
   
   Processing result sample for Europe (Belgium)

.. figure:: ../_static/processing_result/agriculture_fields_11.png
   :alt: Processing result of agriculture fields model
   :align: center
   :width: 18cm 
   
   Processing result sample for Asia (Northern India)