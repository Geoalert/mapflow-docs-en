.. _Processing API:

Mapflow processing API
========================

.. attention::
    The projects and processings that you create in `Mapflow.ai <https://app.mapflow.ai/>`_ won’t be available via the API and vice versa. Neither can your Mapflow credits be used to run processings via the API. Use the API token to start using the API, which you need to generate in the `profile settings <https://app.mapflow.ai/account>`_ (see :doc:`authorization to work with the Mapflow API <../userguides/mapflow_auth>`).

.. note::
    .. figure:: _static/postman_logo.png
       :alt: Preview results
       :align: left
       :width: 1cm

   Check and run this `Postman collection for API <https://documenter.getpostman.com/view/5400715/TzmCiu5h>`_.

.. important::
  You should follow the requirements specified on the page with :doc:`the description of models <../userguides/pipelines>` when uploading your own images for processing through the API of the Mapflow platform. Send a request using data preprocessing to help@geoalert.io.


User status
-------------

Returns user status for the the given user account, including:
* User limits
* Default and custom :ref:`Models` (every User account is connected to the default models, yet specific models have to be linked to the User account by Administrator)
* Default and custom :ref:`Data Providers` (every User account is linked to the default data providers, yet specific commercial providers have to be linked to the User account by Administrator))

.. note::
  If user account is linked to the :ref:`Team accounts` - it returns Team's description as well


Response example:

.. code:: json

    {
      "email": "admin@geoalert.io",
      "processedArea": 45221388394,
      "remainingArea": 54778611606,
      "areaLimit": 100000000000,
      "memoryLimit": 1000000000,
      "models": [
          {
              "id": "30ddfd15-04aa-47f6-9ceb-68ce709fd710",
              "name": "🏠 Buildings",
              "description": "",
              "created": "2023-02-01T08:17:03.871690Z",
              "updated": "2023-05-11T14:24:31.456180Z",
              "pricePerSqKm": 13.0,
              "blocks": [
                {
                    "name": "Classification",
                    "displayName": "Classification",
                    "optional": true,
                    "price": 3.0
                },
                {
                    "name": "Simplification",
                    "displayName": "Polygonization",
                    "optional": true,
                    "price": 5.0
                },
                {
                    "name": "OSM",
                    "displayName": "Merge with OSM",
                    "optional": true,
                    "price": 0.0
                }
            ]
          },
          {
              "id": "5d47a57c-3274-4014-aa04-daac416782f7",
              "name": "🚗 Roads",
              "description": "",
              "created": "2023-02-01T08:17:03.371720Z",
              "updated": "2023-05-11T14:24:31.605710Z",
              "pricePerSqKm": 5.0
          }
      ],
      "teams": [
          {
              "teamId": "a6c5a4cf-c693-4441-8bef-028ac0f2d5d9",
              "name": "My Geoalert Team",
              "role": "OWNER",
              "activeUntil": null,
              "creditsLimit": null
          }
      ]
  }

Projects
---------

Get project
^^^^^^^^^^^^^

``GET https://api.mapflow.ai/rest/projects/{projectId}`` 

Returns the project with the specified ID.  

Response example:

.. code:: json

    {
        "id": "546d148f-19a1-40d8-8f16-d1e6dabfd204",
        "name": "test",
        "description": "test",
        "progress": {
            "status": "UNPROCESSED",
            "percentCompleted": 0,
            "details": []
        },
        "aoiCount": 0,
        "area": 0,
        "user": {
            "id": "61cd6899-19e8-44a0-97db-b86f1a9b7af4",
            "login": "user@user.com",
            "email": "user@user.com",
            "role": "USER",
            "created": "2019-12-16T16:10:29.492358Z"
        },
        "isDefault": false,
        "created": "2020-05-13T13:00:31.978Z",
        "updated": "2020-05-13T13:00:31.978Z",
        "workflowDefs": [
            {
                "id": "084474b5-e001-456f-a486-f62f5ee1ffe1",
                "name": "🏠 Buildings",
                "created": "2020-08-11T19:57:40.974170Z",
                "updated": "2020-08-11T19:57:40.974172Z"
            }
        ]
    }

.. _Projects - API:

Get default project
^^^^^^^^^^^^^^^^^^^^^

.. important::

  Default project is created for each user upon registration.

``GET https://api.mapflow.ai/rest/projects/default`` 

Returns the name and ID of the user's default project and the user's account settings. 

.. code:: json

  {
      "id": "ea2281ab-53f0-4839-9d38-8e3648ee377f",
      "name": "Default",
      "description": null,
      "progress": {
          "status": "OK",
          "percentCompleted": 100,
          "details": [
              {
                  "status": "OK",
                  "count": 1,
                  "area": 836643,
                  "statusUpdateDate": "2022-12-20T08:14:38.882673Z"
              }
          ],
          "completionDate": "2022-12-20T08:14:38.882673Z"
      },
      "aoiCount": 23,
      "area": 20885015,
      "user": {
          "id": "25b12411-bd16-4a31-9842-728264a3aefd",
          "login": "test_user@test.com",
          "email": "test_user@test.com",
          "role": "USER",
          "areaLimit": 50000000,
          "aoiAreaLimit": 50000000,
          "processedArea": 21863903,
          "created": "2022-10-20T14:54:59.630308Z",
          "updated": "2022-12-06T14:00:53.051512Z",
          "isPremium": false
      },
      "isDefault": true,
      "created": "2022-10-20T14:54:59.636598Z",
      "updated": "2022-10-20T14:54:59.636599Z",
      "workflowDefs": [
          {
              "id": "ad7a5460-c903-402b-9c21-b12aa2fc9f69",
              "name": "🏗️ Construction sites",
              "description": null,
              "created": "2022-10-20T14:54:59.690562Z",
              "updated": "2022-10-20T14:54:59.690562Z"
          },
          {
              "id": "495192d6-5dfc-4167-842e-3d76d8abe244",
              "name": "🚜 Fields (Sentinel-2)",
              "description": null,
              "created": "2022-10-20T14:54:59.748459Z",
              "updated": "2022-10-20T14:54:59.748459Z"
          },
          {
              "id": "9c2ceb15-2063-49b2-afec-d1752cbab2e1",
              "name": "🚗 Roads",
              "description": null,
              "created": "2022-10-20T14:54:59.865654Z",
              "updated": "2022-10-20T14:54:59.865654Z"
          },
          {
              "id": "decc5854-3a92-4b25-8e5b-895de9fa4ef3",
              "name": "🌲↕️ Forest with heights",
              "description": null,
              "created": "2022-10-20T14:54:59.787793Z",
              "updated": "2022-11-25T13:08:41.124862Z"
          }
      ]
  }

Get all projects
^^^^^^^^^^^^^^^^^^^

``GET https://api.mapflow.ai/rest/projects`` 

Returns the list of all user's projects.  


Create project
^^^^^^^^^^^^^^^^^^^

``POST https://api.mapflow.ai/rest/projects``

Creates a new project, and returns its immediate state.  

Request body example:

.. code:: json

    {
        "name": "test",          
        "description": "test"
    }



* Name of the project
* Arbitrary description of this project

Response: *the newly created project* contains the project ID and the description of the default AI-models as they are linked to every new project.

.. warning::
    The custom AI-models won't be linked to the new project automatically. 

Rename project
^^^^^^^^^^^^^^^^^^^^^

``PUT https://api.mapflow.ai/rest/projects/{projectId}``

Request body example:

.. code:: json

    {
      "name": "new name (optional)",
      "description": "new description (optional)"
    }


Delete project
^^^^^^^^^^^^^^^^^^^

``DELETE https://api.mapflow.ai/rest/projects/{projectId}`` 

Deletes the project. Cascade deletes any child entities.

Processings
------------

Get all processings
^^^^^^^^^^^^^^^^^^^^^

``GET https://api.mapflow.ai/rest/processings``

Returns the list of the user's processings by the Default project

Get all processings by Project Id
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``GET https://api.mapflow.ai/rest/projects/{projectId}/processings``

Returns the list of the user's processings by user's project

Get processing by Id
^^^^^^^^^^^^^^^^^^^^^^

``GET https://api.mapflow.ai/rest/processings/{processingId}``

Returns the processing with the specified id.  

Response example:

.. code:: json

    {
      "id": "65285409-ac88-4fc0-a937-193cf42c2343",
      "name": "Test processing",
      "description": null,
      "projectId": "a45aa059-fc95-4da0-80e9-2f258fa42c3f",
      "vectorLayer": {
          "id": "726bdc81-4c43-44ba-9d1b-ca5ed53f23fe",
          "name": "Test processing",
          "tileJsonUrl": "https://app.mapflow.ai/api/layers/4f84c84a-3678-4a11-bd20-dac6f230b08f.json",
          "tileUrl": "https://app.mapflow.ai/api/layers/4f84c84a-3678-4a11-bd20-dac6f230b08f/tiles/{z}/{x}/{y}.vector.pbf"
      },
      "rasterLayer": {
          "id": "9cb1df8d-d26c-4458-8e4b-ffd03871edbf",
          "tileJsonUrl": "https://app.mapflow.ai/api/v0/cogs/tiles.json?uri=s3://mapflow-rasters/db3f192f-010d-4fc5-9cbe-f44bc569ba59",
          "tileUrl": "https://app.mapflow.ai/api/v0/cogs/tiles/{z}/{x}/{y}.png?uri=s3://mapflow-rasters/db3f192f-010d-4fc5-9cbe-f44bc569ba59"
      },
      "workflowDef": {
          "id": "c6a71c32-972c-4d67-95a1-e9f3dfc033c9",
          "name": "Buildings (⭐️ Aerial imagery)",
          "description": "Custom model: segmentation of buildings in aerial imagery at resolution 10 cm/pixel",
          "created": "2023-02-07T12:07:35.259144Z",
          "updated": "2023-09-01T13:03:20.905987Z",
          "pricePerSqKm": 33.0,
          "blocks": []
      },
      "aoiCount": 1,
      "area": 12010038,
      "cost": 1638,
      "status": "OK",
      "reviewStatus": null,
      "rating": null,
      "percentCompleted": 100,
      "params": {
          "url": "https://rasters-production.mapflow.ai/api/v0/cogs/tiles/{z}/{x}/{y}.png?uri=s3://mapflow-rasters/4738260d-0fab-479f-beff-633d50a388f0",
          "source_type": "xyz",
          "crs": "EPSG:3857"
      },
      "blocks": [],
      "meta": {
          "source": "tif",
          "source-app": "qgis",
          "version": "1.7.0"
      },
      "messages": [],
      "created": "2023-03-29T06:48:35.103854Z",
      "updated": "2023-07-09T13:32:25.540726Z"
    }

If the processing failed, the response also contains the code and parameters of the error in the `messages` section.
If different AOIs failed with the same error, only one of the repeated errors is returned.
Example of the failed processing response:

.. code:: json

    {
        "id": "6ad89b64-38fd-408f-acbb-75035ec52787",
        "status":"FAILED",
        "percentCompleted":0,
        "messages":[{
            "code": "source-validator.PixelSizeTooHigh",
            "parameters": {
                "max_res": "1.2",
                "level": "error",
                "actual_res": "5.620983603290215"
             }
        }
        ]
    }

Possible error codes, parameters and desctiptions see in :doc:`Error Messages <error_messages>`
 

Create processing
^^^^^^^^^^^^^^^^^^^

``POST https://api.mapflow.ai/rest/processings``

Runs a processing, and returns its immediate state.
Request body sample:

.. code:: json

    {
        "name": "Test",                                      //Name of this processing. Optional.
        "description": "A simple test",                      //Arbitrary description of this processing. Optional.
        "projectId": "20f05e39-ccea-4e26-a7f3-55b620bf4e31", //Project id. Optional. If not set, the user's default project will be applied.
        "wdName": "🏠 Buildings",                            //The name of a workflow (AI model). Could be "🏠 Buildings", or "🌲 Forest", etc. See ref. below
        "geometry": {                                        //A geojson geometry of the area of processing.
            "type": "Polygon",
            "coordinates": [
              [
                [
                  37.29836940765381,
                  55.63619642594767
                ],
                [
                  37.307724952697754,
                  55.63619642594767
                ],
                [
                  37.307724952697754,
                  55.64024152130109
                ],
                [
                  37.29836940765381,
                  55.64024152130109
                ],
                [
                  37.29836940765381,
                  55.63619642594767
                ]
              ]
            ]
        },
        "params": {                           #Arbitrary string parameters of this processing. Optional.
            "source_type": "xyz",
            "url": "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        },
        "meta": {                             #Arbitrary string key-value for this processing (metadata). Optional.
            "test": "test"
        }
    }


To process a user-provided raster (see `Upload GeoTIFF for processing` section), set parameters as follows:  

 .. code:: json

        "params": {
            "source_type": "tif",
            "url": "s3://mapflow-rasters/9764750d-6047-407e-a972-5ebd6844be8a/raster.tif"
        }

Response: the newly created processing.


Customize processing with the workflow options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``POST https://api.mapflow.ai/rest/processings``

Processing workflow can be custoized with enabling some model options.
The "options" can be retrieved through the ``user/status`` request as ``{"blocks": [{"name":<>, "displayName": <>, "optional":true, "price": <>}]`` in the ``models`` list.

Request body example

.. code:: json
  
  {
      "blocks": [
          {
              "name": "Simplification",
              "enabled": false
          },
          {
              "name": "OSM",
              "enabled": false
          }
      ]
  }

Rename processing
^^^^^^^^^^^^^^^^^^^

``PUT https://api.mapflow.ai/rest/processing/{processingId}``

Request body example:

.. code:: json

    {
      "name": "new name (optional)",
      "description": "new description (optional)"
    }


Restart processing
^^^^^^^^^^^^^^^^^^^

``POST https://api.mapflow.ai/rest/processings/{processingId}/restart``

Restarts failed partitions of this processing. Doesn't restart non-failed partitions. Each workflow is restarted from the first failed stage. Thus, the least possible amount of work is performed to try and bring the processing into successful state.

Link processing to another project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``PUT https://api.mapflow.ai/rest/processings/{processing_id}``

Links processing to another project by project ID

.. code:: bash
  
  curl --location --request PUT 'https://api.mapflow.ai/rest/processings/{processing_id}' \ 
  --header 'Content-Type: application/json' \ 
  --header 'Authorization: Basic <YOUR TOKEN>' \ 
  --data-raw '{"projectId": "new_project_id"}'

Delete processing
^^^^^^^^^^^^^^^^^^^

``DELETE https://api.mapflow.ai/rest/processings/{processingId}``

Deletes this processing. Cascade deletes any child entities.

Get processing AOIs
^^^^^^^^^^^^^^^^^^^

``GET https://api.mapflow.ai/rest/processings/{processingId}/aois``  

Returns a list of the defined geographical areas for processing in GeoJSON.  

Response sample:

.. code:: json

    [
        {
            "id": "b86127bb-38bc-43e7-9fa9-54b37a0e17af",
            "status": "IN_PROGRESS",
            "percentCompleted": 0,
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            37.29836940765381,
                            55.63619642594767
                        ],
                        [
                            37.29836940765381,
                            55.64024152130109
                        ],
                        [
                            37.307724952697754,
                            55.64024152130109
                        ],
                        [
                            37.307724952697754,
                            55.63619642594767
                        ],
                        [
                            37.29836940765381,
                            55.63619642594767
                        ]
                    ]
                ]
            },
            "area": 265197,
            "messages": []
        }
    ]


Downloading processing results
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``GET https://api.mapflow.ai/rest/processings/{processingId}/result``

Returns Geojson results of this processing as an octet stream. Should only be called on a successfully completed processing.


Upload images
----------------------------

.. warning::
   This is the legacy method and is going to be deprecated. Use the new :ref:`Data API` instead.

``POST https://api.mapflow.ai/rest/rasters``

Can be used to upload a raster for further processing. Returns url to the uploaded raster. This url can be referenced when starting a processing.  
The request is a multipart request whith the only part "file" - which contains the raster.
Request example with ``cURL``:  

    .. code:: bash

          curl -X POST \
          https://api.mapflow.ai/rest/rasters \
          -H 'authorization: <Insert auth header value>' \
          -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
          -F file=@custom_raster.tif



Response example:  

``{"url": "s3://mapflow-rasters/9764750d-6047-407e-a972-5ebd6844be8a/raster.tif"}``



Parameter values
----------------

Default AI models
^^^^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 10 20 10
   :header-rows: 1

   * - VALUE
     - DESCRIPTION
     - MODEL resolution (m/px), num of input bands
   * - 🏠 Buildings
     - Detects buildings & classifies them
     - 0.5, 3 (RGB)
   * - 🌲 Forest
     - Detects tree-like vegetation
     - 2, 3 (RGB)
   * - 🚗 Roads
     - Detects roads and returns them as polygons / linestrings
     - 1, 3 (RGB)
   * - 🚜 Fields (hi-res)
     - Detects cropland fields
     - 0.5, 3 (RGB)
   * - 🚜 Fields (Sentinel-2)
     - Detects cropland fields using free Sentinel-2 imagery
     - 10 m/px, 10 (multispectral)
   * - 🏗️ Construction
     - Detects cropland fields
     - 0.5, 3 (RGB)


source_type
^^^^^^^^^^^^^^^^^^^
.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - VALUE
     - DESCRIPTION
   * - XYZ
     - The URL to the imagery service in “xyz” format, e.g. `https://tile.openstreetmap.org/{z}/{x}/{y}.png <https://tile.openstreetmap.org/{z}/{x}/{y}.png>`_
   * - TMS
     - The similar to "xyz" with reverse "y" coordinate
   * - WMS
     - (❗️❗️Deprecated) The URL to the imagery service in “wms” format, e.g. `https://services.nationalmap.gov/arcgis/services/ USGSNAIPImagery/ImageServer/WMSServer <https://services.nationalmap.gov/arcgis/services/USGSNAIPImagery/ImageServer/WMSServer>`_
   * - Quadkey
     - The one-dimensional index key that usually preserves the proximity of tiles in "xy" space (Bing Maps tile format)
   * - tif/tiff
     - File of image in georeferenced tiff (GeoTIFF) format


status
^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - VALUE
     - Description
   * - UNPROCESSED
     - The processing is not started yet
   * - IN_PROGRESS
     - The processing is going (or is in the queue)
   * - FAILED
     - The processing ended unsuccessfuly - change wrong params or try to restart
   * - OK
     - The processing is finished at 100 percent completed      



.. include:: error_messages.rst