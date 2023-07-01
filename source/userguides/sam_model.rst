✨ Segment anything
---------------------

The “Segment Anything” (originaly introduced by Meta as universal segmentation model) is available as yet another experimental model in Mapflow. We adjusted it to Mapflow workflows to be used on a sccale. There are the same steps required to launch this model: 
1. Select your data source 
2. Add your geographical area or your image extent
Yet there is one main difference in UI:

- if you run this model using GTIFF file — the original resolution will be used and you get your results.
- if you run it on TMS (e.g. imagery basemaps like default Mapbox Satellite) — you need to define the Zoom (image resolution) the model will be applied to. 

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * Zoom
     - 14
     - 16
     - 18
     - Aero
   * Semantics
     - Land use, forests, parks, fields, bodies of water
     - Small fields, large buildings, lawns, plots
     - Farms, buildings, groups of trees, etc.
     - Houses, trees, vehicles, roof structures, etc.
