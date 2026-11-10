.. meta::
   :description: Detects solar panels from aerial imagery. Useful for monitoring solar energy installations and urban planning. Requires high-resolution aerial imagery for accurate detection.

.. rst-class:: mf-page

Solar panels
============

.. mf-model-hero:: solar-panels

How it works
------------

The model combines detection and segmentation to find photovoltaic panels on rooftops and
in solar farms and outline them as polygons. It is trained on aerial imagery and needs
high-resolution aerial imagery at zoom 19–21 for accurate detection. The test score is
a pixel-wise F1 above 0.77.

Use it to monitor solar energy installations and for urban planning.

.. mf-cta::
