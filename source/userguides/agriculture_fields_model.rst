|:tractor:| Agriculture fields (DEPRECATED)
--------------------------------------------

.. warning::
   This model has been deprecated as default one. it's available only by request.

Model for fields segmentation allows to detect the agricultural fields and delineate the nearby fields from each other, if there is a visual boundary (forest line, road, different crop stage). The model is trained on the high resolution data (1-1.2 m), primarily for Europe, Russia. It performs better with larger fields with active vegetation. Smaller and terrace fields (typical for Asia) are delineated not so good. Fields without vegetation, especially in winter period, are not target class.


.. figure:: _static/processing_result/agriculture_fields_5.jpg
   :alt: Processing result of agriculture fields model
   :align: center
   :width: 15cm
   :class: with-border no-scaled-link
   
   Processing result sample for Europe (Belgium)

.. figure:: _static/processing_result/agriculture_fields_11.jpg
   :alt: Processing result of agriculture fields model
   :align: center
   :width: 15cm
   :class: with-border no-scaled-link
   
   Processing result sample for Asia (Northern India)