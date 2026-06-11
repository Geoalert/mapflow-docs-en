.. _Buildings model:

🏠 Buildings
=================

Extracting of rooftops of buildings from imagery of high resolution.
High performance deep learning model is trained to detect the buildings roofs.

|:label:|

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
against manually annotated ground truth, and compared with the **previous version**
(the current production 🏠 Buildings model). Metrics are object-wise (a prediction
counts as a true positive when it matches a ground-truth footprint). Each cell reads
*previous* → **v.07-06** with the change (Δ) in parentheses; a positive Δ means
v.07-06 improved.

.. list-table::
   :widths: 22 26 26 26
   :header-rows: 1

   * - AOI (location)
     - F1  (prev → v.07-06)
     - Precision  (prev → v.07-06)
     - Recall  (prev → v.07-06)
   * - United States
     - 0.916 → **0.960**  (+0.044 ▲)
     - 0.870 → **0.952**  (+0.082 ▲)
     - 0.968 → 0.968  (±0.000)
   * - Canada
     - 0.809 → **0.809**  (+0.000 ±)
     - 0.752 → **0.771**  (+0.019 ▲)
     - 0.874 → 0.851  (−0.023 ▼)
   * - South Africa
     - 0.782 → **0.739**  (−0.043 ▼)
     - 0.956 → **0.891**  (−0.065 ▼)
     - 0.662 → 0.631  (−0.031 ▼)
   * - New Zealand
     - 0.788 → **0.734**  (−0.054 ▼)
     - 0.722 → **0.691**  (−0.031 ▼)
     - 0.867 → 0.783  (−0.084 ▼)
   * - Côte d'Ivoire
     - 0.778 → **0.717**  (−0.061 ▼)
     - 0.863 → **0.814**  (−0.049 ▼)
     - 0.708 → 0.640  (−0.068 ▼)
   * - United Kingdom
     - 0.646 → **0.703**  (+0.057 ▲)
     - 0.539 → **0.650**  (+0.111 ▲)
     - 0.804 → 0.765  (−0.039 ▼)
   * - Australia
     - 0.579 → **0.674**  (+0.095 ▲)
     - 0.525 → **0.625**  (+0.100 ▲)
     - 0.646 → 0.732  (+0.086 ▲)
   * - **Global (mean of 7 AOIs)**
     - 0.757 → **0.762**  (+0.005 ▲)
     - 0.747 → **0.771**  (+0.024 ▲)
     - 0.790 → 0.767  (−0.023 ▼)

*Object-wise F1 / Precision / Recall measured against ground-truth footprints; evaluation run 2026-06-09.
"prev" = previous version (current production 🏠 Buildings); ▲ improvement, ▼ regression vs the previous version.*

See :doc:`per-location benchmark details <buildings_benchmark_07-06>` for the
area-by-area breakdown, including comparison with the previous candidate (v.02-06)
and prediction-vs-ground-truth overlays.


