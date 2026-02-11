.. _Data API:

Mapflow Data API
==================

The Mapflow Data API enables you to manage custom imagery, organize it into mosaics, and search satellite imagery from external providers. Use your imagery for AI-powered analysis with the :doc:`Processing API <processing_api>`.

.. note::
    .. figure:: _static/postman_logo.png
       :alt: Postman Collection
       :align: left
       :width: 1cm

   Try our `Postman Collection <https://documenter.getpostman.com/view/5400715/2s935hS7ky>`_ for interactive API testing.


Base URL
--------

.. code-block:: text

   https://api.mapflow.ai/rest


Authentication
--------------

All API requests require an API token. Generate yours in `profile settings <https://app.mapflow.ai/account>`_.

.. code-block:: bash

   curl -H "Authorization: Bearer YOUR_API_TOKEN" \
     https://api.mapflow.ai/rest/rasters/memory

See :doc:`authorization guide <../userguides/mapflow_auth>` for details.


Quick Start
-----------

**Upload and process your imagery in 3 steps:**

1. **Create a mosaic**

   .. code-block:: bash

      curl -X POST https://api.mapflow.ai/rest/rasters/mosaic \
        -H "Authorization: Bearer YOUR_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{"name": "My Aerial Survey", "tags": ["survey-2024"]}'

   Response: ``{"id": "mosaic-uuid", ...}``

2. **Upload images to mosaic**

   .. code-block:: bash

      curl -X POST https://api.mapflow.ai/rest/rasters/mosaic/{mosaic-uuid}/image \
        -H "Authorization: Bearer YOUR_TOKEN" \
        -H "Content-Type: multipart/form-data" \
        -F "file=@/path/to/orthophoto.tif"

   Response: ``{"id": "image-uuid", ...}``

3. **Run processing with uploaded imagery**

   .. code-block:: bash

      curl -X POST https://api.mapflow.ai/rest/processings/v2 \
        -H "Authorization: Bearer YOUR_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "name": "Building Detection",
          "projectId": "project-uuid",
          "wdName": "🏠 Buildings",
          "geometry": {...},
          "params": {
            "sourceParams": {
              "myImagery": {"mosaicId": "mosaic-uuid"}
            }
          }
        }'

**Next steps:** Explore :ref:`satellite imagery search <imagery-search>`, manage :ref:`storage limits <storage-management>`, or review the :ref:`complete API reference <api-reference>`.


For complete API reference documentation including all endpoints, parameters, and examples, see :ref:`api-reference`.





