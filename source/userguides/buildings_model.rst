.. _Buildings model:

🏠 Buildings
=================

Extracting of rooftops of buildings from imagery of high resolution.
High performance deep learning model is trained to detect the buildings roofs.

**Model tags** |:label:|

:Version: 07-06
:Geo Domain: Global
:Model method: Segmentation
:GSD / Map Zoom: 0.3 m / z19

*Note:* The building predictions with area less than 20 sq.m. are removed to avoid clutter

The model does not extract the footprints directly, because they are not clearly visible in the images, but it can obtain them, just like human cartographers, by moving the roof to the bottom of the wall (see Additional options).

**Additional options:**

* **Classification by types of buildings** – typology of buildings is represented by the main classes (see :ref:`reference <buildings_classes>`).
* **Regularization** - the algorithm corrects the irregularities of the contours of our model. The irregular geometries are replaced with rectangles, circles or arbitary polygons with 90 degree angles, which fits better to the original shape. This option produces much more map-friendly shapes which look better, but some original mask accuracy can be lost.
* **Simplification** - simplifies the building shape, staying close to the original mask, adjusted for curve and complex shapes. More approximated shapes, but less right angles.
* **Merge with OSM** - some of the areas have great coverage of OpenStreetMap data, and if you prefer human-annotated data, you can select this option.In this case, we check for each building whether it has a good corresponding object in OSM (Jaccard index) and if there is one, we replace our result with OSM polygon. This makes the result not based on the image, so the buildings can be shifted from actual positions. Also the corrected buildings are rotated to align with the nearest roads downloaded from OSM. 
* **Height Estimation (beta)** – feature leverages a dedicated regression-based model that infers height using visual indicators such as shadow length and visible wall segments. The result is what is termed **3D building footprints** where the building's countour is projected to ground level instead of the roof outline. This is especially useful for oblique imagery, where roofs often appear shifted.

   
Benchmarks - segmentation
----------------------------


Latest update — **🏠 Buildings v.07-06** (Global, Segmentation, 0.3 m / z19).
The model was evaluated on a global validation set of 7 areas of interest (AOI)
against manually annotated ground truth. Metrics are area-based: IoU is the
intersection-over-union of the predicted and ground-truth building masks, and
F1 / Precision / Recall are computed on the overlapping mask area.

.. list-table::
   :widths: 24 14 12 14 14 14
   :header-rows: 1

   * - AOI (location)
     - Predicted features
     - IoU
     - F1
     - Precision
     - Recall
   * - United States
     - 65
     - 0.907
     - **0.951**
     - 0.983
     - 0.921
   * - Canada
     - 103
     - 0.870
     - **0.930**
     - 0.934
     - 0.927
   * - Australia
     - 92
     - 0.868
     - **0.929**
     - 0.914
     - 0.945
   * - New Zealand
     - 76
     - 0.838
     - **0.912**
     - 0.900
     - 0.924
   * - United Kingdom
     - 68
     - 0.813
     - **0.897**
     - 0.873
     - 0.922
   * - Côte d'Ivoire
     - 102
     - 0.663
     - **0.797**
     - 0.844
     - 0.755
   * - South Africa
     - 95
     - 0.495
     - **0.662**
     - 0.767
     - 0.582
   * - **Global (mean of 7 AOIs)**
     - 601
     - 0.779
     - **0.868**
     - 0.888
     - 0.854

*Area-based IoU / F1 / Precision / Recall measured against ground-truth building masks; evaluation run 2026-06-13.*

.. seealso::

    📊 See :doc:`per-location benchmark details <buildings_benchmark_07-06>` for the
    area-by-area breakdown, including comparison with the previous version and prediction-vs-ground-truth overlays.


