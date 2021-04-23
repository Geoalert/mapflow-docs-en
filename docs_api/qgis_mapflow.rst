QGIS
=============

 .. attention::
    This application enables to use Mapflow processing capabilities in QGIS (qgis.org). To start using you need :doc:`processing_api` access, please, send us a request to **help@geoalert.io**


What is QGIS
---------------

QGIS is the leading and most popular Open Source Desktop GIS. Users can visualize, manage, edit, analyse data, and compose printable maps. Get a first impression with a more detailed feature list.
Know more on QGIS `official site <https://www.qgis.org/>`_. It has an interface for external Python plugins that allows to connect more apps and extend core functionallity. Our app enables connection to Mapflow :doc:`processing_api` to run AI-mapping processings and download output data as QGIS layers.


User interface
--------------






How to install the plugin
--------------------------

You have to add external repository from our site, click *Plugins* --> *Manage...* --> *Add…* and fill out the form with a name and the `URL to repository <https://qgis.mapflow.ai/mapflow.xml>`_. 

 .. figure:: _static/qgis/add_repo.png
         :alt: Add repo
         :align: center
         :width: 15cm

You will be able to see then if the newer version of the app is available and to check the changelog for details.

  
How to connect to Maxar SecureWatch
------------------------------------

.. note::
 SecureWatch is a service that provides flexible access to high-resolution satellite images and imagery basemaps from the world leader in remote sensing, MAXAR. The spatial resolution of images varies in the range from 30 cm to 1 m. All images are accompanied by metadata, including information about the acquisition date and time, cloud cover etc.

1. On the **Processing** tab, in the *Imagery source* drop-down list, select *Custom (in setting)*.
 
 .. figure:: _static/Geoalert_processing.png
         :alt: Processing dialog
         :align: center
         :width: 15cm

2. Go to the **Settings** tab.
 
3. Enter your SecureWatch account credentials in the *Login* and *Password*.
 
.. important:: 
  If you don't have an account, you need to apply to Maxar `SecureWatch <https://explore.maxar.com/securewatch-demo>`_.
 
4. Select *Maxar Securewatch*. Enter your *Connect ID*. In order to copy your *Connect ID*:

     1.Go to `SecureWatch <https://securewatch.digitalglobe.com/myDigitalGlobe/logout-from-ended-session>`_.

     2.In the title bar select your name, then select **View Profile**. The **User Profile** dialog box will open.
 
     3.Copy your **Current Cnnect ID**.
     
     .. figure:: _static/SecureWatch_user_profile.jpg
         :alt: Your user profile in SecureWatch
         :align: center
         :width: 15cm

     .. attention::
         The **Connect ID** is different for each product you have in your SecureWatch subscription. Therefore, initially choose the one that suits you. To do this, close the *User Profile* window and in the title bar select the required of the two suggested mosaics (**Vivid** and **SecureWatch**) by clicking on the name of one of them.
 
     4. Return to QGIS to **Geoalert plugin**, paste the copied ID in the *Connect ID* input.
     
     5. Click *Get URL*.

     6. 
     
     Now the Maxar layer is available for preview in your raster layers list and for the AI-mapping processing using Mapflow.
     

How to use other imagery services
------------------------------------

You can enter your custom imagery source URL in one of the following formats:

* XYZ
* TMS
* WMS

All formats represent the most widely used protocols to fetch gereferenced imagery via http:
(There is one more type that is supported in the Mapflow which is *quadkey*)


How to process your own imagery data
------------------------------------

You can upload your local raster in GeoTIF format (*Open new .tif*). Every file added as raster layer into QGIS is visible in the drop-down list and can be selected for uploading.

 .. figure:: _static/qgis/upload_tif.png
         :alt: Upload TIF, select from list
         :align: center
         :width: 15cm
