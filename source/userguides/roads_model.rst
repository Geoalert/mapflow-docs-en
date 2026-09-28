.. meta::
   :description: Extract road networks from 0.3-0.5 m satellite imagery. Multi-task learning improves mask connectivity where roads are obscured by trees or buildings.

.. rst-class:: mf-page

Roads
=====

.. mf-model-hero:: roads

How it works
------------

The model is trained mostly on rural and suburban areas. Multi-task learning keeps the road mask
connected where trees or buildings hide the road. It can fail in cities with wide roads,
sidewalks and complex crossings.

The model extracts road centrelines to reduce clutter, cleans the network, then inflates the
lines back into road polygons. Since version 1.1 the road graph is post-processed:

* geometry simplification;
* merging of gaps;
* removal of double edges;
* removal of detached and too short segments.

Sample results
--------------

.. container:: mf-figures

   .. figure:: _static/processing_result/roads_model_india.jpg
      :alt: Roads model result in a complex urban environment
      :class: no-scaled-link

      Complex urban environment: New Town, Kolkata Metropolitan Area, India

.. mf-cta::
