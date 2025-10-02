.. _Processing API:

Mapflow processing API
========================

.. attention::
    The projects and processings that you create in `Mapflow.ai <https://app.mapflow.ai/>`_  **will be available** via the API and vice versa. Also, your Mapflow credits are used to run processings via the API. Use the API token to start using the API, which you need to generate in the `profile settings <https://app.mapflow.ai/account>`_ (see :doc:`authorization to work with the Mapflow API <../userguides/mapflow_auth>`).

.. important::
    You should follow the requirements specified on the page with :doc:`the description of models <../userguides/pipelines>` when uploading your own images for processing through the API of the Mapflow platform. Send a request using data preprocessing to help@geoalert.io.


User
-------

Get user status
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns user status for the given user account, including:
  - User limits
  - Default and custom :ref:`Models` (every User account is connected to the default models, yet specific models have to be linked to the User account by request)
  - Default and custom :ref:`Imagery` (every User account is linked to the default data providers, yet specific commercial providers have to be linked to the User account by request)

If user account is added to the :ref:`Team accounts` - it returns Team's description as well


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
              "description": "Buildings detection and mapping",
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
              "name": "My New Team",
              "role": "OWNER",
              "activeUntil": null,
              "creditsLimit": null
          }
      ]
  }


Obtain processing statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``POST https://api.mapflow.ai/rest/processings/stats``

Returns user's processing history with details. This method supports filters by date, status, etc.
If the user is a :ref:`Team's <Team accounts>` owner, this returns the statistics by all team members.

Params for processing stats:

.. list-table::
   :widths: 30 30 30
   :header-rows: 0

   * - Type
     - JSON
     - Returns stats in structured JSON

.. list-table::
   :widths: 30 20 40
   :header-rows: 1

   * - Filter
     - Type
     - Description
   * - dateFrom, dateTo
     - DATETIME
     - Filters by date-time
   * - statuses
     - ARRAY
     - Filters by statuses ["OK", "IN_PROGRESS", "FAILED", "CANCELED", "REFUNDED"]
   * - terms
     - STRING
     - Filters by arbitrary string value


Sample request:

.. code:: bash

  curl --location 'https://api.mapflow.ai/rest/processings/stats?type=JSON' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Basic <YOUR TOKEN>' \
  --data '{"dateFrom":"2024-11-07T21:00:00.000Z","dateTo":"2025-02-24T21:59:59.999Z","statuses":["OK"]}'

Sample response:

.. code:: json

      {
        "results": [
            {
                "projectName": "Test,
                "name": "test_proc",
                "email": "user1@geoalert.io",
                "area": "536680",
                "cost": "0",
                "created": "2025-02-24T13:34:34.640553Z",
                "completionDate": "2025-02-24T13:35:31.327948Z",
                "status": "OK",
                "percentCompleted": "100",
                "archived": "false",
                "dataProvider": null,
                "linkToMap": "https://app.mapflow.ai/projects/c77bad4b-6a2b-49ed-8af4-4d1841aec771/processings/893bcc22-8a3b-47d5-8e56-0d0a83fab25d",
                "scenario": "🏠 Buildings"
            },
            {
                "projectName": "Test new model NSPD",
                "name": "test_proc2",
                "email": "user2@geoalert.io",
                "area": "450102",
                "cost": "0",
                "created": "2025-02-24T13:37:55.581373Z",
                "completionDate": "2025-02-24T13:38:22.078667Z",
                "status": "OK",
                "percentCompleted": "100",
                "archived": "false",
                "dataProvider": null,
                "linkToMap": "https://app.mapflow.ai/projects/c77bad4b-6a2b-49ed-8af4-4d1841aec771/processings/6ecbd6ae-32cd-499a-aa42-fd0e67d6f9b6",
                "scenario": "🏠 Buildings"
            }
        ],
        "total": 2,
        "count": 2,
        "totalCost": 0,
        "totalArea": 986782
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


Share project
^^^^^^^^^^^^^^^^
``POST https://api.mapflow.ai/rest/projects/share``

Share project with the external or a team user depending on the contribution rights.

1. Share project with the external user:

.. code:: json
  
    {
        "projectId": "70f65cfd-285b-4f25-a058-1fd9103a78f9",
        "email": "some-external-user@email.com",
        "role": "readonly"
    }

2. Share project with the :ref:`team <Team accounts>` user
  
.. code:: json

    {
        "projectId": "70f65cfd-285b-4f25-a058-1fd9103a78f9",
        "email": "team-user@myteam.com",
        "role": "contributor"
    }

User role parameter:

.. note::

    The "readonly" role is applicable for any user. The "contributor+" role is applicable for sharing projects inside the :ref:`team <Team accounts>`.

  .. list-table::
    :widths: 10 10 50
    :header-rows: 1
   
    * - KEY
      - VALUE
      - DESCRIPTION
    * - role
      - readonly
      - User can view project, download results but can't create and run processing.
    * - role
      - contributor
      - User can view project, download results and create and run processing.
    * - role
      - maintainer
      - User can view project, download results, create, run and delete processing + share project.
    * - role
      - owner
      - User can do everything above + assign and remove the project owner.

Delete project
^^^^^^^^^^^^^^^^^^^

``DELETE https://api.mapflow.ai/rest/projects/{projectId}`` 

Deletes the project. Cascade deletes any child entities.

Processings
------------

Processing API v2
^^^^^^^^^^^^^^^^^^^

Get all processings
""""""""""""""""""""

``GET https://api.mapflow.ai/rest/processings/v2``

Returns the list of the user’s processings by the Default project

Get all processings by Project Id
""""""""""""""""""""""""""""

``GET https://api.mapflow.ai/rest/projects/{projectId}/processings/v2``

Returns the list of the user’s processings by user’s project


Get processing by Id v2
""""""""""""""""""""

``GET https://api.mapflow.ai/rest/processings/{processingId}/v2``

Returns the processing with the specified id.

**Response Example:**

.. code:: json

    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "string",
      "description": "string",
      "projectId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "vectorLayer": {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "name": "string",
        "tileJsonUrl": "string",
        "tileUrl": "string"
      },
      "rasterLayer": {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "tileJsonUrl": "string",
        "tileUrl": "string"
      },
      "workflowDef": {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "name": "string",
        "description": "string",
        "created": "2025-10-01T20:05:21.819Z",
        "updated": "2025-10-01T20:05:21.819Z",
        "pricePerSqKm": 0,
        "blocks": [
          {
            "name": "string",
            "description": "string",
            "optional": 0,
            "price": 0
          }
        ]
      },
      "aoiCount": 0,
      "area": 0,
      "cost": 0,
      "status": "UNPROCESSED",
      "reviewStatus": {
        "reviewStatus": "ACCEPTED",
        "feedback": "2025-10-01T20:05:21.819Z"
      },
      "rating": {
        "rating": "string",
        "feedback": "string"
      },
      "percentCompleted": 0,
      "params": {
        "sourceParams": {
          // NOTE: Only ONE of the following source types should be used:
          "myImagery": {              // Use your uploaded imagery
            "imageIds": [
              "string"
            ],
            "mosaicId": "string"
          },
          "imagerySearch": {          // Use imagery from search
            "dataProvider": "orbview",
            "imageIds": [
              "string"
            ],
            "zoom": 0
          },
          "dataProvider": {           // Use data provider directly
            "providerName": "string",
            "zoom": 0
          },
          "userDefined": {            // Use custom imagery source
            "sourceType": "XYZ",
            "url": "string",
            "zoom": 0,
            "crs": "string",
            "rasterLogin": "string",
            "rasterPassword": "string"
          }
        },
        "inferenceParams": {
          "key1": "value1",
          "key2": "value2",
          "keyN": "valueN"
        }
      },
      "blocks": [
        {
          "name": "string",
          "enabled": true
        }
      ],
      "meta": {
        "key1": "value1",
        "key2": "value2",
        "keyN": "valueN"
      },
      "messages": [
        {
          "code": "string",
          "parameters": {
            "key": "string",
            "value": "string"
          }
        }
      ],
      "created": "2025-10-01T20:05:21.819Z",
      "updated": "2025-10-01T20:05:21.819Z"
    }

**Response Codes:**


Create and run processing v2
""""""""""""""""""""""""""""

``POST https://api.mapflow.ai/rest/processings/v2``

Creates and runs a new processing with enhanced v2 parameters and configuration options.

**Request Body:**

.. code:: json

    {
      "name": "string",
      "description": "string",
      "projectId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "wdName": "string",
      "wdId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "geometry": {
        "coordinates": [
          [
            [
              0,
              0
            ]
          ]
        ]
      },
      "params": {
        "sourceParams": {
          // NOTE: Only ONE of the following source types should be used:
          "myImagery": {              // Use your uploaded imagery
            "imageIds": [
              "string"
            ],
            "mosaicId": "string"
          },
          "imagerySearch": {          // Use imagery from search
            "dataProvider": "orbview",
            "imageIds": [
              "string"
            ],
            "zoom": 0
          },
          "dataProvider": {           // Use data provider directly
            "providerName": "string",
            "zoom": 0
          },
          "userDefined": {            // Use custom imagery source
            "sourceType": "XYZ",
            "url": "string",
            "zoom": 0,
            "crs": "string",
            "rasterLogin": "string",
            "rasterPassword": "string"
          }
        },
        "inferenceParams": {
          "key1": "value1",
          "key2": "value2",
          "keyN": "valueN"
        }
      },
      "meta": {
        "key1": "value1",
        "key2": "value2",
        "keyN": "valueN"
      },
      "blocks": [
        {
          "name": "string",
          "enabled": true
        }
      ]
    }

**Response Example:**

.. code:: json

    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "string",
      "description": "string",
      "projectId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "vectorLayer": {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "name": "string",
        "tileJsonUrl": "string",
        "tileUrl": "string"
      },
      "rasterLayer": {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "tileJsonUrl": "string",
        "tileUrl": "string"
      },
      "workflowDef": {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "name": "string",
        "description": "string",
        "created": "2025-10-01T20:05:56.690Z",
        "updated": "2025-10-01T20:05:56.690Z",
        "pricePerSqKm": 0,
        "blocks": [
          {
            "name": "string",
            "description": "string",
            "optional": 0,
            "price": 0
          }
        ]
      },
      "aoiCount": 0,
      "area": 0,
      "cost": 0,
      "status": "UNPROCESSED",
      "reviewStatus": {
        "reviewStatus": "ACCEPTED",
        "feedback": "2025-10-01T20:05:56.690Z"
      },
      "rating": {
        "rating": "string",
        "feedback": "string"
      },
      "percentCompleted": 0,
      "params": {
        "sourceParams": {
          "myImagery": {
            "imageIds": [
              "string"
            ],
            "mosaicId": "string"
          },
          "imagerySearch": {
            "dataProvider": "orbview",
            "imageIds": [
              "string"
            ],
            "zoom": 0
          },
          "dataProvider": {
            "providerName": "string",
            "zoom": 0
          },
          "userDefined": {
            "sourceType": "XYZ",
            "url": "string",
            "zoom": 0,
            "crs": "string",
            "rasterLogin": "string",
            "rasterPassword": "string"
          }
        },
        "inferenceParams": {
          "key1": "value1",
          "key2": "value2",
          "keyN": "valueN"
        }
      },
      "blocks": [
        {
          "name": "string",
          "enabled": true
        }
      ],
      "meta": {
        "key1": "value1",
        "key2": "value2",
        "keyN": "valueN"
      },
      "messages": [
        {
          "code": "string",
          "parameters": {
            "key": "string",
            "value": "string"
          }
        }
      ],
      "created": "2025-10-01T20:05:56.690Z",
      "updated": "2025-10-01T20:05:56.690Z"
    }

**Response Codes:**


Calculate processing cost v2
""""""""""""""""""""""""""""

``POST https://api.mapflow.ai/rest/processing/cost/v2``

Calculate processing cost v2 with enhanced parameters and configuration options.

**Request Body:**

.. code:: json

    {
      "wdId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "geometry": {
        "coordinates": [
          [
            [
              0,
              0
            ]
          ]
        ]
      },
      "areaSqKm": 0,
      "params": {
        "sourceParams": {
          "myImagery": {
            "imageIds": [
              "string"
            ],
            "mosaicId": "string"
          },
          "imagerySearch": {
            "dataProvider": "orbview",
            "imageIds": [
              "string"
            ],
            "zoom": 0
          },
          "dataProvider": {
            "providerName": "string",
            "zoom": 0
          },
          "userDefined": {
            "sourceType": "XYZ",
            "url": "string",
            "zoom": 0,
            "crs": "string",
            "rasterLogin": "string",
            "rasterPassword": "string"
          }
        },
        "inferenceParams": {
          "key1": "value1",
          "key2": "value2",
          "keyN": "valueN"
        }
      },
      "blocks": [
        {
          "name": "string",
          "enabled": true
        }
      ],
      "meta": {
        "key1": "value1",
        "key2": "value2",
        "keyN": "valueN"
      }
    }

**Response Example:**

.. code:: json

    1

Processing API v1
^^^^^^^^^^^^^^^^^^^

Get all processings
""""""""""""""""""""

``GET https://api.mapflow.ai/rest/processings``

Returns the list of the user's processings by the Default project

Get all processings by Project Id
"""""""""""""""""""""""""""""""""""

``GET https://api.mapflow.ai/rest/projects/{projectId}/processings``

Returns the list of the user's processings by user's project

Get processing by Id
""""""""""""""""""""

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
          "url": "https://app.mapflow.ai/api/v0/cogs/tiles/{z}/{x}/{y}.png?uri=s3://white-maps-rasters/0617c425-9bfa-45a3-b2ea-46020e48d775",
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
      "status": "FAILED",
      "percentCompleted": 0,
      "messages": [
        {
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


Processing cost
""""""""""""""""

``POST https://api.mapflow.ai/rest/processing/cost``

To find out the cost of processing without running it, you can use this method.
Returns the cost of the processing in :ref:`credits <credits>` given the model, the area and the data source.

Request body example:

.. code:: json

  {
    "wdId": "8cb13006-a299-4df6-b47d-91bd63de947f", 
    "geometry": {
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
    "params": {
    "data_provider": "Mapbox"
    }
  }

Response example:

``30``

.. note::

  You can find out the details like workflow definition ``ID`` (``wdId``) using this method:
  
  ``GET api.mapflow.ai/rest/user/status``


.. _Create processing:

▶️ Run the processing
""""""""""""""""""""""

``POST https://api.mapflow.ai/rest/processings``

Runs an imagery analysis processing, and returns its immediate state.
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
        "params": {                           //Arbitrary string parameters of this processing. Optional.
            "sourceParams": {
                "dataProvider": {
                    "providerName": "Mapbox",
                    "zoom": 18 // optional
                }
            }
        },
        "meta": {                             //Arbitrary string key-value for this processing (metadata). Optional.
            "test": "test"
        }
    }

.. note::



  To process a user-provided image (see :ref:`Upload image <upload-images>` section), set parameters as follows:  

  .. code:: json

          "params": {
              "source_type": "local",
              "url": "s3://users-data/user@email.com_eaf9e720-c6de-4d9b-8aec-52296d43f0c4/1e7fc660-7d0a-4632-9e6c-e95cf20e62b9/b97e9154-a356-450c-990b-fb1692d404ec.tif"
          }


Response: the newly created processing.



Customize processing with the options
""""""""""""""""""""""""""""""""""""""

``POST https://api.mapflow.ai/rest/processings``

Processing workflow can be customized with enabling or disabling some model options.  The number of options depends on the model and a scenario. 

Request body example

.. code:: json
  
  {
      "blocks": [
          {
              "name": "Simplification",
              "enabled": false
          },
          {
              "name": "Classification",
              "enabled": true
          }
      ]
  }

The "options" can be retrieved for every model in the ``models`` linked to the user – through the ``user/status`` request. 

Response example:

.. code:: json

        "models": 
        [

            {
                "id": "c2e857fe-1bf6-4e7a-b9f4-d5339c46d357",
                "name": "Forest",
                "description": "Default model: segmentation of forested areas with assinment of height classes; thresholds are 4 and 10 meters",
                "created": "2023-07-26T08:14:18.739968Z",
                "updated": "2023-08-11T04:58:40.907896Z",
                "pricePerSqKm": 0.0,
                "blocks": [
                    {
                        "name": "Segmentation",
                        "displayName": "Segmentation",
                        "optional": false,
                        "price": 8.0
                    },
                    {
                        "name": "Heights",
                        "displayName": "Height estimation",
                        "optional": true,
                        "price": 20.0
                    }
                ]
            }
        ]



Rename processing
"""""""""""""""""

``PUT https://api.mapflow.ai/rest/processing/{processingId}``

Request body example:

.. code:: json

    {
      "name": "new name (optional)",
      "description": "new description (optional)"
    }


Restart processing
""""""""""""""""""

``POST https://api.mapflow.ai/rest/processings/{processingId}/restart``

Restarts failed partitions of this processing. Doesn't restart non-failed partitions. Each workflow is restarted from the first failed stage. Thus, the least possible amount of work is performed to try and bring the processing into successful state.

Link processing to another project
"""""""""""""""""""""""""""""""""""

``PUT https://api.mapflow.ai/rest/processings/{processing_id}``

Links processing to another project by project ID

.. code:: bash
  
  curl --location --request PUT 'https://api.mapflow.ai/rest/processings/{processing_id}' \ 
  --header 'Content-Type: application/json' \ 
  --header 'Authorization: Basic <YOUR TOKEN>' \ 
  --data-raw '{"projectId": "new_project_id"}'

Delete processing
"""""""""""""""""

``DELETE https://api.mapflow.ai/rest/processings/{processingId}``

Deletes this processing. Cascade deletes any child entities.

Get processing AOIs
"""""""""""""""""""

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
"""""""""""""""""""""""""""""""

``GET https://api.mapflow.ai/rest/processings/{processingId}/result``

Returns Geojson results of this processing as an octet stream. Should only be called on a successfully completed processing.


.. _upload-images:

Upload images
"""""""""""""

.. note::

  1. ❗️ Use :ref:`Data API` to create a mosaic and upload one or more images
  2. Use s3 link from the ``"image_url"`` as an ``"url"`` param to :ref:`Create processing`


Reference
"""""""""

✍️ Params to run the processing
""""""""""""""""""""""""""""""""

.. csv-table::
    :file: _static/csv/params_run.csv
    :widths: 30, 20, 80
    :header-rows: 1
    :class: longtable


✍️ Params to specify the data source
""""""""""""""""""""""""""""""""""""

.. csv-table::
    :file: _static/csv/params_ds.csv
    :widths: 30, 20, 60, 40
    :header-rows: 1
    :class: longtable

**Create new processing with default Data provider**

.. code:: json

      "params": {
        "sourceParams": {
            "dataProvider": {
                "providerName": "Mapbox",
                "zoom": 18 // optional
            }
        }
    }


**Create new processing with User custom URl**

.. code:: json
  
      "params": {
        "sourceParams": {
            "userDefined": {
                "url": "https://app.mapflow.ai/api/v0/cogs/tiles/{z}/{x}/{y}.png?uri=s3://white-maps-rasters/0617c425-9bfa-45a3-b2ea-46020e48d775",
                "sourceType": "XYZ",
                "zoom": 19, // optional
                "crs": "epsg:3857", // optional
                "rasterLogin": "qwerty", // optional
                "rasterPassword": "12345678" // optional
            }
        }
    }

**Create new processing with My Imagery (Image collection)**

.. code:: json

      "params": {
        "sourceParams": {
            "myImagery": {
                "mosaicId": "0617c425-9bfa-45a3-b2ea-46020e48d775"
            }
        }
    }


**Create new processing with My Imagery (single Image)**

.. code:: json

      "params": {
        "sourceParams": {
            "myImagery": {
                "imageIds": ["0c26a0d3-96d8-4ed5-aa62-3843d1d7905c"]
            }
        }
    }


✍️ Params to specify the "source_type"
""""""""""""""""""""""""""""""""""""""""

.. list-table::
   :widths: 10 30
   :header-rows: 1

   * - VALUE
     - DESCRIPTION
   * - XYZ
     - The URL to the imagery service in “xyz” format
   * - TMS
     - The similar to "xyz" with reverse "y" coordinate
   * - WMS
     - (❗️❗️Deprecated) The URL to the imagery service in “wms” format
   * - Quadkey
     - The one-dimensional index key that usually preserves the proximity of tiles in "xy" space (Bing Maps tile format)
   * - local
     - File of image in GeoTIFF format


✍️ Default AI models
"""""""""""""""""""""

.. list-table::
   :widths: 10 20 10 10 20
   :header-rows: 1

   * - VALUE
     - DESCRIPTION
     - MODEL input (m/px), num of bands
     - ZOOM LEVEL
     - OPTIONS
   * - 🏠 Buildings
     - Detects buildings & classifies them
     - 0.5, 1-3 (RGB)
     - 17–18
     - Simplification, OSM, Classification
   * - 🌲 Forest
     - Detects tree-like vegetation
     - 0.5, 3 (RGB)
     - 17-18
     - Heights
   * - 🚗 Roads
     - Detects roads and returns them as polygons / linestrings
     - 0.5, 3 (RGB)
     - 17–18
     - 
   * - 🏗️ Construction
     - Detects construction sites
     - 0.5, 3 (RGB)
     - 17–18
     - 


✍️ Processing status
""""""""""""""""""""

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
   * - *IN_REVIEW*
     - The additional status enabled by request (if the results are under review)


.. include:: error_messages.rst