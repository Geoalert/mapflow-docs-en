.. meta::
   :description: Segment agricultural fields and delineate field boundaries from 1-1.2 m satellite imagery. Trained for Europe and Russia; available as a custom model. Note: current model coverage is limited to specific geographic regions, test before taking it onto a large scale. Primary use cases: precision agriculture, crop fields delineation, land use analysis.

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
mostly of Eastern Europe, and works best on larger fields with active vegetation.
Small and terraced fields, typical for Asia, are delineated less well. Fields without vegetation,
especially in winter, are not the target class.

Use it for precision agriculture, crop field delineation and land use analysis. Coverage is
limited to specific regions, so test the model on a small area before you run it at scale.

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
