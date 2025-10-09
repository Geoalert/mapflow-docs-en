.. _Mapflow <> QGIS:

Mapflow <> QGIS
================

.. attention::
    Mapflow can be used via QGIS. You need to autohorise :doc:`authorization to work with the Mapflow API <../userguides/mapflow_auth>` and get `API token <https://app.mapflow.ai/account/api>`_ to login.

.. note::
      .. figure:: _static/github_logo.png
       :alt: Preview results
       :align: left
       :width: 1cm
       
  Join Mapflow <> QGIS `open source project on Github <https://github.com/Geoalert/mapflow-qgis>`_. 

What is QGIS
-------------

QGIS (`qgis.org <https://www.qgis.org/>`_) is the leading and most popular Open Source Desktop GIS. Users can visualize, manage, edit, analyse geodata, and compose printable maps. Get a first impression with a more detailed feature list.
Know more about QGIS and istall it from `official site <https://www.qgis.org/>`_. 

QGIS has an interface for external Python plugins that allows to connect more apps and extend core functionallity. Our "Mapflow - QGIS" app enables connection to Mapflow :doc:`processing_api` to run AI-mapping and add output as layers to the QGIS workspace.


How to install the plugin
-------------------------

Click *Plugins* -–> *Manage...*, go to the *Not installed* (or *All*) tab and enter "MapFlow" in the search box. Click *Install Plugin*. You will be able to see then if the newer version of the app is available (in the Upgradeable tab) and to check the changelog for details.

The plugin icon has appeared in the QGIS Toolbar. 
If the icon isn't automatically displayed, right-click on the Toolbar and check if the Mapflow checkbox is activated.


How to login
------------

You need to log in with your credentials to start using the plugin. Go to `mapflow.ai <https://app.mapflow.ai/>`_, register and obtain `API token <https://app.mapflow.ai/account/api>`_.

.. figure:: _static/qgis/login_window_w_oauth.png
         :alt: Login window
         :align: center
         :width: 9cm

|

Or you can use the `OAuth 2.0 <https://en.wikipedia.org/wiki/OAuth>`_ protocol as a more convenient and secure way.

.. warning::
  Logging in with OAuth is a convenient feature, but still experimental for us.

  Also keep in mind that at the moment this feature does not support proxies.

OAuth2 setup
~~~~~~~~~~~~

Information on how to log in using OAuth can be found in :doc:`this section <../userguides/howto>`.

User interface
----------------

Main plugin workspace has two sections: left sidebar with the processing controls and the tabs section.

Processing controls panel allows to start new processing and/or rate finished processings, and includes following:

.. figure:: _static/qgis/processing_panel.jpg
         :alt: View of the processing panel
         :align: center
         :width: 8cm
         :class: with-border

**Processing controls panel**

.. csv-table::
    :file: _static/qgis/processing_controls_panel.csv 
    :header-rows: 1
    :class: longtable
    :widths: 10 20

Your current balance is dispayed in the Tob bar. It also contains menu to access you personal profile on Mapflow.ai: top up you balance; open billing history; log out of current session. 

The main window contains 5 tabs:

:ref:`Project/Processing`

:ref:`Imagery_search`

:ref:`My imagery qgis`

:ref:`Settings`

:ref:`Help`


.. _Project/Processing:

1. Project/Processing
~~~~~~~~~~~~~~~~~~~~~~~

This tab is divided into two parts. First, you will see a list of your projects. Here you can create, edit, and delete projects using the buttons at the bottom of the panel. Various sorting options and a search for a project by name are also available.

.. figure:: _static/qgis/project_tab.png
         :alt: View of the project tab
         :align: center
         :width: 18cm
         :class: with-border no-scaled-link 

         Project tab

.. |right_arrow| image:: _static/qgis/right_arrow.png
  :width: 0.7cm

.. |left_arrow| image:: _static/qgis/left_arrow.png
  :width: 0.7cm

To go to the processing of the selected project, you need to double-click on it or select the project and click on |right_arrow|. To return to the list of projects, click |left_arrow|.

.. note::
  Since plugin version 3.3.0, the processing :ref:`API v2.0 <processing-api-v2>` is used.

.. figure:: _static/qgis/processing_tab.png
         :alt: View of the processing tab
         :align: center
         :width: 18cm
         :class: with-border no-scaled-link

         Processing tab

To view the processing results, click on the "View results" button or double-click on the processing name in the table. 
You can manage the processings using the options and buttons in the bottom panel menu (Delete, Rename, Save results, etc.). Processing filter by name is available at the top of the panel.

Just like in Mapflow WEB, you can duplicate the selected processing and run a copy of it with the same parameters via "Duplicate" button. Also, if the processing fails, you can restart it using the "Restart" button (it is displayed in the menu only if the selected processing is in a FAILED status).

.. hint::
    To download the processing results, you can double-click on the completed processing in the list. 
    
.. hint::   
    By default the processing results are downloadable as vector tiles for faster preview.  To donwload the processing results as a file you havve to choose this option: Setttings --> "save rresults as a local vector file"

To view detailed information about a processing, click "See details". The window that opens will display the processing's **Name**, **ID** and **Status**, as well as the **Data provider**, **Model** and **Model options** used.
In some cases, a button will appear next to the **Data provider**. You can use it to go directly to the data source, for example, to a "My imagery" collections or a specific image.

.. figure:: _static/qgis/see_details_window.png
         :alt: View of the see details window
         :align: center
         :width: 11cm
         :class: with-border no-scaled-link

         Processing details

.. **Explanation of the fields and buttons of this tab:**

.. .. list-table:: Fields
..    :widths: 5 10
..    :header-rows: 1

..    * - Name of the field
..      - Description
..    * - Name
..      - Your processing name.
..    * - Model
..      - User-selected item from the list of available models.
..    * - Status
..      - Processing status: IN_PROGRESS, OK, FAILED. 
..    * - Progress
..      - The percentage of completeness of the processing.
..    * - Area
..      - The processing area (AOI).
..    * - Created
..      - The date-time of the processing creation.

.. .. list-table:: Buttons
..    :widths: 5 10
..    :header-rows: 1

..    * - Name of the button
..      - Description
..    * - View results
..      - Shows the results of completed processing in QGIS layers.
..    * - Delete
..      - Deletes selected processing/processings.
..    * - Options
..      - A list of options for working with the results of processings.
..    * - Save results
..      - Saves processing results to GeoJSON file. 
..    * - Download AOI
..      - Adds processing AOI to qgis as a layer, for further work or export.
..    * - See details
..      - Shows information about processing (*Name, Status, Model, Model options, Data provider*).
..    * - Rename
..      - Renames your processing.


.. _Imagery_search:

2. Imagery search
~~~~~~~~~~~~~~~~~~~

.. figure:: _static/qgis/imagery_search_tab.png
         :alt: View of the imagery search tab
         :align: center
         :width: 18cm
         :class: with-border

|

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Name of the field / button
     - Description
   * - Period of time (From...To)
     - The images will be provided for the specified time period.
   * - Mosaic
     - The search will be performed only for providers with the "Mosaic" type (ArcGIS World Imagery, Global mosaic 2022).
   * - Image
     - The search will be performed only for providers with the "Image" type (Orbview).
   * - Search
     - Use to collect metadata for the selected area. After clicking it, a list will be shown with all images intersecting your area.
   * - Min intersection
     - Use to set the minimum intersection rate between the image and the area of interest.
   * - Cloud cover
     - Use to set the minimum percentage of image cloudiness.
   * - Providers
     - Here you can select which providers will be searched.
   * - "Search only..."
     - The search results will show only those providers that are connected to your account.
   * - Preview
     - Click this column to preview the specified satellite imagery by geospatial provider.
   * - Clear
     - Deletes all search results from the table.

.. hint::
  Read more about :ref:`Imagery search <Imagery search  main>`.


How to preview the search results
"""""""""""""""""""""""""""""""""

.. |preview| image:: _static/qgis/magnifier_button.png
  :width: 0.7cm

Imagery search provides the ability to preview search results with a double-click on a row in a table. You cannot open previews of certain specific parts of some data sources (e.g. ArcGIS World Imagery), but you can enable preview of the entire source! To do this, select the desired provider in the left control panel and click the "Preview" button |preview|.

.. figure:: _static/qgis/preview_data_source.png
         :align: center
         :width: 10cm
         :class: with-border

|

.. _My imagery qgis:

3. My imagery
~~~~~~~~~~~~~~

To upload you images and process multiple images in a one shot you can use "My imagery" tool available in Mapflow QGIS.

**The main scenario of working with My imagery in QGIS:**

.. figure:: _static/qgis/my_imagery_scenario.png
         :align: center
         :class: with-border
         :width: 18cm

|

**Main interface:**

.. figure:: _static/qgis/my_imagery_main.png
         :alt: My imagery main
         :align: center
         :class: with-border
         :width: 24cm

|

How to run the processing using My imagery
"""""""""""""""""""""""""""""""""""""""""""

1. Create the Imagery collection by clicking "Add collection" (You can upload your image to it instantly or do it in the next step.);
2. Upload your images into collection, click "+" on selected collection and choose the way of uploading - you can choose from the file on your device or from QGIS raster layer;
3. Now you can preview the whole Imagery collection (QGIS tile layer will be added);
4. See the uploaded images and preview them one at a time (QGIS tile layer will be added):

.. figure:: _static/qgis/my_imagery_images.png
         :align: center
         :class: with-border
         :width: 18cm

|

5. To run the processing, select the collection or a single image you need. Choose custom AOI or collection/image extent through the "+" button;

.. note::
   Selecting Collection or Image extent as a processing AOI:

      .. figure:: _static/qgis/collection_or_image_extent.png
               :align: center
               :class: with-border
               :width: 11cm


.. figure:: _static/qgis/my_imagery_run.png
         :align: center
         :class: with-border
         :width: 18cm

         Example of processing by Imagery collection

|

6. Click "Start processing".

.. hint::
   You can delete your images from the Imagery collections one at a time or using multiselect:

    .. figure:: _static/qgis/my_imagery_delete.png
            :align: center
            :class: with-border
            :width: 12cm

    |

.. hint::
   You can rename images in your Imagery collections:

    .. figure:: _static/qgis/rename_image.png
            :align: center
            :class: with-border
            :width: 11cm

    |

.. _Settings:

4. Settings
~~~~~~~~~~~~~

.. figure:: _static/qgis/settings_tab.png
         :alt: View of the settings tab
         :class: with-border
         :align: center
         :width: 15cm

|

.. .. list-table:: 
..    :align: center
..    :widths: auto
..    :header-rows: 1

..    * - Name of the field / button
..      - Description
..    * - Imagery providers
..      - Drop-down list with additional satellite imagery providers.
..    * - "Add provider" button
..      - Button for adding a source of images. 
..    * - "Delete provider" button
..      - Button for deleting the custom data provider.
..    * - "Edit provider" button
..      - Opens dialog to edit custom data provider.
..    * - Select mapflow project
..      - Drop-down list with mapflow projects on you account.
..    * - "Add project" button
..      - Button for creating your new map flow project.
..    * - "Delete project" button
..      - Button for deleting the mapflow project.
..    * - "Edit project" button
..      - Button for editing the mapflow project.

This tab allows you to manage many of the plugin's components: 

- **Add, edit, and delete data sources;**
- **Configure columns in Processing and Imagery search tables;**
- **Сonfigure how the processing results will be uploaded to QGIS;**

    There are two ways:

    1. ``view result as a vector layer`` - This is streaming vector tiles directly from our server, which allows you to view results of the processings without downloading full results file, so it will be faster for big processings.

    2. ``save local gpkg file to view results`` - Saving local gpkg files on your disk for further loading as QGIS layers.

- **Enable or disable parameter confirmation before starting processing.**

.. figure:: _static/qgis/confirm_processing.png
         :alt: View of the processing confirmation
         :class: with-border
         :align: center
         :width: 14cm

         After clicking "Start processing", a confirmation of the parameters will appear

|

.. .. warning::
..   Vector tiles are an experimental feature for us, so choose the method that is convenient for you.

.. hint::
    This tab also contains *Output directory* button. 

    *Output directory* - set up where the processing results will be loaded on your local disk If the ``save local gpkg file to view result`` option is selected.

.. _Help:

5. Help
~~~~~~~~

The tab contains all useful links to the plugin documentation.


How to run the processing
"""""""""""""""""""""""""

To start the processing you need to add the Polygon **Area of Interest** (AOI).

The plugin has several built-in options for creating AOI.

   1. Draw AOI at the map;
   
   2. Use imagery extent (Imagery collection or Image extent will be used if the processing is started by My imagery);
   
   3. Create new AOI from the map canvas extent using the "+" button.

Besides, you can create a new vector layer or add existing AOI into QGIS project. If the vector layer consists of several polygons select one of them.

  .. figure:: _static/qgis/AOI_button.png
         :alt: View of the aoi 
         :align: center
         :width: 15cm
         :class: with-border no-scaled-link


Use of commercial satellite imagery providers
----------------------------------------------

How to search for specific images in the 🌏 Global mosaic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../userguides/search_mosaic.rst

.. _Maxar SecureWatch:

How to connect to Maxar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
 SecureWatch (new name - ) is a service that provides global access to high-resolution satellite images and imagery basemaps from the world leader in remote sensing, MAXAR, through the subscription model. The spatial resolution of images varies in the range from 30 cm to 1 m. All images are accompanied by metadata, including information about the acquisition date and time, cloud cover etc. In our application we implemented the special interface to connect to this service and use imagery via Mapflow's processings pipelines.


* **Use of embedded Maxar SecureWatch for image processing by Mapflow**

   In the *Settings -- Add or edit imagery providers* select the type *Maxar WTS*, switch to the *Imagery search* tab.

* **Maxar preview**

  1. Select your AOI in the Area drop-down list and click on the *Search imagery*.
  2. Double click on the selected image in the search results (or click Preview button) to add it on the map.

.. important:: 
   In the free tariff plan the *Max zoom* is limited up to 12 and the processing cannot be started using SecureWatch. If you want to use this data provider - you have to switch to the `Premium <https://mapflow.ai/pricing>`_ tariff plan or `write to us <https://geoalert.io/#contacts>`_ to get a quote.



* **Using your SecureWatch account for image processing by the Mapflow**

.. figure:: _static/qgis/addnewprovider.png
         :alt: View of the providers tab
         :align: center
         :width: 10cm
         :class: with-border no-scaled-link 

|


   1. Click *+* button and choose Maxar WMTS option in the dropdown list;

   2.  Enter *Login / Password* from your Maxar SecureWatch account;

   3.  Enter WMTS URL link for Maxar Secure Watch (`SecureWatch <https://securewatch.digitalglobe.com/myDigitalGlobe/logout-from-ended-session>`_ - Login - Securewatch - Use with - Web Services - WMTS)

   4.  Optional: specify the coordinate system (default epsg:3857);

   5.  Optional: Check *Save login and password*


  .. hint::
       How to find Maxar WMTS URL:

      1. Go to `SecureWatch <https://securewatch.digitalglobe.com/myDigitalGlobe/logout-from-ended-session>`_ and login.

      2. In the upper menu select **Use With** >> **Web Services** >> **WMTS**

      3. Copy the WMTS (or TMS) url.

        .. figure:: _static/qgis/SecureWatch_user_profile.png
         :alt: Your user profile in SecureWatch
         :align: center
         :width: 15cm
         :class: with-border no-scaled-link 

        The **Connect ID** is different for each product you have in your SecureWatch subscription. Therefore, initially choose the one you want. To do this, open the *User Profile* menu and in the title bar select the required of the two suggested mosaics (**Vivid** and **SecureWatch**).
     

  4. Click *Preview*. 
     
Now the Maxar layer is available for preview in your raster layers list and for the AI-mapping processing using Mapflow.


How to find and process the image by Feature ID using Maxar SecureWatch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use SW to discover available images for you area of interest.

1. Go to the *Providers* tab.
2. Select Maxar SecureWatch from the dropdown list.
3. In the *Maxar SecureWatch imagery Catalog* select the vector layer containing the boundary of your area of interest.

.. note::
    To define the imagery search area you can create the new polygon (*Layer -> Create layer -> ...*, select *Polygon* as a geometry type, add polygon using the tool *Add polygon feature*) or upload it from the file with coordinates. If there is more than one polygon in the file, select with the tool *Select object(s)* the polygon you need. For more information on creating and working with vector layers, see the `QGIS User Guide <https://docs.qgis.org/3.16/en/docs/training_manual/create_vector_data/create_new_vector.html>`_.
    Alternatively, you can check the option "use canvas extent".

     .. figure:: _static/qgis/add_SW_WFS.png
         :alt: Get specific image from SW
         :align: center
         :width: 15cm

4. *Search imagery*, to view meta-data of all available images intesecting your AOI. You can apply search filters and specify the period for which you would like to receive images. This will help in forming an imagery catalog with the necessary parameters.
5. Select the prteferable image from the imagery catalog or use the WFS generated vector layer (*Maxar SW metadata*) to search through more attributes. If you want to process a specific image in advance, insert your image ID in the field on the top of the plugin, this will make it easier to find the image in the imagery catalog.

.. note::
    Imagery metadata is saved in the form of vector layer. You can interact with its Attribute Table by searching through all attributes.

6. Click *Preview* to view the selected image in the form of new raster layer (or double-clicking on the row in the table).

.. attention::
    "max zoom 12" checkbox is active to prevent the paid streaming on the side of Maxar SecureWatch.
     

How to use other imagery services
------------------------------------

Go to the plugin, on the *Providers* tab click on the *Add* (1) and enter the relevant data in the opened window (2). Click the *Preview* (3) the image, - you must be at the correct zoom and coordinates to see the image.

To start processing using this data source, go to the *Processing* tab, fill in all fields of processing parameters, click *Start processing*.

 .. figure:: _static/qgis/custom_imagery_source.png
         :alt: Custom imagery source
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


.. hint::
    You can define your own source of data in XYZ format. The example: ``https://your_site.xyz/{z}/{x}/{y}``


.. hint::

  Check for more imagery sources connections in the UserGuide How To:

  1. How to connect to :ref:`Openaerialmap <oae>`

  2. How to connect to :ref:`Nearmap <Nearmap_>`

  3. How to connect to :ref:`Maxar Imagery <Maxar SecureWatch>`


How to upload your image
-------------------------

You can upload your own GeoTIFF using :ref:`My Imagery <My Imagery qgis>`.


.. important::

  Please, follow the requirements specified on the page with :doc:`../userguides/requirements` when uploading your own images to the Mapflow platform. If you get the error message while uploading your data, please check the instruction :doc:`../userguides/howto`. 

    * **Check the data type** 
          Your data is supposed to be automatically converted into RGB, 8bit. To preprocess your data locally before uploading it to Mapflow you can use the `preprocessing script <https://github.com/Geoalert/mapflow_data_preprocessor/>`_
    * **Check the image size**
          Both sides image dimension must not exceed 30.000x30.000 pixels. If you have larger images you should either cut them in smaller chunks or switch to the `Mapflow Premium <https://geoalert.io/#contacts>`_.
    * **Check the number of channels**  
          Normally, the Mapflow processes 3-bands RGB rendered images. Mapflow platform can also process single-band (panchromatic) imagery, but the  quality of the result may be worse than expected.
    * **Check the projection and georeference** 
          Make sure that your imagery is georeferenced in geographic or projected coordinate system.
    * **Check the resolution**
          The resolution restrictions vary for different models, see :ref:`Model requirements`   
  


Work with results
------------------

View the results
~~~~~~~~~~~~~~~~~~~~~

The processing results that are 100% complete can be downloaded as a vector file to your local directory or streaming as a vector tiles and automatically added as layer to QGIS workspace.

Double click on the processing name in the :ref:`Processing <Project/Processing>` table or select it and push the button "View results".
The layer will appear in the Layers panel (QGIS --> View --> Panels --> Layers) in the folder "Mapflow".
You can work with it further as with the usual vector layer in QGIS.

.. note::
  If the default AI model is used, the plugin automatically assigns predefined styles to the vector layer. For all custom models / pipelines the single default style is assigned. You can always change it.

Save results
~~~~~~~~~~~~~~~~~~~~~~
The processing results, which are 100% complete, can be downloaded in GeoJSON format, to do this, click on the ``Save results`` button, select output directory in the window that appears and name the file to be saved.

Delete the processing
~~~~~~~~~~~~~~~~~~~~~~

To delete the processing - select it in the list, click the button "Delete" and confirm.

.. warning::
  The processing cannot be restored by user. Before the permanent deletion the data backup is **temporarily stored** on the Mapflow server in case of emergency. So if you deleted your results by mistake and want us to restore the processing – send your request to the support without delay.
 

Review the results*
~~~~~~~~~~~~~~~~~~~~

.. note::
   ❗️ This option is available for the limited number of Mapflow customers who have signed up for the enterprise support

If activated, every completed processing comes with the status **"Review required"**. The user can either accept the result or request the review, so the support can reprocess it and get better results, until it meets the requirements. 
To request the **Review** of the results:

.. _Review workflow:

1. Select the processing with the Status **"Review required"** and click the "Review" button

2. Provide comments in the Review dialogue:

.. epigraph::
  * Add your comment on why and what you want us to make a review
  * *Optionally* Add the polygon area, highlighting the objects that are not correctly processed, weren't identified correctly, etc – it will help us to pay attention to the specific issues
  * The processing Status will change to **"In review"**

 .. figure:: _static/qgis/review_required.jpg
         :alt: Upload TIF, select from list
         :align: center
         :width: 15cm
         :class: with-border
         
         Select AOI and request a Review

3. As soon as Review is done on our side the Status will change back to **"Review required"**. Accept the results or return to the #1


 .. figure:: _static/qgis/review_accept.jpg
         :alt: Upload TIF, select from list
         :align: center
         :width: 15cm
         :class: with-border
         
         Accept the results when Review is done


Proxy-settings
---------------

If you are behind a firewall, go to *QGIS* -> *Preferences* -> *Network* and will please adjust the proxy settings for plugin connection.

 .. figure:: _static/qgis/proxy_settings.png
         :alt: Proxy settings
         :align: center
         :width: 15cm
         
