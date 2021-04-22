QGIS
=============

 .. attention::
    This application enables to use Mapflow processing capabilities in QGIS (qgis.org). To start using you need :doc:`processing_api` access, please, send us a request to **help@geoalert.io**


What is QGIS
---------------



User interface
---------------


How to install the plugin
------------------------


  
How to connect to Maxar SecureWatch
------------------------------------

.. note::
 SecureWatch is a service that provides flexible access to optical images from the world leader in remote sensing, MAXAR. The spatial resolution of images varies in the range from 30 cm to 1 m. All images are accompanied by metadata, including information about the shooting date and time, shooting angle and cloud cover, spatial resolution, image processing level, etc.

1. On the *Processing* tab, in the *Imagery source* drop-down list, select *Custom (in setting)*.
 
 .. figure:: _static/Geoalert_processing.png
         :alt: Processing dialog
         :align: center
         :width: 15cm

2. Go to the *Setting* tab.
 
3. Enter your SecureWatch account information in the *Login* and *Password*.
 
.. important:: 
  If you don't have an account, register on the `SecureWatch <https://securewatch.digitalglobe.com/myDigitalGlobe/logout-from-ended-session>`_.
 
4. Select *Maxar Securewatch*. Enter your *Connect ID*:

     1.Go to the `SecureWatch <https://securewatch.digitalglobe.com/myDigitalGlobe/logout-from-ended-session>`_.

     2.In the title bar select your name, then select **View Profile**. The **User Profile** dialog box will open.
 
     3.Copy your connection ID from the **Current Connect ID**.
     
     .. figure:: _static/SecureWatch_user_profile.jpg
         :alt: Your user profile in SecureWatch
         :align: center
         :width: 15cm

     .. attention::
         The **Connect ID** is different for each mosaic. Therefore, initially choose the one that suits you. To do this, close the *User Profile* window and in the title bar select the required of the two suggested mosaics (**Vivid** and **SecureWatch**) by clicking on the name of one of them.
 
     4. Return to QGIS to **Geoalert plugin**, paste the copied ID in the *Connect ID*.
     
     5. Click *Get standart* layer Maxar.

     6. In the *Custom* active area, click *Connect satellite imagery provider*.
     
     Now the Maxar layer is displayed in your raster layers list.
     

How to use other imagery services
------------------------------------


How to process your own imagery data
------------------------------------