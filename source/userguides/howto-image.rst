How to process your own UAV imagery with Mapflow
================================================

Unmanned aerial vehicles – UAVs or, more commonly, drones – have become a deeply integrated part of the geomatic industry over the last ten years. This is owing to their increasing usability, falling hardware costs, and easing government regulations. Yet, as more data is available with UAV surveys, more data need to be processed operatively. 
To process your UAV data you might be looking for some cloud or desktop software to create a mosaic or orthophoto.  Do you know that you can easily publish your data with Openaerialmap and analyze (say detect and calculate some objects and calculate their areas) with Mapflow QGIS or Mapflow Web? 

Let’s take the “UAV buildings” :doc:`models_changelog/buildings_aerial_imagery_model` model that extracts the detailed building outlines (the recommended image resolution is 10 cm).

Processing with Mapflow Web
----------------------------

1. Select raster source – you can either use Custom URL (see below how to publish your image with Openaerialmap and get the TMS link) or upload your image as GeoTIFF.

    .. image:: _static/select_provider_2.png
            :align: center
            :class: with-border
            :scale: 50

.. warning::

    *Currently, a preview of the uploaded image is not possible after loading the image, you will see only the area of its extent.*

2. Define the processing Area.
The processing area (AOI) must be located within the area of the image extent, otherwise, the area will be cut off by the extent boundaries. The processing area size is calculated by the intersection of the image extent and the AOI.

.. important::

    Image upload requirements:
    The file size must be less than 512 mb.

    The image must be georeferenced and the CRS must be one of:
    * WGS84 (EPSG: 4326)
    * Web mercator (EPSG: 3857)
    * UTM (any zone)

    If your image doesn’t meet the parameters, we suggest using Mapflow API / QGIS plugin which has more capabilities.
    Mapflow supports RGB imagery and also processes single-band (panchromatic) imagery, but the AI models are not tuned for such kind of data, so the quality of the result may be worse than expected.


Processing with Mapflow – QGIS
------------------------------

In case you are already used to working with QGIS you need to install the Mapflow plugin. You can upload your own GeoTIFF (up to 2 GB). All raster layers currently loaded in your QGIS (1) are visible in the drop-down list (2) and can be selected for upload. 
Open files in the Additional options (3) also adds your item to the tree of QGIS layers.

    .. image:: _static/select_raster_qgis.png
       :align: center
       :class: with-border

.. important::

    Please, consider the requirements specified on the page with Models reference when uploading your own images for AI-mapping processing.

Use Openaerialmap as an imagery publication tool
------------------------------------------------

`OpenAeriaMap <https://map.openaerialmap.org>`_ is an open collection of UAV imagery data, crowdsourced by users. The project is supported by a consortium of companies developing open source software and services for working with geospatial data.
As soon as your aerial image published on Openaerialmap it’s displayed on the public map and can be streamed using TMS/WMTS protocols or downloaded as GeoTIFF file. 
Both ways are OK to work with Mapflow.

    .. image:: _static/oam_search.png
       :align: center
       :class: with-border

1. Copy link to TMS and paste it into the “Custom imagery URL” in your new Mapflow processing. 
2. Check if you see the image on the map, go through the next steps (AI model, processing params) to and start the processing.

Preparing and optimizing the large size images
----------------------------------------------

Here are few tips on how to prepare and optimize your data and reduce the image size to upload it faster and not to exceed the Mapflow upload limit.

Usually UAV image is an RGB compiosite provided as GeoTIFF of 16 or 8 bit. 
The type must be Byte (8 bit). If the Data type is Int16 or Float32 etc, please follow the instruction :doc:`howto8bit`.
Alternatively: use the `preprocessing script <https://github.com/Geoalert/mapflow_data_preprocessor/>`_ for preparing your image for Mapflow processing.

You can reduce the size of the image using GDAL translate. (https://gdal.org/)
E.g. using JPEG compression.
``gdal_translate -co compress=JPEG input.tif output.tif``
By default the compression quality is 75% (``gdal_translate -co compress=JPEG -co jpeg_quality = 75 input.tif output.tif``) but it doesn’t really impact the quality of the Mapflow mask whenever the resolution of the input iage meets the recommended params.

The same can be done using QGIS interface:

    .. image:: _static/optimize_qgis.png
       :align: center
       :class: with-border


Tell us if you have more tips to share with the community or if you have more questions – we are ready to help.

**Run the flow!**