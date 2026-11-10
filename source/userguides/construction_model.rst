.. meta::
   :description: Detects and outlines areas containing construction sites and buildings under construction from satellite imagery. Model identifies active construction activity including partially built structures and construction zones. Output is construction area polygons in GeoJSON format. Note: current model coverage is limited to specific geographic regions, test before taking it onto a large scale. Primary use cases: urban development monitoring, construction activity tracking, infrastructure project oversight, real estate development analysis.

.. rst-class:: mf-page

Constructions
=============

.. mf-model-hero:: constructions

How it works
------------

The model outlines areas with active construction: construction sites, partially built
structures and buildings under construction. It returns construction site polygons
that you can download as GeoJSON. It works best on 0.6–0.3 m satellite imagery (zoom 18)
of fast-developing areas.

Use it to monitor urban development, track construction activity, oversee infrastructure
projects and analyse real estate development. Coverage is limited to selected countries,
so test the model on a small area before you run it at scale.

Sample results
--------------

.. container:: mf-figures

   .. figure:: _static/processing_result/construction_model.jpg
      :alt: Construction sites detected in a fast-developing area
      :class: no-scaled-link

      A rapidly developing area with construction sites

.. mf-cta::
