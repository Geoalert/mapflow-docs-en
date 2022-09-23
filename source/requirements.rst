Requirements for using the platform
====================================

Follow the requirements listed on the page with :doc:`Models reference <userguides/pipelines>` to process images with the Mapflow platform.

Please pay attention to the following:

  * images must be in Uint8 format. If your image is not of this type, please use our `image preprocessing script <https://github.com/Geoalert/mapflow_data_preprocessor/>`_ or other tools to translate it to the appropriate format;
  * your imagery must be georeferenced in geographic or projected coordinate system, WGS84;
  * each Mapflow model has its recommendations for the spatial resolution of the input data.

In case of non-compliance with any requirements, the following errors occur: 

.. toctree::
   :glob:
   :maxdepth: 1

   messages/error_messages
   

