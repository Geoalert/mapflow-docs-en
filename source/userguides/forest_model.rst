.. meta::
   :description: Detect forest, trees and shrub vegetation from 0.6-0.3 m satellite imagery. Covers sparse forest, shrubland, small tree groups and narrow tree lines, with height classes and tree crowns.

.. rst-class:: mf-page

Forest and trees
================

.. mf-model-hero:: forest

The model is trained on 0.6–0.3 m imagery from different regions and climate zones. Its resolution
is enough to find small groups of trees and narrow tree lines. Use imagery from the growing season:
leafless trees and snow-covered vegetation are not the target class.

Scenarios with this model
-------------------------

Each scenario is the Forest and trees model with one option switched on.
Choose options in the run form of Mapflow Web or the QGIS plugin.

.. mf-scenario-cards:: forest

.. _scenario-vegetation-height:

Vegetation height along power lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. mf-scenario:: vegetation-height

.. _forest_classes:

.. note::
   Height classes:

   * shrubs lower than 4 m;
   * forest from 4 to 10 m;
   * forest higher than 10 m.

   The classes support vegetation management in power line corridors and similar zones,
   see the `professional solutions by Geoalert <https://geoalert.io/solutions/power>`_.
   The thresholds can be customized for your requirements.

.. _scenario-tree-crowns:

Count individual trees
~~~~~~~~~~~~~~~~~~~~~~

.. mf-scenario:: tree-crowns

.. important::
   Use 0.3 m imagery (about zoom 19) with the **Tree crowns** options when you need individual trees.

All options
-----------

.. rst-class:: mf-options

Height estimation
   Classifies the forest mask by height: shrubs under 4 m, forest 4–10 m, forest over 10 m.

Tree crown polygons
   Extracts tree crowns from forest and from free-standing trees, as polygons.

Tree crown points
   Extracts tree crowns from forest and from free-standing trees, as points with a crown radius.

Sample results
--------------

.. container:: mf-figures

   .. figure:: _static/processing_result/forest_model_3.jpg
      :alt: Forest model result: solid forest mask
      :class: no-scaled-link

      Solid **forest** mask

   .. figure:: _static/processing_result/output-crowns.gif
      :alt: Forest model result: tree crowns as points

      **Tree crowns**, points

   .. figure:: _static/processing_result/forest_w_heights_model.jpg
      :alt: Forest model result: forest with height classes
      :class: no-scaled-link

      **Forest with heights** (raster output)

.. _forest_benchmarks:

Benchmarks
----------

**Forest and trees v.2026-07-03** (Global, segmentation) was evaluated on 8 areas of interest
against manually annotated ground truth. Metrics are area-based: IoU is the intersection-over-union
of the predicted and ground-truth vegetation masks, and F1, precision and recall are computed
on the overlapping mask area.

.. list-table::
   :widths: 32 14 12 14 14 14
   :header-rows: 1

   * - AOI (location)
     - Predicted features
     - IoU
     - F1
     - Precision
     - Recall
   * - Italy — Crotone
     - 254
     - 0.862
     - **0.926**
     - 0.944
     - 0.909
   * - Spain — Madrid
     - 368
     - 0.813
     - **0.897**
     - 0.880
     - 0.915
   * - Philippines — Balanga
     - 220
     - 0.806
     - **0.892**
     - 0.864
     - 0.923
   * - Spain — Velilla de San Antonio
     - 1070
     - 0.784
     - **0.879**
     - 0.894
     - 0.864
   * - Spain — Cuenca
     - 409
     - 0.763
     - **0.865**
     - 0.859
     - 0.872
   * - Uzbekistan — Tashkent
     - 156
     - 0.730
     - **0.844**
     - 0.905
     - 0.791
   * - Spain — Rus
     - 249
     - 0.617
     - **0.763**
     - 0.699
     - 0.841
   * - Argentina — La Banda
     - 93
     - 0.576
     - **0.731**
     - 0.653
     - 0.829
   * - **Global (mean of 8 AOIs)**
     - 2819
     - 0.744
     - **0.850**
     - 0.837
     - 0.868

*Area-based IoU / F1 / Precision / Recall measured against ground-truth vegetation masks; evaluation run 2026-07-03.
Compared with the previous version v.2025-06-14 (mean F1 0.513, IoU 0.396).*

.. seealso::

    📊 See :doc:`per-location benchmark details <forest_benchmark_2026-07-03>` for the
    area-by-area breakdown, the comparison with the previous version and prediction-vs-ground-truth overlays.

.. mf-cta::
