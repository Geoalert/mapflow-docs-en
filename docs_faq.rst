Mapflow FAQ
============

Payment
---------
**How are payments made for using the platform? How much is it?**

    In accordance with the User Agreement, the cost of the Services is determined in conventional units, Credits, where 1 Credit is equal to USD 0.1. To make a payment, go to the Settings of your personal account, or click on the balance icon and select the required number of credits (the equivalent in Russian rubles is displayed under the nominal value of credits). Our `tariffs <https://docs.mapflow.ai/docs_userguides/prices.html>`_.

**Can I get spent funds if I’m not satisfied with the processing results?**
    
    The funds spent are not refundable. Upon registration, we give you 500 credits to test Mapflow functionality. For a more detailed solution to the issue, you can write to us at help@geoalert.io.

**I represent a company and would like to perform large volumes of processing, do you have corporate rates?**

    We don’t, but you can email us at help@geoalert.io to discuss this issue privately.


Satellite imagery
------------------

**What satellite imagery do you use? What are their resolution, alignment accuracy and other characteristics?**

    Currently, we only support RGB or PAN images as raw data. By default, Mapflow uses the `Mapbox Satellite <https://www.mapbox.com/maps/satellite>`_ satellite mosaic, which primarily consists of **Vivid Basic** imagery from Maxar. These images have a spatial resolution of 0.5m, the georeferencing accuracy is about 3-5m and the age is no more than two years. A complete list of specifications can be found `here <https://cdn1-originals.webdamdb.com/13264_94721902?cache=1596135643&response-content-disposition=inline;filename=10009-ds-imagerybasemaps-07-2020.pdf&response-content-type=application/pdf&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cCo6Ly9jZG4xLW9yaWdpbmFscy53ZWJkYW1kYi5jb20vMTMyNjRfOTQ3MjE5MDI~Y2FjaGU9MTU5NjEzNTY0MyZyZXNwb25zZS1jb250ZW50LWRpc3Bvc2l0aW9uPWlubGluZTtmaWxlbmFtZT0xMDAwOS1kcy1pbWFnZXJ5YmFzZW1hcHMtMDctMjAyMC5wZGYmcmVzcG9uc2UtY29udGVudC10eXBlPWFwcGxpY2F0aW9uL3BkZiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MjE0NzQxNDQwMH19fV19&Signature=UXBlDqy95IXlX6saByLkbIJs6E2kRhhCpGbgfZSzvZO69NmERBUUG2wWv1Ax4mC5kg7Zfet6hcIltSGE7qUiidd~gT8Cjo8RCcBp4IFoxZ8Hi8v3y3MCbGcRbwFugwA1-rfnG6bdGjtgIX1AuFKekobv1njziOw3IrihyBTytV9g7mQHELLYuSuHwuzBb~z2~uw1ySdDUjGUlFYMxxV5Ispg6pvhws98Yv~e31ARjwirUyUCDOCVko1Ch9~MoSbWEU-Zt8Iq~oPhSiWOOPL2Ihr~SxEsP4p4nKJNzdF8ShexLxXSxRaiMR2~3595LoIk9pO~XvRZm~VjSFDo~DKNOA__&Key-Pair-Id=APKAI2ASI2IOLRFF2RHA>`_.

**Can I choose another satellite mosaic like Yandex or Google?**

    Yes, the user has the ability to set his own XYZ or TMS layers. Under a separate user license, we provide Maxar SecureWatch, a service that contains an enhanced version of Vivid Basic and updates.

**Can I upload my own images for processing?**

    Yes, but only when using the `Geoalert API <https://ru.docs.mapflow.ai/docs_api/processing_api.html>`_ or `plugin Mapflow for QGIS <docs_api/qgis_mapflow>`_. It is planned to add this functionality to Mapflow Web in the next releases.


**Can I buy satellite imagery from you?**

    No, you can’t.  We only sell vector data that we have extracted from images.

**Can you control the channels of the RGB data used?**

    In the current version, the Mapflow platform uses only the standard set and configuration of RGB channels.


**Can I use non-RGB data like radar data?**

    No, you can’t. We currently don’t support SAR imagery as raw data.

Vector data
------------

**Can I download the results in a format other than GeoJSON?**

    Yes, you can. To do this, in your *Project* in the *Results* tab, select *“Open in geojson.io”*, then, in the menu bar, select *Save* and the format you need (you can save in formats: CSV, KML, GeoJSON, TopoJSON, WKT, Shapefile).

**Can I load a processing area from a format other than GeoJSON?**

    No, you can’t, the platform currently only supports **GeoJSON**. You can use geojson.io or the QGIS desktop application to convert your dataset to GeoJSON.

**Is it possible to process multiple areas in one treatment?**

    Only one area can be drawn or loaded for one processing at the moment. If your GeoJSON has multiple scopes in the FeatureCollection, only the first one will be used. If you want to process multiple areas, you can split them into separate files and start processing for each.

**Results contain gaps / false contours / inaccuracies / errors in classification and / or heights. Why?**

    The images are processed by artificial intelligence, so inaccuracies may occur. We are constantly improving our models and neural networks, but 100% of the result can be achieved only by combining automatic processing with subsequent validation.


Projects and treatments
------------------------

**What is a “project”? Do I have to create every new treatment in a new project?**

    **Project** allows you to collect all logically related processing for a more efficient and faster search for the one you need. It's like a folder on your computer. One project can have many treatments.

**Immediately after registration, I got a project called “Demo processings”. What is it and why?**

    This project allows you to get acquainted with the capabilities of Mapflow without using Credits. In the History of treatments, you can select the treatment you are interested in and see its results. It is also possible to view the selected processing parameters, to do this, click **use as template**.

**Can I rename a project/processing?**

    It isn't possible to rename a project/processing at the moment. Planned for the next release.

**Are there any restrictions on the processing area?**

    Yes, the processing area must be at least 1 sq. km and no more than 100 sq. km. If you need to process a large area, you can divide the area to be treated into several smaller areas, one per file, and start processing for each.

**Why are the options for Building heights and Forest heights only available when processing over 50 sq. km?**

    Calculating heights requires additional resources from us. At this stage, we can perform a limited number of such processing. In the future, we are going to reduce this limitation or completely remove it.

Support and other questions
----------------------------

**Do you have any documentation on working with the platform?**

    `Yes, we do <https://ru.docs.mapflow.ai/index.html>`_.

**Do you have an API?**

    `Yes, we do <https://ru.docs.mapflow.ai/docs_api/processing_api.html>`_.

**Do you have GIS integration?**

    Yes, we do. Our `plugin Mapflow <docs_api/qgis_mapflow>`_for the open GIS `QGIS <https://qgis.org/ru/site/forusers/download.html>`_. 
    
**I have another question, where can I ask it?**

    You can ask your question on the Mapflow website in the online chat, where we will answer your questions in real time. Also, you can write to us at help@geoalert.io.
