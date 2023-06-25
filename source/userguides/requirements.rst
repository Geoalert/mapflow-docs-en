Requirements for using the platform
====================================

Upload GeoTIFF requirements
----------------------------

.. note::
    Please pay attention to the following:

    * Images you upload must be in `Uint8` format. If your image is not of this type, please use our `image preprocessing script <https://github.com/Geoalert/mapflow_data_preprocessor/>`_ or other tools to translate it to the appropriate format;
    * Your imagery must be georeferenced in geographic or projected coordinate system, ellipsoid WGS84, it is recommended to use UTM or Web Mercator;
    * Your image is supposed to be RGB composite, RGBa and Singleband will work as well*;
    * Each Mapflow model has its recommendations for the spatial resolution of the input data, see :ref:`Model requirements` below

In case of non-compliance with any requirements, the system reports an error. 
If you are using Mapflow Web or Mapflow QGIS plugin, the error messages are shown in the user interface.
For more details, see :doc:`errors description <../api/error_messages>`.

.. _Model requirements:

Model requirements
-------------------

The table below lists model requirements for spatial resolution of the input imagery.

**"Required"** means that the imagery with resolution outside of this range will
be rejected from processing and the request will fail.

**"Recommended"** means that the model is fit specifically for this spatial resolution.
Any images of higher resolution will be downsampled before processing, so it gives no profit to upload higher resolution.
Images of lower resolution (if meeting the "required" section) will be upsampled,
but the results will not be so good as for recommended resolution.

GSD is specified in `UTM coordinate system <https://proj4.org/en/9.2/operations/projections/utm.html>`_,
and may not correspond to what you see as "pixel size" if your image's coordinate system differs.

`Learn more <https://wiki.openstreetmap.org/wiki/Zoom_levels>`_  about zoom and spatial resolution of imagery basemaps.

.. list-table::
   :widths: 20 50 10 10 10 10
   :header-rows: 1

   * - Model
     - Description
     - Recommended zoom
     - Recommended GSD m/px
     - Required zoom range
     - Required GSD range, m/px
   * - Buildings
     - Extract roof contours, with optional classification, simplification and height estimation
     - 18
     - 0.5
     - 17 – 18
     - 0.3 - 1.5
   * - High-density housing [Mapflow Web only]
     - Extraction and instance detection of the building roofprints in the areas of high density housing
     - 19
     - 0.3
     - 18-19
     - 0.15 - 1.2
   * - Buildings (Aerial imagery)
     - Extract roof contours (roofprints) from very high-resolution aerial imagery
     - 20
     - 0.1
     - 20-21
     - 0.05-0.4
   * - Forest
     - Extract segmentation masks of forested areas from high-resolution RGB images
     - 18
     - 0.5
     - 17 – 18
     - 0.3 - 2.0
   * - Forest with heights [Mapflow API/QGIS only]
     - Extract segmentation masks of forested areas from high-resolution RGB images with separation by height classes
     - 18
     - 0.5
     - 17 – 18
     - 0.3 - 2.0
   * - Roads
     - Extract road mask from high-resolution satellite imagery
     - 18
     - 0.5
     - 17 – 18
     - 0.3 - 1.2
   * - Constructions
     - The model highlights areas in the satellite image that contain construction sites and buildings under construction
     - 18
     - 0.5
     - 17 – 18
     - 0.3 - 2.0
   * - Agriculture fields
     - Extraction and instance separation of agriculture fileds from high-resolution satellite imagery
     - 17
     - 1.2
     - 15-17
     - 0.5-4.8

\* Mapflow.ai can also process single-band (panchromatic) imagery, but the NN models are not tuned for such kind of data, so the quality of the result may be worse than expected.