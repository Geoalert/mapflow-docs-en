Geoalert Urban Mapping API
==========================

 .. attention::
    This API serves ready-to-use datasets. It provides access to validated datasets within the current coverage of "Urban mapping". To start using the API, please, send us a request to help@geoalert.io.

Authorization
--------------

The API uses the (`Basic Auth <https://en.wikipedia.org/wiki/Basic_access_authentication>`_) authorization method.


Geospatial data
---------------

The output data is in geographic coordinate reference system ``EPSG: 4326`` by default.
* Data format - ``GeoJSON``


Querying features with http service
---------------------------------------
The endpoint is: ``https://urban-mapping.geoalert.io/geojson``.  

 
The service streams geojson features, producing a chunked stream as an http response. It should be safe to fetch reasonably large pieces of data.

The target area is specified by request params:  
``bbox`` in the format ``[xmin, ymin, xmax, ymax]``
or  
``polygon`` in the geojson format  
``srid`` specifies the projection of the bbox/polygon (optional)


.. important:: 
 	``POST`` requests are also supported (with the same endpoint url). ``Bbox`` or ``polygon`` is then supplied in the request body. Other request parameters work as with ``GET`` requests. This option may be useful for querying features by a complex polygon, which doesn't fit into ``GET`` request limits.


**Request example** (default projection, polygon, returns centroids):

.. code:: json

	https://urban-mapping.geoalert.io/geojson?polygon={"type":"Polygon","coordinates":[[[37.29962647696191,55.64732925994261],[37.29962647696191,55.579658422801145],[37.39575684805566,55.579658422801145],[37.39575684805566,55.64732925994261],[37.29962647696191,55.64732925994261]]]}

**Request example** (mercator projection, bbox):

.. code:: json

	https://urban-mapping.geoalert.io/geojson?points=true&srid=3857&bbox=[4152175.426194705, 7475188.589286174, 4162876.6101546297, 7488526.850721938]


Response body example
---------------------

.. code:: json

   {
    "type":"FeatureCollection",
    "features": [
            {
                  "type": "Feature",
                  "geometry": {
                          "type": <"Point" OR "Polygon">, # "Point" if points=true else "Polygon" 
                          "coordinates": <coordinate array> # in lon, lat order; 1-d for points, 3-d for polygons
            },
            "properties":  {
	    	"id": <int> # sequential feature id,
		"processing_date": <date> # the date the processing was ran in our platform (not the image capture date),
		"ground_area": <float> # total area of the building's footprint,
		"height": <int>,
		"volume": <float> # building_height multiplied by ground_area,
                "estimated_population": <int>,
		"residential_floor_count": <int> # for buildings taller than 15m, (height / 3) - 1 since those usually have an attic; otherwise, (height / 3) 
		"in_zkh": <bool> # whether a match was found in the Reforma GKH database (if false, the fields below will be empty),
                "unit_count_residential": <int>,
		"unit_count_total": <int>,
                "floor_area_total": <float> # sum of areas of all floors (as reported by Reforma GKH), sq. m,
		"floor_area_residential": <float> # total floor area of residential units (as reported by Reforma GKH), sq. m,
                "is_rundown": <bool> whether the building is to be demolished,
                "year_of_construction": <int>,   
		"project_type": <string> # aribitrary string: building type or project series
       }
   }

   
API reference
-------------


   .. tabularcolumns:: |p{5cm}|p{5cm}|p{5cm}|p{12cm}|

   .. csv-table::
      :file: _static/api_ref_um1.csv 
      :header-rows: 1 
      :class: longtable
      :widths: 1 1 1 1
