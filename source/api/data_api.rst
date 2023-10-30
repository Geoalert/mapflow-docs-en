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
    The API aims to perform as a middle-tear between multiple imagery source and a :doc:`Mapflow Processing API <processing_api>`.
    The API returns the search results by the imagery providers linked to the specific user. 
    If no provider is linked to the user it returns all providers available. To run the processing one needs to get the provider linked to his user account. 

Get metadata of available images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``POST https://api.mapflow.ai/catalog/meta``

``type: application/json``


Returns a list of the available images, filtered by metadata. 

E.g.:

.. code:: json

    {
        "aoi": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        69.1618,
                        41.2105
                    ],
                    [
                        69.1618,
                        41.3784
                    ],
                    [
                        69.3716,
                        41.3784
                    ],
                    [
                        69.3716,
                        41.2105
                    ],
                    [
                        69.1618,
                        41.2105
                    ]
                ]
            ]
        },
        "acquisitionDateFrom": "2023-10-01T00:00:00Z",
        "acquisitionDateTo": "2022-10-10T00:00:00Z",
        "maxCloudCover": 0.1,
        "maxResolution": 0.5,
        "minResolution": 0.3
    }

Response example:

.. code:: json

    {
        "images": [
            {
                "id": "JL1GF03D15_PMS_20230913140838_200196307_108_0001_001_L1",
                "footprint": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                69.2325,
                                41.5352
                            ],
                            [
                                69.3602,
                                41.5151
                            ],
                            [
                                69.3182,
                                41.3647
                            ],
                            [
                                69.1906,
                                41.3848
                            ],
                            [
                                69.2325,
                                41.5352
                            ]
                        ]
                    ]
                },
                "pixelResolution": 0.0,
                "acquisitionDate": "2023-09-13T14:08:40Z",
                "productType": "A",
                "sensor": "JL1GF03D15",
                "colorBandOrder": "unknown",
                "cloudCover": 0.0,
                "offNadirAngle": -12.49,
                "previewType": "png",
                "previewUrl": "https://home.sat-imagery.com/geoserver/rs_data/wms?SERVICE=WMS&VERSION=1.1.0&REQUEST=GetMap&FORMAT=image%2Fpng&TRANSPARENT=true&LAYERS=rs_data%3AJL1GF03D15_PMS_20230913140838_200196307_108_0001_001_L1&STYLES=&serverType=geoserver&crossOrigin=anonymous&tiled=false&angle=0&WIDTH=188&HEIGHT=253&SRS=EPSG%3A3857&BBOX=7702262.3596810745%2C5066284.571753241%2C7721142.145319615%2C5091606.951481916",
                "providerName": "sat_imagery"
            }
        ]
    }

.. note::

   | ``aoi``: geometry, - required, Geojson-like Polygon or Multipolygon
   | ``acquisitionDateFrom``: UTC time string 
   | ``acquisitionDateTo``: UTC time string
   | ``minResolution``: float, in meters
   | ``maxResolution``: float, in meters
   | ``maxCloudCover``: float, in percents 
   | ``minOffNadirAngle``: float, in degrees
   | ``maxOffNadirAngle``: float, in degrees
   | ``minAoiIntersectionPercent``: float, in percents

.. warning::
    The size of the search area cannot exceed the size of processing AOI limit assigned to the specific user.


Run processing by image ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For detailed description how to run a processing with Mapflow API see :doc:`Mapflow Processing API <processing_api>` – "Create processing".
To run a processing using the specific image returned by Search API define **provider** and **image ID** in the params as follows:

``{"params": {"data_provider":<providerName>, "url":<id>}}``


