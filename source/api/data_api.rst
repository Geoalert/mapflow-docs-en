.. _Data API:

Mapflow Data API
==================

.. note::
    .. figure:: _static/postman_logo.png
       :alt: Preview results
       :align: left
       :width: 1cm

   Check and run this `Postman collection for API <https://documenter.getpostman.com/view/5400715/2s935hS7ky>`_.

.. note::
    Data API allows to manage your imagery, organise it into collections (mosaics), reuse for processings with Mapflow and preview them as XYZ layers.
    👉 To use the imagery processing API see :doc:`this documentation <processing_api>`
 

Manage Imagery Mosaics
-------------------------

.. note::
    What is "mosaic"? This is the collection of single images, aimed at instant preview and processing. It's helpful in such cases as mosaicing the number of single aerial images covering some area or batching the large ortho-plan for faster uploading and optimizing its storage in the cloud.


Create mosaic
^^^^^^^^^^^^^^^

``POST https://api.mapflow.ai/rest/rasters/mosaic`` 

Creates the mosaic (the empty collection of images) and returns its ID.

.. code:: bash

    curl --location --request POST 'https://api.mapflow.ai/rest/rasters/mosaic' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Basic <YOUR TOKEN>' \
    --data-raw '{
    "name": "mosaic-name",
    "tags": [
        "tag-1",
        "tag-2"
        ]
    }'

Creates mosaic and uploads images to the mosaic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: bash

    curl --location -g --request POST 'https://api.mapflow.ai/rest/rasters/mosaic/mosaic?name={name}&tags={tag1}&tags={tag2}' \
    --header 'Content-Type: multipart/form-data' \
    --header 'Authorization: Basic <YOUR TOKEN>' \
    --form 'file=@"/path/to/file"'


Get mosaic
^^^^^^^^^^^^^^^

``GET https://api.mapflow.ai/rest/rasters/mosaic/{mosaic_id}`` 


Update mosaic
^^^^^^^^^^^^^^^

.. code:: bash

    curl --location --request PUT 'https://api.mapflow.ai/rest/rasters/mosaic/{mosaic_id}' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Basic <YOUR TOKEN>' \
    --data-raw '{
    "name": "new-mosaic-name",
    "tags": [
        "new-tag-1",
        "new-tag-2"
        ]
    }'

Upload images to the existing mosaic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::
    ⚠️ The uploaded images are required to have the same georeference system, number of bands, and spatial resolution.   

``POST https://api.mapflow.ai/rest/rasters/mosaic/{mosaic_id}/image`` 


Link image to the existing mosaic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``POST https://api.mapflow.ai/rest/rasters/mosaic/{mosaic_id}/link-image``

.. code:: bash

    curl --location -g --request POST 'https://api.mapflow.ai/rest/rasters/mosaic/{mosaic_id}/link-image' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Basic <YOUR TOKEN>' \
    --data-raw '{
    "url": "s3://users-data/user@email.com_045b8085-0ab8-42dc-8c65-c366cbaab5e0/8b6e9f1e-8ee6-4c15-9b39-c3bd6431f3f6/cog/area-5911389.tif"
    }'

Response example:

.. code:: json

    {
    "message": "File successfully linked to a mosaic",
    "mosaic_id": "6ee95ae6-f26e-41bd-8cb1-39bea545119f"
    }


Delete mosaic
^^^^^^^^^^^^^^^

.. attention::
    Deleting mosaic also deletes all linked images and they cannot be restored


``DELETE https://api.mapflow.ai/rest/rasters/mosaic/{mosaic_id}`` 


Manage Images
---------------

Get image metadata by image ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``GET https://api.mapflow.ai/rest/rasters/image/{image_id}``

Delete image
^^^^^^^^^^^^^^^

``DELETE https://api.mapflow.ai/rest/rasters/image/{image_id}``

Get image preview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``GET https://api.mapflow.ai/rest/rasters/{image_id}/preview/{preview_type}``

E.g.:

.. code:: bash

    curl --location --request GET 'https://api.mapflow.ai/rest/rasters/image/{image_id}/preview/s' \
    --header 'Content-Type: image/jpg' \
    --header 'Authorization: Basic <YOUR TOKEN>'

Response example:

.. image:: _static/data_api/response_preview_s.jpeg
    :alt: Image preview 
    :align: left


.. list-table::
    :widths: 10 20
    :header-rows: 1

    * - PREVIEW TYPE
      - DESCRIPTION
    * - s
      - image 256x256
    * - l
      - image 1024x1024


.. attention::
    Mapflow Storage

Get user's storage limits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``GET https://api.mapflow.ai/rest/rasters/memory``

This method allows to check user's storage usage against the available limit.



Search Imagery
----------------

.. note::
    This is the early version of the Mapflow API to search for available satellite images provided by external data providers.
    The API aims to perform as a middle-tear between multiple data source and a :doc:`Mapflow Processing API <processing_api>`.

Get metadata of available images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``POST https://api.mapflow.ai/catalog/meta``

Returns a list of the images in GeoJSON, filtered by metadata. E.g.:

.. code:: json

      { "aoi": {
              "type": "Polygon",
              "coordinates": [
                [
                  [
                    37.34396696090698,
                    55.6731196654679
                  ],
                  [
                    37.35926628112793,
                    55.6731196654679
                  ],
                  [
                    37.35926628112793,
                    55.67997991819218
                  ],
                  [
                    37.34396696090698,
                    55.67997991819218
                  ],
                  [
                    37.34396696090698,
                    55.6731196654679
                  ]
                ]
              ]
          },
        "acquisitionDateFrom": "2021-01-01T00:00:00Z", 
        "acquisitionDateTo": "2022-01-01T00:00:00Z",
        "maxCloudCover": 0.1,
        "maxResolution": 0.31,
        "minResolution": 0.3
      }


Response example:

.. code:: json

    { "images": [
            {
                "id": "a518230a236664891bfb2d8041028a59",
                "footprint": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                37.2883723,
                                55.96500262
                            ],
                            [
                                37.3950109,
                                55.96416162
                            ],
                            [
                                37.50164951,
                                55.96332062
                            ],
                            [
                                37.50141629,
                                55.72561772
                            ],
                            [
                                37.50118307,
                                55.48791481
                            ],
                            [
                                37.39506886,
                                55.48708936
                            ],
                            [
                                37.28895464,
                                55.48626391
                            ],
                            [
                                37.28866347,
                                55.72563326
                            ],
                            [
                                37.2883723,
                                55.96500262
                            ]
                        ]
                    ]
                },
                "pixelResolution": 0.31,
                "acquisitionDate": "2021-07-07T08:42:03Z",
                "productType": "Pan Sharpened Natural Color",
                "sensor": "WV03_VNIR",
                "colorBandOrder": "RGB",
                "cloudCover": 0.0,
                "offNadirAngle": 6.471679
            }
        ]
    }

``aoi`` (required) - the geometry of the area (GeoJSON, Lat Lon coordinates) to search imagery for. Currently the only type ``Polygon`` is supported.

.. important::

    The size of the area cannot exceed the size of processing AOI limit assigned to the specific user.

``acquisitionDateFrom`` <> ``acquisitionDateTo`` (optional) - date/time format in UTC time zone according to ISO-8601. Determines the time range that the imagery acquisition date corresponds to.

``maxCloudCover`` (optional) - maxCloudCover — optional, a decimal number in the range 0 - 1 (corresponds to 0-100% cloud coverage). This parameter defines the maximum area of an image (in pixels) that was classified as covered by clouds.

``maxResolution`` - optional, defines the maximum allowed resolution in m / pixel

``minResolution`` - optional, defines the minimum allowed resolution in m / pixel


Get metadata by image ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``GET https://api.mapflow.ai/rest/catalog/meta/{image_id}``

.. code:: bash

    curl --location --request GET 'https://api.mapflow.ai/rest/catalog/meta/{image_id}' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Basic <YOUR TOKEN>'

You can get ``image_id`` from ``processing.params.url``


