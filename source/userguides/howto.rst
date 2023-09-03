.. _howto:

Userguides - How To
===================

How to change the data type of your image to Uint8 bit in QGIS
--------------------------------------------------------------

1. Check the data type of your image. 
Right-click on the imagery layer - i - Information from provider. The Data type must be Byte. Follow the next steps if the Data type is Int16, Float 32 etc.

    
    .. figure:: _static/information.png


  

2. Right click on your image Layer Properties -  Symbology tab, then customize the display of your image. Select desired channels for Band rendering, adjust brightness and contrast. 
      
    
    .. figure:: _static/symbology.png



3. Right-click on the layer’s name, go to the  Export in the context menu, Save as…

 
    .. figure:: _static/export.png
    


4. Check Output mode as Rendered Image


    .. figure:: _static/save_raster.png
    


5. Save your image  - navigate to the desired folder, input the file name then click OK



6. Use the new image layer as Imagery source when using the Mapflow plugin for QGIS


How to process your own UAV imagery with Mapflow
------------------------------------------------

Unmanned aerial vehicles – UAVs or, more commonly, drones – have become a deeply integrated part of the geomatic industry over the last ten years. This is owing to their increasing usability, falling hardware costs, and easing government regulations. Yet, as more data is available with UAV surveys, more data need to be processed operatively. 
To process your UAV data you might be looking for some cloud or desktop software to create a mosaic or orthophoto.  Do you know that you can easily publish your data with Openaerialmap and analyze (say detect and calculate some objects and calculate their areas) with Mapflow QGIS or Mapflow Web? 

Let’s take the “UAV buildings” :doc:`buildings_aerial_imagery_model` model that extracts the detailed building outlines (the recommended image resolution is 10 cm).

Processing with Mapflow Web
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Select raster source – you can either use Custom URL (see below how to publish your image with Openaerialmap and get the TMS link) or upload your image as GeoTIFF.

.. image:: _static/select_provider_2.png
            :align: center
            :class: with-border
            :scale: 50

.. warning::

    *Currently, a preview of the uploaded image is not possible after loading the image, you will see only the area of its extent.*

2. Define the processing Area.
The processing area (AOI) must be located within the area of the image extent, otherwise, the area will be cut off by the extent boundaries. The processing area size is calculated by the intersection of the image extent and the AOI.

.. important::

    Image upload requirements:
    The file size must be less than 512 mb. Both sides image dimmesions must not exceed 30.000x30.000

    The image must be georeferenced and the CRS must be one of:
    * WGS84 (EPSG: 4326)
    * Web mercator (EPSG: 3857)
    * UTM (any zone)

    If your image doesn’t meet the parameters, we suggest using Mapflow API / QGIS plugin which has more capabilities.
    Mapflow supports RGB imagery and also processes single-band (panchromatic) imagery, but the AI models are not tuned for such kind of data, so the quality of the result may be worse than expected.


Processing with Mapflow – QGIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case you are already used to working with QGIS you need to install the Mapflow plugin. You can upload your own GeoTIFF (up to 1 GB, max. 30000x30000 px.). All raster layers currently loaded in your QGIS (1) are visible in the drop-down list (2) and can be selected for upload. 
Open files in the Additional options (3) also adds your item to the tree of QGIS layers.

    .. image:: _static/select_raster_qgis.png
       :align: center
       :class: with-border

.. important::

    Please, consider the requirements specified on the page with Models reference when uploading your own images for AI-mapping processing. Contact us if you have a large dataset of images or your file size exceeds our limits.

Use Openaerialmap as an imagery publication tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`OpenAeriaMap <https://map.openaerialmap.org>`_ is an open collection of UAV imagery data, crowdsourced by users. The project is supported by a consortium of companies developing open source software and services for working with geospatial data.
As soon as your aerial image is published on Openaerialmap it’s displayed on the public map and can be streamed using TMS/WMTS protocols or downloaded as GeoTIFF file. 
Both ways are OK to work with Mapflow.

    .. image:: _static/oam_search.png
       :align: center
       :class: with-border

1. Copy link to TMS and paste it into the “Custom imagery URL” in your new Mapflow processing. 
2. Check if you see the image on the map, go through the next steps (AI model, processing params) to and start the processing.

Preparing and optimizing the large size images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here are few tips on how to prepare and optimize your data and reduce the image size to upload it faster and not to exceed the Mapflow upload limit.

Usually UAV image is an RGB compiosite provided as GeoTIFF of 16 or 8 bit. 
The type must be Byte (8 bit). If the Data type is Int16 or Float32 etc, please follow the instruction :doc:`howto`.
Alternatively: use the `preprocessing script <https://github.com/Geoalert/mapflow_data_preprocessor/>`_ for preparing your image for Mapflow processing.

You can reduce the size of the image using GDAL translate. (https://gdal.org/)
E.g. using JPEG compression.
``gdal_translate -co compress=JPEG input.tif output.tif``
By default the compression quality is 75% (``gdal_translate -co compress=JPEG -co jpeg_quality=75 input.tif output.tif``) but it doesn’t really impact the quality of the Mapflow mask whenever the resolution of the input iage meets the recommended params.

The same can be done using QGIS interface:

    .. image:: _static/optimize_qgis.png
       :align: center
       :class: with-border


Tell us if you have more tips to share with the community or if you have more questions – we are ready to help.

**Run the flow!**


How to view results using Kepler.gl
-----------------------------------

**Kepler.gl** is an open source tool designed for geospatial data analysis. It is a simple yet powerful for displaying and exploring geodatasets.

To view the processing results in the Mapflow, select the required processing and press the button *"Open in kepler.gl"*.

.. note ::
   You can share your processing view in Kepler by copying the open URL (right click on *"Open in kepler.gl"* --> Copy Link Address)

Using the Kepler you can change the visual properties of data, set filters, and choose a background map.


Layers tab
~~~~~~~~~~~~

Click on the layer name to bring up the *Layer settings* from the drop-down menu. To hide all data, click on the *eye* icon.

.. figure:: ../kepler/_static/view_layer_settings.png
    :alt: View layer settings
    :align: center
    :width: 15cm


These settings allow you to choose a more suitable type of received data:

* *Fill color.* You can choose any color from the palette for polygons, and also hide the display of data by changing the position of the slider. You can change the transparency of polygons (property *Opacity*) in the additional settings of this function.
* *Stroke color.* You can choose any color from the palette for outlining polygons, as well as completely remove the stroke. You can change the transparency of the stroke (property *Opacity*) In the additional settings of this function.
* *Stroke width.* Controls the thickness of the stroke.
* *Height.* Allows you to view data with heights in 3D format. Set the desired coefficient and select the attribute of the layer with heights.

.. figure:: ../kepler/_static/3D_buildings.png
    :alt: 3D buildings
    :align: center
    :width: 15cm


Filters tab
~~~~~~~~~~~~~

This tab allows you to add a filter of interest by a specific attribute of the layer (as in this case, the filter is set by classes with different typology of buildings).

.. figure:: ../kepler/_static/filter_panel.png
    :alt: Filter panel
    :align: center
    :width: 15cm


Interaction tab
~~~~~~~~~~~~~~~~~

You can select or remove attributes that will be visible in the menu that appears when you hover over an object. It is also possible to turn on the panel indicating longitude and latitude.

.. figure:: ../kepler/_static/interaction_panel.png
    :alt: Interaction panel
    :align: center
    :width: 15cm
    :class: with-border no-scaled-link


Base map tab
~~~~~~~~~~~~~~

Here you can choose the styles of the map, as well as choose to display its various layers.


.. include:: iterative_mapping.rst


How to run a bulk processing using Mapflow API
------------------------------------------------

In case you have many polygons to process it can be boring to upload them one by one using Web or GIS user tools. In this case you'd better think of using Mapflow :ref:`Processing API`.
In this example let's assume we have a number of polygons indicating the settlement borders and we want to extract features like "buildings" within the borders.
To make it more realistic let's download some populated places borders for the sample area in Uzbekistan using Openstreetmap.
To do this we can make a query with Overpass Turbo API like this:

.. code:: xml

    [out:xml] [timeout:25];
    (
        way["place"]( {{bbox}});
    );
    (._;>;);
    out body;

Alternatively, we can use QuickOSM plugin in QGIS which is very friendly when it comes to downloading not a very large volume of data from Openstreetmap.  

.. figure:: _static/python_examples/quickosm.jpg
    :alt: quickosmm
    :align: center
    :width: 15cm
    :class: with-border no-scaled-link

Let's import the required libs that we will use and enter your Mapflow token for further authorization. 

.. code:: python

    import requests
    import json
    import base64

    token = input("token:") # Your Mapflow token goes here. Obtain it at https://app.mapflow.ai/account/api

    username, password = base64.b64decode(token).decode().split(':')
    print(username, password)

Now you get your token decoded in a username and a password and use it for the authorization with the requests.

.. hint::
    To learn more about tokens and authorization see :ref:`Mapflow Auth`


It might be useful to organise your processing with the **projects**. In this case create you project with another API request.

.. code:: python

    url = "https://api.mapflow.ai/rest/projects"
    headers = {
        'Content-Type': 'application/json'
        }

    payload = json.dumps({
            "name": "Test project 111"  # Your project name
        })

    response = requests.request("POST", url, headers=headers, auth=(username,password), data=payload)

    if  response.status_code == 200:
        print(response.text)
    else:
        print(f"Request failed")
        print(response.text)

Here we get the response containing the project ID, and the description of the default AI-models as they are linked to every new project.

Response example:

.. code:: json

            {
            "id": "fb49b97e-51ec-4b31-872f-d1411284de85",
            "name": "Test project 111",
            "description": null,
            "progress": {
                "status": "UNPROCESSED",
                "percentCompleted": 0,
                "details": [],
                "completionDate": null
            },
            "aoiCount": 0,
            "aoiArea": 0,
            "area": 0,
            "user": {
                "id": "78a0215f-243d-429c-a555-e714094da895",
                "email": "georgy@geoalert.io",
                "role": "USER",
                "areaLimit": 1000000000000,
                "aoiAreaLimit": 100000000000,
                "processedArea": 262349176505,
                "created": "2021-10-27T15:54:00.904095Z",
                "updated": "2023-02-01T11:43:04.242524Z",
                "isPremium": true,
                "reviewWorkflowEnabled": false
            },
            "isDefault": false,
            "created": "2023-09-02T12:13:30.528789Z",
            "updated": "2023-09-02T12:13:30.528789Z",
            "workflowDefs": [
                {
                    "id": "168ec337-ee9e-4fa0-bdac-af4a4361aa80",
                    "name": "🏠 Buildings",
                    "description": "Default model: segmentation of buildings. Classification and simplification postprocessing included. Model is selected depending on geographic position of AOI",
                    "created": "2023-02-01T08:58:25.135947Z",
                    "updated": "2023-08-28T14:03:57.027301Z",
                    "pricePerSqKm": 0.0,
                    "blocks": [
                        {
                            "name": "Segmentation",
                            "displayName": "Segmentation",
                            "optional": false,
                            "price": 5.0
                        },
                        {
                            "name": "Postprocessing1",
                            "displayName": "",
                            "optional": false,
                            "price": 0.0
                        },
                        {
                            "name": "Classification",
                            "displayName": "Classification",
                            "optional": true,
                            "price": 3.0
                        },
                        {
                            "name": "Simplification",
                            "displayName": "Polygonization",
                            "optional": true,
                            "price": 5.0
                        },
                        {
                            "name": "OSM",
                            "displayName": "Merge with OSM",
                            "optional": true,
                            "price": 0.0
                        },
                        {
                            "name": "Postprocessing2",
                            "displayName": "",
                            "optional": false,
                            "price": 0.0
                        }
                    ]
                },
                {
                    "id": "7c1c872a-2afe-4186-a459-c4e9d9d675f9",
                    "name": "🚗 Roads",
                    "description": "Default model: roads segementation. The road parts are connected into network when possible, then replaced with polygons for better displey",
                    "created": "2023-02-01T08:58:24.584101Z",
                    "updated": "2023-08-28T14:03:57.247564Z",
                    "pricePerSqKm": 5.0,
                    "blocks": []
                },
                {
                    "id": "f711cefe-6a81-44c9-a1a9-727fb2bdbbb9",
                    "name": "🚜 Fields (hi-res)",
                    "description": "Default model: agriculture fields segmentation.",
                    "created": "2023-02-01T08:58:24.933788Z",
                    "updated": "2023-08-28T14:03:57.405171Z",
                    "pricePerSqKm": 5.0,
                    "blocks": []
                },
                {
                    "id": "a6ccb1d4-e5aa-45a2-9526-111b67b2924b",
                    "name": "🌲 Forest",
                    "description": "Default model: segmentation of forested areas with assinment of height classes; thresholds are 4 and 10 meters",
                    "created": "2023-02-01T08:58:24.377220Z",
                    "updated": "2023-08-28T14:03:57.600319Z",
                    "pricePerSqKm": 0.0,
                    "blocks": [
                        {
                            "name": "Segmentation",
                            "displayName": "Segmentation",
                            "optional": false,
                            "price": 8.0
                        },
                        {
                            "name": "Heights",
                            "displayName": "Height estimation",
                            "optional": true,
                            "price": 20.0
                        },
                        {
                            "name": "Postprocessing",
                            "displayName": "",
                            "optional": false,
                            "price": 0.0
                        }
                    ]
                },
                {
                    "id": "b11c626e-b7de-4f67-ab2c-4567079bc0ca",
                    "name": "🏗️ Construction sites",
                    "description": "Default model: segmentation of possible construction sites. Sensitive to open soil + big construction equimpent",
                    "created": "2023-02-01T08:58:25.030308Z",
                    "updated": "2023-08-28T14:03:57.777228Z",
                    "pricePerSqKm": 4.0,
                    "blocks": []
                }
            ]
        }

.. warning::
    The custom AI-models won't be linked to the new project automatically. 


Let's save Openstreetmap places and the properties as a GeoJSON file as it's simple and straightforward format to be used in any application or GIS software. 
Then we open this file and create a python dictionary to loop through all GeoJSON features that we are going to send as AOI geometries for the processing. Like this:

.. code:: python

    with open('/Users/work/uzb_places_select.geojson', 'r') as file:  # Define your GeoJSON file path
    geojson_data = json.load(file)

    for feature in geojson_data['features']:
        name = feature['properties']['name']
        print(name);

Display the list of all the features by their names. We will use  ``name`` to entitle the processing. The name is optional yet it's more convenient to work with the results afterwards.
Now we are ready to create the processing for each "place" using its AOI geometry.  


.. code:: python

    url = "https://api.mapflow.ai/rest/processings"
    headers = {
        'Content-Type': 'application/json'
        }

    for feature in geojson_data['features']:
        name = feature['properties']['name']  # Extract the "place" name
        geometry = feature['geometry']
        payload = json.dumps({
            "name": name, 
            "projectId": "25a24df3-15e4-42f8-b38a-f3f87f4f84d9",  # Here is our project Id to organize the processing into specific project. It's options
            "wdName": "🏠 Buildings",
            "geometry": geometry,
            "meta": {
                "project": "test"
            }
        })
        response = requests.request("POST", url, headers=headers, auth=(username,password), data=payload)
    
        if  response.status_code == 200:
            print(f"Request successful: {name}")
        else:
            print(f"Request failed for feature: {name}")
            print(response.text)


If everything was done correctly - the list of succesfully created processing will be displayed.


Download all the results using Mapflow API
-------------------------------------------

When all processings complete you can download easily the results for each processing.

If you have one processing with the multiple AOIs you can run a single API call to download the results:
``GET https://api.mapflow.ai/rest/processings/{processingId}/result``

In case of the multiple processings you might find it useful to run this kind of script.

1. Get the list of all the processing IDs and names:

.. code:: python

    import requests
    import json

    url = "https://api.mapflow.ai/rest/projects/25a24df3-15e4-42f8-b38a-f3f87f4f84d9/processings"

    response = requests.request("GET", url, auth=(username,password))

    json_data = response.json()

    for id, name in values:
        print(f"{id}, {name}")


Response example:

.. code:: bash

    5f748822-c94a-4233-ae1e-7622973bf9b5, Бой
    87f258e6-c1ce-4deb-8155-ccd6b21ac237, Авазли
    1e24c0e5-9b6f-4a26-9970-82dfb1f67807, Avazali
    0316606a-4c04-4196-bdab-6495af4bb7b0, Авлиятепа
    38435f06-6b85-420e-86f8-3ebef4755480, Акбуйра
    33ffec93-ef2b-4ead-a51e-30cad1bcb71d, Аксулат
    c8f73cf5-8a44-4c36-8b2e-49b27f7f5da5, Актепа
    6eaca828-41ec-4ce5-aea4-b9f039211bbe, Арабхана
    ...


2. Save results for all the listed processings:

.. code:: python

    output_json = '/Users/work/DATA/' # Define local folder to save files

    for id, name in values:
        response = requests.request("GET", url + id + '/result', headers=headers)
    
        if  response.status_code == 200:
            with open(output_json_file + name + '.geojson', 'w') as geojson:
                geojson.write(response.text)    
                print(f"File saved")
        else:
            print(f"Request failed")
            print(response.text)


.. figure:: _static/python_examples/sample_results.jpg
    :alt: quickosmm
    :align: center
    :width: 15cm
    :class: with-border no-scaled-link