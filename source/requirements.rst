Requirements for using the platform
====================================

Follow the requirements listed on the page with :doc:`Models reference <userguides/pipelines>` to process images with the Mapflow platform.

.. note::
    Please pay attention to the following:
    * images you upload must be in `Uint8` format. If your image is not of this type, please use our `image preprocessing script <https://github.com/Geoalert/mapflow_data_preprocessor/>`_ or other tools to translate it to the appropriate format;
    * your imagery must be georeferenced in geographic or projected coordinate system, ellipsoid WGS84;
    * each Mapflow model has its recommendations for the spatial resolution of the input data.

In case of non-compliance with any requirements, the system reports an error. 
If you are using Mapflow Web or Mapflow QGIS plugin, the error messages are shown in the user interface.
If you use API, see errors description in :doc:`API docs <api/error_messages>`.






   

