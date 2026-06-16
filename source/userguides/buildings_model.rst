.. _Buildings model:

🏠 Buildings
=================

Extracting of rooftops of buildings from imagery of high resolution.
High performance deep learning model is trained to detect the buildings roofs.

**Model tags** |:label:|

:Version: 2026-07-06
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

Aerial imagery
~~~~~~~~~~~~~~~~

Latest update — **🏠 Buildings v.2026-07-06** (Global, Segmentation, 0.3 m / z19).
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

Satellite imagery
~~~~~~~~~~~~~~~~~~

Additional validation of **🏠 Buildings v.2026-07-06** on satellite imagery across 5 dense
urban areas of interest.

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
    area-by-area breakdown of both the global and satellite sets, including comparison
    with the previous version and prediction-vs-ground-truth overlays.


