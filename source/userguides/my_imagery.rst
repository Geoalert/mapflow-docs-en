.. _My imagery main:

My imagery
===========

.. note::
     ❗️ Currently, you can use *My imagery* in :ref:`Maplfow QGIS plugin <My imagery qgis>` and :ref:`API <Data API>`. The My Imagery Web implementation is in progress.


My imagery in QGIS
----------------------

"My imagery" allows you to collect images in separate collections, called "mosaic". Using this service, users can easily manage their data collections, reuse images for the next processings and analysis with Mapflow models.

.. figure:: ../api/_static/qgis/my_imagery_images.png
         :align: center
         :class: with-border
         :width: 18cm
|

Basic usage:
    - Processing of multiple images at one time. If you are experiencing the processing of multiple images in one area, this tool will be helpful.
    - Reusing of the uploaded images for the next processings
    - Adding tags to the imagery collections to make them searchable in the Mapflow projects

The basic scenario of working with "My imagery" service is as follows:
    1. You are creating a mosaic (a set of images)
    2. Optionally add tags to identify the mosaic
    3. Upload your images to the mosaic
    4. Start processing with Mapflow using the whole mosaic or the specific image. With both methods, you can limit the processing area by applying an AOI.

.. warning::
     There are two main **restrictions on uploading images** in the free plan - the image should be no more than *1 GB* and no more than *100,000 pixels* by the side. We have no other restrictions on uploading to the mosaic, but it is important that each uploaded image has the SAME parameters as the rest of the images in the mosaic (pixel size, number of bands, georeference). For example, two images with pixel sizes of 10 cm and 1 m cannot be added to the same mosaic.

.. note::
     Read how to use it in detail in :ref:`Maplfow QGIS plugin <My imagery qgis>`.


My imagery Web
---------------

.. note::
     ❗️The Web app implementation is in progress. But now you can already view the list of your image collections and, if necessary, delete unused ones.

.. |preview| image:: _static/preview_mosaic.png
  :width: 0.6cm

.. |delete| image:: _static/delete_single_mosaic.png
  :width: 0.6cm

.. |more| image:: _static/more_menu.png
  :width: 0.6cm

By default, Mapflow provides a free 1 Gb storage for all new users to upload and process data. If the memory limit is running out (*Memory free* at the bottom of the page), you can either extend your limit by switching to one of the `Premium plans <https://mapflow.ai/pricing>`_ or delete the unused data using this page. After viewing the information about the collection and previewing its images (|preview|), you can delete one collection at a time (|delete|) or several at once via multiselect ((|more|) -> "Delete selected mosaics").

.. figure:: _static/my_imagery_page.png
         :align: center
         :class: with-border
         :width: 18cm
|

.. note::
     Please note that the table lists all your previously uploaded images as separate collections, each with a unique UUID.
     
      .. figure:: _static/select_delete_mosaics.gif
            :align: center
            :class: with-border
            :width: 15cm
      |    
