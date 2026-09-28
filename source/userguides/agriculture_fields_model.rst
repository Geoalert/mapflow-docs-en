.. meta::
   :description: Segment agricultural fields and delineate field boundaries from 1-1.2 m satellite imagery. Trained for Europe and Russia; available as a custom model.

.. rst-class:: mf-page

Agriculture fields
==================

.. mf-model-hero:: agriculture-fields

.. note::
   This model is no longer a default model. It is available on request.

How it works
------------

The model detects agricultural fields and separates neighbouring fields where there is a visible
boundary: a forest line, a road or a different crop stage. It is trained on 1–1.2 m imagery,
mostly of Europe and Russia, and works best on larger fields with active vegetation.
Small and terraced fields, typical for Asia, are delineated less well. Fields without vegetation,
especially in winter, are not the target class.

Sample results
--------------

.. container:: mf-figures

   .. figure:: _static/processing_result/agriculture_fields_5.jpg
      :alt: Agriculture fields result in Belgium
      :class: no-scaled-link

      Europe (Belgium)

   .. figure:: _static/processing_result/agriculture_fields_11.jpg
      :alt: Agriculture fields result in Northern India
      :class: no-scaled-link

      Asia (Northern India)

.. mf-cta::
