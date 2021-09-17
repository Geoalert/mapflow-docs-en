Authorization to work with Mapflow API
======================================

To access the platform from external applications such as :doc:`plugin for QGIS <../api/qgis_mapflow>` you need to get the **API token**.
Token must be passed in the **Basic Auth** authorization parameters as a password, and as a login you must transfer your login from your account to Mapflow.ai.

.. note::
    An example of authorization in an application for QGIS:

 .. figure:: _static/api_token_login.png
  :alt: Preview map
  :align: center
  :width: 12cm

Authorization in a Web application and obtaining an API token
-------------------------------------------------------------

1. Open the web application `Mapflow <https://app.mapflow.ai>`_. Register a new account or sign in using your Google account.

2. Go to `user profile settings <https://app.mapflow.ai/account>`_ to generate a new API token.

.. figure:: _static/api_tab.png
    :alt: Preview map
    :align: center
    :width: 8cm

.. attention:: 
  Make sure you save the token, otherwise you will need to reissueit.