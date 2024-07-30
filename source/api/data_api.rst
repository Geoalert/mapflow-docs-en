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
    What is "mosaic"? This is the collection of images, aimed at instant preview and processing. It's helpful in such cases as collecting and mosaicing the number of single aerial images covering some area or batching the large orthomap for faster uploading and optimizing its storage in the cloud.


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

Create mosaic and upload images to mosaic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


Get images by mosaic ID
^^^^^^^^^^^^^^^^^^^^^^^^^^

``GET https://api.mapflow.ai/rest/rasters/mosaic/{mosaic_id}\image``

Response example:

.. code:: json

    [
        {
            "id": "6ae7f9e9-da2d-41e0-b16f-83396003af57",
            "image_url": "s3://users-data/user@email.com_eaf9e720-c6de-4d9b-8aec-52296d43f0c4/90fe01b2-8c21-4d5b-9d4f-143b05d3e986/6ae7f9e9-da2d-41e0-b16f-83396003af57.tif",
            "preview_url_l": "https://api.mapflow.ai/rest/rasters/image/6ae7f9e9-da2d-41e0-b16f-83396003af57/preview/l",
            "preview_url_s": "https://api.mapflow.ai/rest/rasters/image/6ae7f9e9-da2d-41e0-b16f-83396003af57/preview/s",
            "uploaded_at": "2023-01-26T13:58:32.122099",
            "file_size": 68417439,
            "footprint": "POLYGON ((1.991514383583533 48.76433046008412, 1.991514383583533 48.77553902852908, 1.968476220399751 48.77553902852908, 1.968476220399751 48.76433046008412, 1.991514383583533 48.76433046008412))",
            "filename": "bd8b9969505748898adac2cfa80d3425.tif",
            "checksum": "9d2d9e9bd347fc5204e5fd1add0982aadff21f17",
            "meta_data": {
                "crs": "EPSG:32631",
                "count": 3,
                "width": 5589,
                "dtypes": [
                    "uint8",
                    "uint8",
                    "uint8"
                ],
                "height": 4079,
                "nodata": null,
                "pixel_size": [
                    0.3000000000000021,
                    0.3000000000000457
                ]
            },
            "cog_link": "s3://users-data/user@email.com_eaf9e720-c6de-4d9b-8aec-52296d43f0c4/90fe01b2-8c21-4d5b-9d4f-143b05d3e986/cog/area-1101712.tif"
        }
    ]


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



🔍 Search Imagery
------------------

.. note::
    This is an early version of the Mapflow unified API to search for available satellite images provided by external data providers.
    The API aims to perform as a middle-tear between multiple imagery source and a :doc:`Mapflow Processing API <processing_api>`.
    The API returns the search results for the imagery providers linked to the specific Mapflow user. 
    If no provider is linked to the user it returns all providers results available. But to run the processing the user needs to get the provider linked to his account. 

Get metadata of available images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``POST https://api.mapflow.ai/catalog/meta``


Returns a list of the available images, filtered by metadata keys. 

E.g. request:

.. code:: bash

    curl --location 'https://api.mapflow.ai/rest/catalog/meta' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Basic ******' \
    --data '{
    "aoi": {
            "type": "Polygon",
            "coordinates": [[[76.6755,43.2234],[76.6755,43.4712],[77.0163,43.4712],[77.0163,43.2234],[76.6755,43.2234]]]
        },
    "acquisitionDateFrom": "2022-04-01T00:00:00Z", 
    "acquisitionDateTo": "2022-11-01T00:00:00Z",
    "maxCloudCover": 0.1,
    "maxResolution": 0.5,
    "minResolution": 0.3
    }'

.. note::

   | ``aoi``: geometry, - required, Geojson-like Polygon or Multipolygon of the area of the search
   | ``acquisitionDateFrom``: UTC time string 
   | ``acquisitionDateTo``: UTC time string
   | ``minResolution``: float, in meters
   | ``maxResolution``: float, in meters
   | ``maxCloudCover``: float, in percents 
   | ``minOffNadirAngle``: float, in degrees
   | ``maxOffNadirAngle``: float, in degrees
   | ``minAoiIntersectionPercent``: float, in percents – minimum intersection of the image footprint with the aoi

.. warning::
    The size of the search area cannot exceed the size of AOI limit assigned to the specific user.

1. Response example – *Scene*:

.. code:: json

        {
            "id": "JL1GF03A_PMS_20220607132729_200087596_103_0002_001_L1",
            "footprint": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            76.5009,
                            43.3412
                        ],
                        ...
                    ]
                ]
            },
            "pixelResolution": 1.06,
            "acquisitionDate": "2022-06-07T13:27:33Z",
            "productType": "Scene",
            "sensor": "JL1GF03A",
            "colorBandOrder": "B,G,R,NIR,PAN",
            "cloudCover": 0.09,
            "offNadirAngle": -3.91,
            "previewType": "png",
            "previewUrl": "https://cgwx-jpg.obs.cn-north-4.myhuaweicloud.com:443/thumbnail_mss/JL1GF03A_PMS_20220607132729_200087596_103_0002_001_L1.jpg",
            "providerName": "CG"
        }

.. image:: _static/data_api/CG_image_preview.jpg
   :alt: Preview image
   :align: center
   :width: 8cm
   :class: with-border no-scaled-link 

|

2. Response example – *Mosaic*:

.. code:: json

        {
            "id": "JL1KF01A_PMS04_20220717131252_200093089_101_0005_001_L1",
            "footprint": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [
                            [
                                76.903651508,
                                43.252856702
                            ],
                            ...
                        ]
                    ]
                ]
            },
            "pixelResolution": 0.0,
            "acquisitionDate": "2022-07-17T00:00:00Z",
            "productType": "Mosaic",
            "sensor": "JL1KF01A",
            "colorBandOrder": "RGB",
            "cloudCover": 0.0,
            "offNadirAngle": 3.0,
            "previewType": "xyz",
            "previewUrl": "https://app.mapflow.ai/tiles/charmingglobe/{z}/{x}/{-y}.png?year=2022",
            "providerName": "CG_mosaic_2022"
        }

.. note::

    There are two types of products in the Imagery Search API, available for ordering;
    1. The **Scene** product is available by request, the workflow implementation is in progress.
    1. The **Mosaic** product is available for instant processing if the appropriate data provider is linked to your Mapflow account. 


Run processing by image ID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For detailed description how to run a processing with Mapflow API see :doc:`Mapflow Processing API <processing_api>` – "Create processing".
To run a processing using the specific image returned by Search API define **provider** and **image ID** in the params as follows:

``{"params": {"data_provider":<providerName>, "url":<id>}}``


