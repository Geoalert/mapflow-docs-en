.. _howto:

Userguides - How To
===================

How to change the data type of your image to Uint8 bit in QGIS
--------------------------------------------------------------

1. Check the data type of your image. 
Right-click on the imagery layer - i - Information from provider. The Data type must be Byte. Follow the next steps if the Data type is Int16, Float 32 etc.

    
    .. figure:: _static/information.png


  

2. Right click on your image Layer Properties -  Symbology tab, then customize the display of your image. Select desired channels for Band rendering, adjust brightness and contrast. 
      
    
    .. figure:: _static/symbology.png



3. Right-click on the layer’s name, go to the  Export in the context menu, Save as…

 
    .. figure:: _static/export.png
    


4. Check Output mode as Rendered Image


    .. figure:: _static/save_raster.png
    


5. Save your image  - navigate to the desired folder, input the file name then click OK



6. Use the new image layer as Imagery source when using the Mapflow plugin for QGIS


How to process your own UAV imagery with Mapflow
------------------------------------------------

Unmanned aerial vehicles – UAVs or, more commonly, drones – have become a deeply integrated part of the geomatic industry over the last ten years. This is owing to their increasing usability, falling hardware costs, and easing government regulations. Yet, as more data is available with UAV surveys, more data need to be processed operatively. 
To process your UAV data you might be looking for some cloud or desktop software to create a mosaic or orthophoto.  Do you know that you can easily publish your data with Openaerialmap and analyze (say detect and calculate some objects and calculate their areas) with Mapflow QGIS or Mapflow Web? 

Let’s take the “UAV buildings” :doc:`models_changelog/buildings_aerial_imagery_model` model that extracts the detailed building outlines (the recommended image resolution is 10 cm).

Processing with Mapflow Web
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case you are already used to working with QGIS you need to install the Mapflow plugin. You can upload your own GeoTIFF (up to 2 GB). All raster layers currently loaded in your QGIS (1) are visible in the drop-down list (2) and can be selected for upload. 
Open files in the Additional options (3) also adds your item to the tree of QGIS layers.

    .. image:: _static/select_raster_qgis.png
       :align: center
       :class: with-border

.. important::

    Please, consider the requirements specified on the page with Models reference when uploading your own images for AI-mapping processing.

Use Openaerialmap as an imagery publication tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`OpenAeriaMap <https://map.openaerialmap.org>`_ is an open collection of UAV imagery data, crowdsourced by users. The project is supported by a consortium of companies developing open source software and services for working with geospatial data.
As soon as your aerial image published on Openaerialmap it’s displayed on the public map and can be streamed using TMS/WMTS protocols or downloaded as GeoTIFF file. 
Both ways are OK to work with Mapflow.

    .. image:: _static/oam_search.png
       :align: center
       :class: with-border

1. Copy link to TMS and paste it into the “Custom imagery URL” in your new Mapflow processing. 
2. Check if you see the image on the map, go through the next steps (AI model, processing params) to and start the processing.

Preparing and optimizing the large size images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here are few tips on how to prepare and optimize your data and reduce the image size to upload it faster and not to exceed the Mapflow upload limit.

Usually UAV image is an RGB compiosite provided as GeoTIFF of 16 or 8 bit. 
The type must be Byte (8 bit). If the Data type is Int16 or Float32 etc, please follow the instruction :doc:`howto`.
Alternatively: use the `preprocessing script <https://github.com/Geoalert/mapflow_data_preprocessor/>`_ for preparing your image for Mapflow processing.

You can reduce the size of the image using GDAL translate. (https://gdal.org/)
E.g. using JPEG compression.
``gdal_translate -co compress=JPEG input.tif output.tif``
By default the compression quality is 75% (``gdal_translate -co compress=JPEG -co jpeg_quality=75 input.tif output.tif``) but it doesn’t really impact the quality of the Mapflow mask whenever the resolution of the input iage meets the recommended params.

The same can be done using QGIS interface:

    .. image:: _static/optimize_qgis.png
       :align: center
       :class: with-border


Tell us if you have more tips to share with the community or if you have more questions – we are ready to help.

**Run the flow!**


How to view results using Kepler.gl
-----------------------------------

**Kepler.gl** is an open source tool designed for geospatial data analysis. It is a simple yet powerful for displaying and exploring geodatasets.

To view the processing results in the Mapflow, select the required processing and press the button *"Open in kepler.gl"*.

.. note ::
   You can share your processing view in Kepler by copying the open URL (right click on *"Open in kepler.gl"* --> Copy Link Address)

Using the Kepler you can change the visual properties of data, set filters, and choose a background map.


Layers tab
^^^^^^^^^^

Click on the layer name to bring up the *Layer settings* from the drop-down menu. To hide all data, click on the *eye* icon.

.. figure:: ../kepler/_static/view_layer_settings.png
    :alt: View layer settings
    :align: center
    :width: 15cm


These settings allow you to choose a more suitable type of received data:


* *Fill color.* You can choose any color from the palette for polygons, and also hide the display of data by changing the position of the slider. You can change the transparency of polygons (property *Opacity*) in the additional settings of this function.
* *Stroke color.* You can choose any color from the palette for outlining polygons, as well as completely remove the stroke. You can change the transparency of the stroke (property *Opacity*) In the additional settings of this function.
* *Stroke width.* Controls the thickness of the stroke.
* *Height.* Allows you to view data with heights in 3D format. Set the desired coefficient and select the attribute of the layer with heights.

.. figure:: ../kepler/_static/3D_buildings.png
    :alt: 3D buildings
    :align: center
    :width: 15cm


Filters tab
^^^^^^^^^^^

This tab allows you to add a filter of interest by a specific attribute of the layer (as in this case, the filter is set by classes with different typology of buildings).

.. figure:: ../kepler/_static/filter_panel.png
    :alt: Filter panel
    :align: center
    :width: 15cm


Interaction tab
^^^^^^^^^^^^^^^

You can select or remove attributes that will be visible in the menu that appears when you hover over an object. It is also possible to turn on the panel indicating longitude and latitude.

.. figure:: ../kepler/_static/interaction_panel.png
    :alt: Interaction panel
    :align: center
    :width: 15cm


Base map tab
^^^^^^^^^^^^

Here you can choose the styles of the map, as well as choose to display its various layers.

.. figure:: ../kepler/_static/base_map_panel.png
    :alt: Interaction panel
    :align: center
    :width: 5cm