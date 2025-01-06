.. _My imagery main:

My imagery
===========

"My imagery" allow you to collect images in separate catalogs, which we call "mosaic". If you are faced with the task of processing multiple images in one area, this tool is for you.

.. hint::
    *Mosaic* - a set of images covering a specific area.

Basic usage:
    - Processing of multiple images at one time
    - Reusing already uploaded images in the past for future processings

The main scenario of working with My imagery is pretty simple:
    1. You are creating a mosaic (a set of images)
    2. Upload your images to it
    3. And start processing (for the whole mosaic or for one image in the mosaic. Also, with both methods, you can limit the processing area by choosing an AOI)

.. note::
     Learn how to use *My imagery* in Maplfow :ref:`QGIS plugin <My imagery qgis>` and :ref:`API <Data API>`

.. warning::
     There are two main **restrictions on uploading images** - the image should not be more than *10 GB* and *100,000 pixels* on the side. We have no other restrictions on uploading to the mosaic, but it is important that each uploaded image has the SAME parameters as the rest of the images in the mosaic (pixel size, channel set, georeference), i.e. two images with pixel sizes of 10 cm and 10 m cannot be in the same mosaic.
