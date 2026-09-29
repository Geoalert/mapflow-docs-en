.. meta::
   :description: Detect building roofs in terraced and densely built areas typical of the Middle East and Africa. Available as a custom Mapflow model on request.

.. rst-class:: mf-page

High-density housing
====================

.. mf-model-hero:: high-density-housing

.. note::
   This model is no longer a default model. It is available on request.

How it works
------------

Like the regular Buildings model, this model detects building roofs. It first segments building
blocks as a whole, then tries to split each block into individual houses from roof markers,
with a rectangular grid or a Voronoi diagram.

Sample results
--------------

.. container:: mf-figures

   .. figure:: _static/processing_result/high-density_housing_2.jpg
      :alt: High-density housing result in Tunisia
      :class: no-scaled-link

      Dense urban development (Tunisia): instance segmentation and grid post-processing

.. mf-cta::
