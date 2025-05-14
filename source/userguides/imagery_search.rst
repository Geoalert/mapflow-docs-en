.. _Imagery search  main:

Imagery search
================

"Imagery search" allows Mapflow users to search for available satellite imagery over their area of analysis.
It's powered by Mapflow API providing access to the global satellite data providers and partners. 

Imagery providers available for the search and ordering:
    * ORBVIEW (aggregates and provides satellite imagery from the leading Chinese satellite operators)

Imagery providers supported for the account-based integration:
    * ArcGIS Worldview
    * :ref:`Maxar secureWatch / MGP <Maxar SecureWatch>`

.. note::
    Read more about how to use :ref:`Imagery providers` with Mapflow.


Using Imagery Search in Mapflow WEB
--------------------------------------

.. image:: _static/historical_data_tab.png
  :alt: Imagery search tab
  :align: center
  :width: 16cm
  :class: with-border no-scaled-link  

|

To start the processing using the Imagery Search data, you must:

1. Select a date range or a specific date;
2. Set the search parameters (Clouds, Off-Nadir, AOI/Scene intersection);
3. Apply provider filters:

    - "Mosaic" (Global mosaic 2022, ArcGIS World Imagery)
    - "Image" (Orbview)
    - "Available for me" - The search results will show only those providers that are connected to your account.

.. note::
    Filters and search parameters also work in real time for the list of images; for example, you can hide all images from the table or filter only the results from the providers that are available for you.

4. After clicking "Search Image", a table with search results and images extents will appear:

.. figure:: _static/historical_data_images.png
  :alt: Imagery search results
  :align: center
  :width: 16cm
  :class: with-border

|

5. You can sort, enable or disable images on the map, and preview them if the provider supports this feature (The preview will be automatically added to the map after selecting the image in the table);

.. image:: _static/search_table.png
  :alt: Search table
  :align: center
  :width: 14cm
  :class: with-border no-scaled-link  

|

6. At the final step, you need to select the desired image by clicking on it in the table and click "Save". Now you are ready to start processing!


Using Mapflow Imagery Search in QGIS
--------------------------------------

1. Switch to the tab "Imagery Search". To start the search, set the dates and the product type filters ("Mosaic" – Imagery basemaps like ArcGIS or Global mosaic and/or "Images" - Satellite imagery archives)
2. Set additional filters like a minimum intersection with your area of analysis.
3. If there is non-empty response, it will add the **🔎 Imagery Search metadata** layer to your QGIS project. You can select one or multiple results in the table - or use the layer's attribute table to start the analysis and processing with Mapflow models.

.. figure:: _static/img_search_qgis.png
         :align: center
         :class: with-border no-scaled-link
         :width: 18cm
|

.. hint::
    In the Arcgis search results you see the zoom level at which the mosaic is available over you area. You can configure the table columns in the Settings.

.. figure:: _static/arcgis-new-plugin.gif
         :align: center
         :class: with-border no-scaled-link
         :width: 18cm
|