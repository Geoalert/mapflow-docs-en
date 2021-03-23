Geoalert Urban Mapping API
==========================

 .. attention::
    This API to ready-to-use data service. It provides access to validated datasets according to the current coverage of "urban mapping" project. To start using the API, please, send us a request to help@geoalert.io.

Authorization
--------------

The API uses the ``Basic Auth`` authorization method, for details about how it, click `here <https://en.wikipedia.org/wiki/Basic_access_authentication>`_.


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

Request example (default projection, polygon):

.. code:: json

	https://urban-mapping.geoalert.io/geojson?polygon={"type":"Polygon","coordinates":[[[37.29962647696191,55.64732925994261],[37.29962647696191,55.579658422801145],[37.39575684805566,55.579658422801145],[37.39575684805566,55.64732925994261],[37.29962647696191,55.64732925994261]]]}

Request example (mercator projection, bbox):

.. code:: json

	https://urban-mapping.geoalert.io/geojson?srid=3857&bbox=[4152175.426194705, 7475188.589286174, 4162876.6101546297, 7488526.850721938]
