.. _Processing API:

Mapflow Processing API
========================

The Mapflow Processing API enables you to run AI-powered geospatial analysis on satellite and aerial imagery. Use it to detect buildings, roads, forests, and more at scale.

.. attention::
    Projects and processings created via the API are **synchronized** with `Mapflow.ai <https://app.mapflow.ai/>`_. API calls consume your Mapflow credits.

Base URL
--------

.. code-block:: text

   https://api.mapflow.ai/rest


Authentication
--------------

All API requests require an API token. Generate yours in `profile settings <https://app.mapflow.ai/account>`_.

.. code-block:: bash

   curl -H "Authorization: Bearer YOUR_API_TOKEN" \
     https://api.mapflow.ai/rest/user/status

See :doc:`authorization guide <../userguides/mapflow_auth>` for details.


Quick Start
-----------

**Run your first processing in 3 steps:**

1. **Create a project**

   .. code-block:: bash

      curl -X POST https://api.mapflow.ai/rest/projects \
        -H "Authorization: Bearer YOUR_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "name": "My First Project",
          "description": "Buildings detection"
        }'

   Response: ``{"id": "project-uuid", ...}``

2. **Create and run processing**

   .. code-block:: bash

      curl -X POST https://api.mapflow.ai/rest/processings/v2 \
        -H "Authorization: Bearer YOUR_TOKEN" \
        -H "Content-Type: application/json" \
        -d '{
          "name": "Downtown Buildings",
          "projectId": "project-uuid",
          "wdName": "🏠 Buildings",
          "geometry": {
            "type": "Polygon",
            "coordinates": [[
              [37.6156, 55.7558],
              [37.6256, 55.7558],
              [37.6256, 55.7608],
              [37.6156, 55.7608],
              [37.6156, 55.7558]
            ]]
          },
          "params": {
            "sourceParams": {
              "dataProvider": {
                "providerName": "Mapbox",
                "zoom": 18
              }
            }
          }
        }'

   Response: ``{"id": "processing-uuid", "status": "IN_PROGRESS", ...}``

3. **Check status and download results**

   .. code-block:: bash

      # Check status
      curl https://api.mapflow.ai/rest/processings/{processing-uuid}/v2 \
        -H "Authorization: Bearer YOUR_TOKEN"

      # Download results (when status = "OK")
      curl https://api.mapflow.ai/rest/processings/{processing-uuid}/result \
        -H "Authorization: Bearer YOUR_TOKEN" \
        -o results.geojson

**Next steps:** Explore :ref:`available models <Model requirements>`, upload :ref:`custom imagery <upload-images>`, or review the :ref:`complete API reference <api-reference>`.




