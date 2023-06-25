Mapflow <> QGIS
===============

.. attention::
    Mapflow can be used via `QGIS <https://www.qgis.org/>`_. You will need access to the data processing API that to use it (see :doc:`authorization to work with the Mapflow API <../userguides/mapflow_auth>`).

    In the `API tab <https://app.mapflow.ai/account/api>`_ of the profile settings is specified the area limit for processing provided to you (initially 25 km\ :sup:`2`) and the total area of ​​already completed processing.

.. note::
      .. figure:: _static/github_logo.png
       :alt: Preview results
       :align: left
       :width: 1cm
       
  Join Mapflow <> QGIS `open source project on Github <https://github.com/Geoalert/mapflow-qgis>`_. 

What is QGIS
-------------

QGIS is the leading and most popular Open Source Desktop GIS. Users can visualize, manage, edit, analyse geodata, and compose printable maps. Get a first impression with a more detailed feature list.
Know more on QGIS and istall `official site <https://www.qgis.org/>`_. 

QGIS has an interface for external Python plugins that allows to connect more apps and extend core functionallity. Our "Mapflow - QGIS" app enables connection to Mapflow :doc:`processing_api` to run AI-mapping and add output as layers to the QGIS workspace.


How to install the plugin
-------------------------

Click *Plugins* --> *Manage...*, go to the *Not installed* (or *All*) tab and enter "MapFlow" in the search box. Click *Install Plugin*. You will be able to see then if the newer version of the app is available (in the Upgradeable tab) and to check the changelog for details.

The plugin icon has appeared in the QGIS Toolbar. 

.. hint::
  If the icon isn't automatically displayed, right-click on the Toolbar and check if the Mapflow toolbar is activated.


How to login
------------

You need to log in with your credentials to start using the plugin. Go to `mapflow.ai <https://app.mapflow.ai/>`_, register and obtain `API token <https://app.mapflow.ai/account/api>`_.

.. figure:: _static/qgis/login_window.png
         :alt: Login window
         :align: center
         :width: 9cm

|


User interface
--------------


Mapflow plugin
~~~~~~~~~~~~~~~~

Main plugin workspace has two sections: left sidebar with the processing controls and the tabs section.

.. figure:: _static/qgis/main_window.png
         :alt: View of the main window
         :align: center
         :width: 20cm

|

Processing controls panel allows to start new processing and/or rate finished processings, and includes following:

**Processing controls panel**

.. csv-table::
    :file: _static/qgis/processing_controls_panel.csv 
    :header-rows: 1 
    :class: longtable
    :widths: 1 3  

|

How to run the processing
~~~~~~~~~~~~~~~~~~~~~~~~~

To start the processing you need to select the **Polygon Area** (AOI) on a Map.

The plugin has several built-in options for creating AOI.

   1. Create new AOI from the map extent using the "+" button;

   2. Upload the existing AOI using the "+" button;

   3. Use the extent of the uploaded image;

  Besides, you can create a new vector layer or add existing AOI into QGIS project. If the vector layer consists of several polygons select one of them.

  .. figure:: _static/qgis/AOI_button.png
         :alt: View of the aoi 
         :align: center
         :width: 15cm



Tabs section contains 4 tabs:

:ref:`Processing`

:ref:`Providers`

:ref:`Settings`

:ref:`Help`


.. _Processing:

1. Processing
~~~~~~~~~~~~~~

.. figure:: _static/qgis/processing_tab.png
         :alt: View of the processing tab
         :align: center
         :width: 15cm

|

**Start processings and display the output on the map**

.. list-table::
   :widths: 5 10
   :header-rows: 1

   * - Name of the field / button
     - Description
   * - Name
     - Processing name.
   * - Model
     - User-selected item from the list of available models.
   * - Status
     - Processing status: IN_PROGRESS, OK, FAILED. 
   * - Progress
     - The percentage of completeness of the processing.
   * - Area
     - The processing area.
   * - Created
     - The date-time of the processing creation.
  

To download the processing results, double-click on the completed processing.

This tab contains also two buttons: *Download results* and *Delete* buttons.

*Download results* - downloading the results of completed processing. 

*Delete* - delete selected processing/processings. 

.. _Providers:

2. Providers
~~~~~~~~~~~~~

.. figure:: _static/qgis/Providers_tab.png
         :alt: View of the providers tab
         :align: center
         :width: 15cm

|


.. list-table::
   :widths: auto
   :header-rows: 1

   * - Name of the field / button
     - Description
   * - Additional sources of images
     - Drop-down list with additional satellite imagery providers.
   * - "Add" button
     - Button for adding a source of satellite images. 
   * - "Delete" button
     - Button for deleting the source of satellite images.
   * - "Edit" button
     - Button for changing the parameters of the source of satellite images.
   * - Preview
     - A button to preview the background of the specified satellite imagery and geospatial provider.
   * - Image ID
     - Image ID from the *Imagery catalog* of the selected image of specified satellite image source.
   * - Max zoom
     - Zoom number is selected by default to exclude the consumption of paid traffic for preview (Relevant if connected to **Maxar SecureWatch**).
   * - Area
     - The area for which metadata will be presented.
   * - Use canvas extent
     - The processing area will be taken from the QGIS image search workspace of the specified satellite imagery provider.
   * - Period of time (From...To)
     - The images will be provided for the specified time period.
   * - Search imagery
     - Use to collect metadata for the selected area. After clicking it, a list will be shown with all images intersecting your area.
   * - Additional Filters
     - Use to set the minimum intersection rate between the image and the area of interest and the minimum percentage of image cloudiness.


.. hint::
    You can define your own source of data in XYZ format. Here is the example: ``https://your_site.xyz/{z}/{x}/{y}``

    Check for free aerial images and try XYZ links at  `Open aerial Map <https://tiles.openaerialmap.org>`_.


.. _Settings:

3. Settings
~~~~~~~~~~~~~

This tab contains *Output directory* and *Logout* button. 

*Output directory* - Define where the processing results will be loaded.

*Logout* button - Sign out from your Mapflow account.

.. _Help:

4. Help
~~~~~~~~

The tab contains all useful links to this plugin documentation.


Use commercial satellite imagery providers
-------------------------------------------

How to connect to Maxar SecureWatch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
 SecureWatch is a service that provides global access to high-resolution satellite images and imagery basemaps from the world leader in remote sensing, MAXAR, through the subscription model. The spatial resolution of images varies in the range from 30 cm to 1 m. All images are accompanied by metadata, including information about the acquisition date and time, cloud cover etc. In our application we implemented the special interface to connect to this service and use imagery via Mapflow's processings pipelines.


* **Use of embedded Maxar SecureWatch for image processing by Mapflow**

  On the **Processing** tab, in the *Remote sensing data* drop-down list, select the required Maxar product (SecureWatch, Vivid), specify all processing parameters and click the *Start processing*.

* **Maxar preview**

  1. Select the required Maxar product in the drop-down list on the **Data sources** tab;
  2. Select your AOI in the Area drop-down list and click on the *Search imagery*.
  3. Double click on the selected image in the search results (or click Preview button) to add it on the map.

.. important:: 
   In the free tariff plan the *Max zoom* is limited up to 12 and the processing cannot be started using SecureWatch. If you want to use this data provider - you have to switch to the `Premium <https://mapflow.ai/pricing>`_ tariff plan or `write to us <https://geoalert.io/#contacts>`_ to get a quote.



* **Using your SecureWatch account for image processing by the Mapflow**

.. figure:: _static/qgis/addnewprovider.png
         :alt: View of the providers tab
         :align: center
         :width: 15cm

|


   1. Click *+* button on the *Providers* tab, choose Maxar WMTS option in the dropdown list;

   2.  Enter *Login / Password* from your Maxar SecureWatch account;

   3.  Enter WMTS URL link for Maxar Secure Watch (`SecureWatch <https://securewatch.digitalglobe.com/myDigitalGlobe/logout-from-ended-session>`_ - Login - Securewatch - Use with - Web Services - WMTS)

   4.  Optional: specify the coordinate system;

   5.  Optional: Check *Save login and password*



  .. hint::
       How to find out Maxar WMTS:

      1. Go to `SecureWatch <https://securewatch.digitalglobe.com/myDigitalGlobe/logout-from-ended-session>`_ and login.

      2. In the upper menu select **Use With** >> **Web Services** >> **WMTS**

      3. Copy the WMTS (or TMS) url.

        .. figure:: _static/qgis/SecureWatch_user_profile.png
         :alt: Your user profile in SecureWatch
         :align: center
         :width: 15cm

        The **Connect ID** is different for each product you have in your SecureWatch subscription. Therefore, initially choose the one you want. To do this, open the *User Profile* menu and in the title bar select the required of the two suggested mosaics (**Vivid** and **SecureWatch**).
     

  4. Click *Preview*. 
     
Now the Maxar layer is available for preview in your raster layers list and for the AI-mapping processing using Mapflow.


How to find and process the image by Feature ID using Maxar SecureWatch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use SW to discover available images for you area of interest.

1. Go to the *Providers* tab.
2. Select Maxar SecureWatch from the dropdown list.
3. In the *Maxar SecureWatch imagery Catalog* select the vector layer containing the boundary of your area of interest.

.. note::
    You have to create the new one area (*Layer -> Create layer -> ...*, select *Polygon* as a geometry type, in the created layer using the tool *Add polygon feature* draw an area of interest) or to upload from the file with coordinates using QGIS. If there is more than one polygon in the file, select with the tool *Select object(s)* the polygon you need. For more information on creating and working with vector layers, see the `QGIS User Guide <https://docs.qgis.org/3.16/en/docs/training_manual/create_vector_data/create_new_vector.html>`_.

     .. figure:: _static/qgis/add_SW_WFS.png
         :alt: Get specific image from SW
         :align: center
         :width: 15cm    

4. *Search imagery*, to view meta-data of all available images intesecting your AOI. You can apply search filters and specify the period for which you would like to receive images. This will help in forming an imagery catalog with the necessary parameters.
5. Select the prteferable image from the imagery catalog or use the WFS generated vector layer (*Maxar SW metadata metadata*) to search through more attributes. If you want to process a specific image in advance, insert your image ID in the field on the top of the plugin, this will make it easier to find the image in the imagery catalog.

.. note::
    Imagery metadata is saved in the form of vector layer. You can interact with its Attribute Table by searching through all attributes.

6. Click *Preview* to view the selected image in the form of new raster layer (or double-clicking on the row in the table).

.. attention::
    "max zoom 13" checkbox is active to prevent the paid streaming on the side of SecureWatch.
     

How to use other imagery services
------------------------------------

For example, let's use the `Openaerialmap <https://openaerialmap.org/>`_ is an open collection of UAV imagery data, crowdsourced by users. The project is supported by a consortium of companies developing open source software and services for working with spatial data.
As soon as your aerial image is published on Openaerialmap it's presented on the public map and can be fetched using TMS/WMTS protocols.

Select the image and copy link to TMS.

  .. figure:: _static/qgis/search_openaerialmap_image.png
         :alt: Search for imagery in Openaerialmap 
         :align: center
         :width: 15cm

  |

Go to the plugin, on the *Providers* tab click on the *Add* (1) and enter the relevant data in the opened window (2). Click the *Preview* (3) the image, - you must be at the correct zoom and coordinates to see the image.

To start processing using this data source, go to the *Processing* tab, fill in all fields of processing parameters, click *Start processing*.

 .. figure:: _static/qgis/custom_imagery_source.png
         :alt: Custom imagery service
         :align: center
         :width: 15cm

 |

.. list-table::
   :widths: 10 30
   :header-rows: 1
 
   * - Name of the field / button
     - Description
   * - Name
     - Name of other imagery data provider
   * - URL
     - URL of the imagery data provider
   * - Type
     - Data source type. You can enter your custom imagery source URL in one of the following formats: `XYZ <https://en.wikipedia.org/wiki/Tiled_web_map>`_, `TMS <https://en.wikipedia.org/wiki/Tile_Map_Service>`_, `WMS <https://en.wikipedia.org/wiki/Web_Map_Tile_Service>`_, `Quadkey <https://docs.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system>`_. All formats represent the most widely used protocols to fetch georeferenced imagery via HTTP.


How to upload your image
-------------------------

You can upload your own GeoTIFF. All raster layers currently loaded in your QGIS (1) are visible in the drop-down list (2) and can be selected for upload. Opening files from the *Additional options* button (3) also adds it to the tree of QGIS layers.

 .. figure:: _static/qgis/upload_tif.png
         :alt: Upload TIF, select from list
         :align: center
         :width: 15cm

|

.. important::

  Please, follow the requirements specified on the page with :doc:`../userguides/requirements` when uploading your own images for processing through the API of the Mapflow platform.

    * **Check the data type** 
          The Data type must be Byte (8 bit). If the Data type is Int16,  or Float32 etc, please follow the instruction :doc:`../userguides/howto`.

          Alternative option: use the `preprocessing script <https://github.com/Geoalert/mapflow_data_preprocessor/>`_ 
    * **Check the number of channels**  
          Normally, the Mapflow processes 3-channel RGB rendered images. Mapflow platform can also process single-band (panchromatic) imagery, but the NN models are not
          tuned for such kind of data, so the quality of the result may be worse than expected.
    * **Check the projection and georeference** 
          Make sure that your imagery is georeferenced in geographic or projected coordinate system.
    * **Check the resolution**
          The resolution restrictions vary for different models, see :ref:`Model requirements`   
  
You can send a request for data preprocessing to help@geoalert.io


Proxy-settings
--------------

If you are behind a firewall, go to *QGIS* -> *Preferences* -> *Network* and will please adjust the proxy settings for plugin connection.

 .. figure:: _static/qgis/proxy_settings.png
         :alt: Proxy settings
         :align: center
         :width: 15cm

|