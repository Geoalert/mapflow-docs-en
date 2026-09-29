.. meta::
   :description: Extract building rooftops and footprints from high-resolution satellite and aerial imagery. Building types, simplification, OpenStreetMap merge and height estimation.

.. _Buildings model:

.. rst-class:: mf-page

Buildings
=========

.. mf-model-hero:: buildings

Scenarios with this model
-------------------------

Each scenario is the Buildings model with one option switched on.
Choose options in the run form of Mapflow Web or the QGIS plugin.

.. mf-scenario-cards:: buildings

.. _scenario-building-types:

Sort buildings by type
~~~~~~~~~~~~~~~~~~~~~~

.. mf-scenario:: building-types

The full list of types is in the :ref:`building classes reference <buildings_classes>`.

.. _scenario-building-heights:

Building heights and 3D footprints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mf-scenario:: building-heights

The model does not see footprints directly, because walls hide them in the image.
Like a cartographer, it moves the roof outline down to the bottom of the wall.

All options
-----------

.. rst-class:: mf-options

Building types
   Assigns every building one of the main classes (see :ref:`reference <buildings_classes>`). No extra cost.

Regularization
   Corrects irregular contours. Shapes are replaced with rectangles, circles or polygons with
   90° angles that fit the original shape. The result is more map-friendly, but some of the
   original mask accuracy can be lost.

Simplification
   Simplifies the building shape while staying close to the original mask, including curved and
   complex shapes. Fewer right angles than regularization.

Merge with OpenStreetMap
   Where OpenStreetMap coverage is good, each building that has a matching OSM object (Jaccard index)
   is replaced with the OSM polygon, and rotated to align with the nearest OSM road.
   The result is then no longer based on the image, so buildings can be shifted from their actual position.

Height estimation (beta)
   A regression model estimates height from visual cues such as shadow length and visible walls,
   and returns 3D footprints: the contour projected to ground level instead of the roof outline.
   Most useful on oblique imagery, where roofs appear shifted. +10 credits per km².

.. note::
   Buildings smaller than 20 m² are removed from the result to avoid clutter.

.. _buildings_benchmarks:

Benchmarks
----------

**Buildings v.2026-07-06** (Global, segmentation, 0.3 m / z19) was evaluated against manually
annotated ground truth. Metrics are area-based: IoU is the intersection-over-union of the predicted
and ground-truth building masks, and F1, precision and recall are computed on the overlapping mask area.

.. tab-set::

   .. tab-item:: Aerial imagery

      .. list-table::
         :widths: 24 14 12 14 14 14
         :header-rows: 1

         * - AOI (location)
           - Predicted features
           - IoU
           - F1
           - Precision
           - Recall
         * - United States — Fort Myers
           - 65
           - 0.907
           - **0.951**
           - 0.983
           - 0.921
         * - United States — Phoenix
           - 47
           - 0.903
           - **0.949**
           - 0.944
           - 0.953
         * - Canada — Rigaud
           - 103
           - 0.870
           - **0.930**
           - 0.934
           - 0.927
         * - Australia — Adelaide
           - 92
           - 0.868
           - **0.929**
           - 0.914
           - 0.945
         * - New Zealand — Lower Hutt
           - 106
           - 0.867
           - **0.929**
           - 0.956
           - 0.903
         * - New Zealand — Wellington
           - 76
           - 0.838
           - **0.912**
           - 0.900
           - 0.924
         * - United Kingdom — London
           - 68
           - 0.813
           - **0.897**
           - 0.873
           - 0.922
         * - Côte d'Ivoire — Bangolo
           - 102
           - 0.663
           - **0.797**
           - 0.844
           - 0.755
         * - South Africa — Worcester
           - 156
           - 0.592
           - **0.744**
           - 0.867
           - 0.651
         * - **Aerial (mean of 9 AOIs)**
           - 815
           - 0.813
           - **0.893**
           - 0.913
           - 0.878

      *Area-based IoU / F1 / Precision / Recall measured against ground-truth building masks; evaluation run 2026-06-13.*

   .. tab-item:: Satellite imagery

      .. list-table::
         :widths: 28 14 12 14 14 14
         :header-rows: 1

         * - AOI (location)
           - Predicted features
           - IoU
           - F1
           - Precision
           - Recall
         * - Russia — Ufa
           - 426
           - 0.821
           - **0.902**
           - 0.897
           - 0.907
         * - Saudi Arabia — Riyadh
           - 225
           - 0.817
           - **0.899**
           - 0.920
           - 0.879
         * - India — Bangalore
           - 508
           - 0.779
           - **0.876**
           - 0.859
           - 0.894
         * - India — Thane
           - 429
           - 0.768
           - **0.869**
           - 0.889
           - 0.849
         * - United Arab Emirates — Abu Dhabi
           - 142
           - 0.751
           - **0.858**
           - 0.828
           - 0.890
         * - **Satellite (mean of 5 AOIs)**
           - 1730
           - 0.787
           - **0.881**
           - 0.879
           - 0.884

      *Area-based IoU / F1 / Precision / Recall measured against ground-truth building masks; evaluation run 2026-06-16.*

.. seealso::

    📊 See :doc:`per-location benchmark details <buildings_benchmark_07-06>` for the
    area-by-area breakdown of both sets, the comparison with the previous version and
    prediction-vs-ground-truth overlays.

.. mf-cta::
