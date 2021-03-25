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
		"shape_type": <string> # auxillary field, should be ignored,
                "population": <float> # estimated number of inhabitants,
		"in_zkh": <bool> # whether a match was found in the Reforma GKH database (if false, the fields below will be empty),
                "living_quarters_count": <int> # number of residential units,
                "area_total": <float> # total floor area of the building, sq. m,
                "project_type": <string> # arbitrary string,
                "floor_count_max": <int> # max number of floors for multipart buildings,
                "floor_count_min": <int> # min of floors for multipart buildings,
                "processing_date": <date> # the date the processing was ran in our platform (not the image capture date),
                "is_alarm": <bool> whether the building is decrepit and scheduled for demolishing,
                "area_residential": # total floor area of residential units, sq. m,
                "built_year": <int> # the year the building was built,
                "house_type": <string> # arbitrary string like "duplex", etc., in Russian,
                "quarters_count": <int> # total number of units,
                    
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
