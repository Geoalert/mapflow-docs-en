   
Forest Mapping classes
======================

Here is presented a list of classes for Foret vegetation Mapping Model.
There two options for forest semantic classification:

* Classification by heights – classification the areas of vegetation and shrub vegetation by height classes according to the specified thresholds: 0-4 m, 4-10 m, 10+ m. Forest areas of each height class are polygonized in separate features, the height class is indicated in its properties. Heights thresholds are customizable values in the processing pipeline.

* Classification by overgrowth density – classification of the area of vegetations and shrub vegetation into classes according to the density and height: high forest, low (growing) forest, open woodland, shrub.


   .. tabularcolumns:: |p{3cm}|p{5cm}|p{7cm}|

   .. csv-table::
      :file: _static/csv/classes_forest.csv 
      :header-rows: 1 
      :class: longtable
      :widths: 1 1 1 