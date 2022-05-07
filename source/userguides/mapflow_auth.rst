Authorization to Mapflow API
============================

To access from external applications such as :doc:`plugin for QGIS <../api/qgis_mapflow>` you need to get **API token**. Users can register and obtain token at 
`https://app.mapflow.ai/account/api <https://app.mapflow.ai/account/api>`_.
Token must be passed in the **Basic Auth** parameters like in the example:

.. code:: curl

    curl --location --request GET 'https://api.mapflow.ai/rest/projects/default' \
    --header 'Authorization: Basic <YOUR TOKEN>'  


Authorization in a Web application and obtaining an API token
-------------------------------------------------------------

1. Open the web application `Mapflow <https://app.mapflow.ai>`_. Register a new account or sign in using your Google account.

2. Go to `user profile settings <https://app.mapflow.ai/account>`_ to generate a new API token.

.. figure:: _static/api_tab.png
    :alt: Preview map
    :align: center
    :width: 8cm

.. attention:: 
  Make sure you save the token, otherwise you will need to reissue it.

.. note::
    An example of authorization in an :doc:`application for QGIS <../api/qgis_mapflow>`:

 .. figure:: _static/api_token_login.png
  :alt: Preview map
  :align: center
  :width: 10cm
