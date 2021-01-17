
Mapflow Web UI
================

Open Web App following the link https://app.mapflow.ai/.

Register or login using your Google account.

How to run your flow
---------------------

Our platform is very easy to use. The step-by-step process of starting processing is reflected and described below: 

.. figure:: _static/ui_flow_basic.png
   :alt: UI Mapflow – run flow
   :align: center
   :width: 15cm

1. Data source

 The Mapflow platform receives remote sensing data from global sources, including commercial satellite imagery providers. At this step, you can take advantage of these possibilities and specify a **geographic area on the map** or **a data source / image file** for which processing should be carried out.
   
  1.1. Mapflow resources

  Just use the proposed map, to select the area of processing you need in Mapflow. Find your processing area directly on the map, zooming in and out, as well as moving around it, or use the search bar above the map. After finding the desired area, select the desired area in a square for further processing. 
   
  .. figure:: _static/ui_map_select_source.png
    :alt: UI Mapflow – define AOI
    :align: center
    :width: 15cm

  1.2. Processing your data

  You can upload your own RS data for processing. To do this, drag the desired file to the file upload area or click on the area to find it on your device.

  .. attention::
   Try GeoJSON - it's the most popular format for geographic object to display them on web maps. 

  GeoJSON sample:

  .. code:: json

    {
      "type": "Polygon",
      "coordinates": [
        [
          [
            37.490057513654946,
            55.923029653520395
          ],
          [
            37.490057513654946,
            55.949815087874605
          ],
          [
            37.54308202484029,
            55.949815087874605
          ],
          [
            37.54308202484029,
            55.923029653520395
          ],
          [
            37.490057513654946,
            55.923029653520395
          ]
        ]
      ]
    }

  :download:`Download GeoJSON <_static/_downloads/buildings_aoi.geojson>`

  .. important:: 
   Currently the only one source by default is selected (**Mapbox Satellite**) using Mapflow Web App. See **API DOC** if you want to define your own input data source or upload GeoTIFF image.

2. AI model

 Select one of the **Mapping models** (:doc:`See Models description <pipelines>`).

3. Options

 Select the additional options available for the Model (e.g. "Typology" and "Heights" for the "Building" model).

 .. important:: 
   Building Heights option is limited by the minumum area of the processing (from 50 sq.km).
 
4. Run the processing

 .. attention::
   After you choose the Mapping model and the processing params – you will see the total score of your processing cost. You have 500 credits on your account, which are credited when you register to get acquainted with the Mapflow functionality (: doc:`See the tariff plan <prices>`).


Working with results
---------------------

The processing results are saved in the "Job history" panel.
When this panel is opened, the status is displayed, and the previously selected processing parameters are highlighted in the main window.

.. figure:: _static/preview_button.png
   :alt: Preview results
   :align: center
   :width: 7cm

After finishing the processing, you can view the results on an interactive map or download it as vector geodata (GeoJSON).

 .. important:: When you restart it with the same parameters, a new processing is started.

Options for displaying processing results:

1. Download **GeoJSON** - a geodata format that is natively supported by web map libraries like **Leaflet** (https://leafletjs.com/) or GIS like **QGIS** (https : //qgis.org/).

2. "Open with geojson.io" - viewing results in an external application using a direct link from Mapflow - example: `geosjon.io <http://geojson.io/#data=data:application/json,%7B%22type%22%3A%20%22Polygon%22%2C%20%22coordinates%22%3A%20%5B%20%5B%20%5B%2037.490057513654946%2C%2055.923029653520395%20%5D%2C%20%5B%2037.490057513654946%2C%2055.949815087874605%20%5D%2C%20%5B%2037.543082024840288%2C%2055.949815087874605%20%5D%2C%20%5B%2037.543082024840288%2C%2055.923029653520395%20%5D%2C%20%5B%2037.490057513654946%2C%2055.923029653520395%20%5D%20%5D%20%5D%7D>`_.

 .. note::
  Also, by clicking the link geojsonn.io `geosjon.io <http://geojson.io/#data=data:application/json,%7B%22type%22%3A%20%22Polygon%22%2C%20%22coordinates%22%3A%20%5B%20%5B%20%5B%2037.490057513654946%2C%2055.923029653520395%20%5D%2C%20%5B%2037.490057513654946%2C%2055.949815087874605%20%5D%2C%20%5B%2037.543082024840288%2C%2055.949815087874605%20%5D%2C%20%5B%2037.543082024840288%2C%2055.923029653520395%20%5D%2C%20%5B%2037.490057513654946%2C%2055.923029653520395%20%5D%20%5D%20%5D%7D>`_, you are given the opportunity to view the results and save them in other formats (CSV, KML, GeoJSON, topojson, WKT, Shapefile). To do this, select Save and the format you want in the menu bar.

 .. figure:: _static/geojson.io.png
   :name: Preview map
   :align: center
   :width: 15cm

3. "View on the map" shows the result of processing on top of the original image. This is the fastest way to view the results.

.. figure:: _static/preview_map.png
   :alt: Preview map
   :align: center
   :width: 15cm


Working with API
^^^^^^^^^^^^^^^^

Mapflow platform provides a Rest API to query for running processings and getting results.
If you are developing application and want to use API - check :doc:`../docs_api/processing_api` and contact us at help@geoalert.io.

