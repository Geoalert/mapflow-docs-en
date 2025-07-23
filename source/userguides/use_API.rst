Mapflow API guides
====================

How to run bulk processing using Mapflow API
------------------------------------------------

In case you have multiple polygons to process or update, it can be boring to upload them one by one using Web or GIS user tools. In this case, you'd better think of using Mapflow :ref:`Processing API`.
In this example let's assume we have a list of polygons indicating the populated places borders and we want to extract features like "buildings" with Mapflow processing API.

1. To make it more realistic let's download some populated places borders for the sample area in Uzbekistan using Openstreetmap.
To do this we can make a query with Overpass Turbo API like this:
We can use QuickOSM plugin in QGIS which is very friendly when it comes to downloading a managable volume of data from Openstreetmap.  

.. figure:: _static/python_examples/quickosm.jpg
    :alt: quickosmm
    :align: center
    :width: 15cm
    :class: with-border no-scaled-link
|

Authorization with Mapflow token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's use Mapflow token for further authorization. 

.. code:: python

    import base64

    token = input("token:") # Your Mapflow token goes here. Obtain it at https://app.mapflow.ai/account/api

    username, password = base64.b64decode(token).decode().split(':')
    print(username, password)

Now you get your token decoded as a username and a password and use it for the authorization with the requests.

Create the project (it's optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. hint::
   It might be useful to organise your processing with the **projects**. To do this create the new project with the following API method.

.. code:: python

    import requests
    import json

    url = "https://api.mapflow.ai/rest/projects"
    headers = {
        'Content-Type': 'application/json'
        }

    payload = json.dumps({
            "name": "My new project"  # Your project name
        })

    response = requests.request("POST", url, headers=headers, auth=(username,password), data=payload)

    if  response.status_code == 200:
        print(response.text)
    else:
        print(f"Request failed")
        print(response.text)

Here we get the response containing the project ID, that we can use to create the processings in this specific project. 

Response example:

.. code:: json
    
        {
        "id": "fb49b97e-51ec-4b31-872f-d1411284de85",
        "name": "My new project",
        ...
    }

See more in :ref:`Projects - API`

Prepare AOIs for the processings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's save areas of interest with the properties as a GeoJSON file as it's simple and straightforward format to be used in any application or GIS software. 
Then we open this file and create a python dictionary to loop through all GeoJSON features that we are going to use as AOI geometries for creating the processing. Like this:

.. code:: python

    with open('<path to the file>', 'r') as file:  # Define your GeoJSON file path
    geojson_data = json.load(file)

    for feature in geojson_data['features']:
        name = feature['properties']['name']   # Extract the "name" property from OSM data
        print(name);

Let's check if we created the data array from our file and display all the features by their names. At the next step, we will use the ``name`` property to define the processing. The "name" is optional yet it's more convenient to work with the results afterwards.

Run the Processings
~~~~~~~~~~~~~~~~~~~~

Now we are ready to create the processing for each AOI using its geometry.  

.. code:: python

    url = "https://api.mapflow.ai/rest/processings"

    for feature in geojson_data['features']:
        name = feature['properties']['name']
        geometry = feature['geometry']
        payload = json.dumps({
            "name": name, 
            "projectId": "fb49b97e-51ec-4b31-872f-d1411284de85",  # Here is your project Id to link the processing to the specific project. 
            "wdName": "🏠 Buildings",
            "geometry": geometry
        })
        response = requests.request("POST", url, headers=headers, auth=(username,password), data=payload)

        if  response.status_code == 200:
            print(f"Request successful: {name}")
        else:
            print(f"Request failed for feature: {name}")
            print(response.text)


If everything was done correctly - the list of successfully created processing will be displayed.


Download all the results using Mapflow API
-------------------------------------------

When all processings are complete you can download easily the results for each one.

If you have one processing with the multiple AOIs *(by default the number of AOIs in one processing is limited to 10)* you can run a single API call to download the results:

.. code:: bash

    curl --location 'https://api.mapflow.ai/rest/processings/<ID>/result' \
    --header 'Authorization: Basic <YOUR API TOKEN>' -O <YOUR PATH TO FILE>.geojson

In case of the multiple processings, you might find it useful to run the small script.

1. Get the list of all "ids" and "names" by processing:

.. code:: python

    import requests
    import json

    url = "https://api.mapflow.ai/rest/projects/fb49b97e-51ec-4b31-872f-d1411284de85/processings"

    response = requests.request("GET", url, auth=(username,password))

    json_data = response.json()

    values = []
    for item in json_data:
        if "id" in item and "name" in item:
            values.append((item["id"], item["name"]))

    if  response.status_code == 200:
        for id, name in values:
            print(f"{id}, {name}")
    else:
        print(response.text)


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

    output_json = '<path to the folder>' # Define local folder to save files

    for id, name in values:
        response = requests.request("GET", url + id + '/result', headers=headers)

        if  response.status_code == 200:
            with open(output_json_file + name + '.geojson', 'w') as geojson:
                geojson.write(response.text)    
                print(f"File saved")
        else:
            print(f"Request failed")
            print(response.text)
