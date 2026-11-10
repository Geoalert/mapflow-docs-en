.. meta::
   :description: Detects swimming pools from aerial imagery. Useful for urban planning and real estate analysis. Requires high-resolution aerial or satellite imagery. Note, detection accuracy may vary depending on geographic location, test before large-scale use.

.. rst-class:: mf-page

Swimming pools
==============

.. mf-model-hero:: swimming-pools

How it works
------------

The model combines detection and classification: it finds swimming pools and assigns each
pool a class. It returns pool polygons with the class as an attribute, with a test score
above F1 0.95. It needs high-resolution imagery, ideally aerial imagery at zoom 19–20.

Use it for urban planning and real estate analysis, for example to keep property records
up to date. Accuracy can vary by region, so test the model on a small area before
you run it at scale.

Sample results
--------------

.. container:: mf-figures

   .. figure:: _static/processing_result/custom_models/swmp_arizona.jpg
      :alt: Swimming pools detected and classified
      :class: no-scaled-link

      Pools detected and classified on aerial imagery

.. mf-cta::
