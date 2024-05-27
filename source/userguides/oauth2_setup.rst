**1. Select the** ``Use OAuth2`` **option in the login window**

.. figure:: _static/oauth2_login/login_oauth_window.png
         :alt: OAuth login window
         :align: center
         :width: 9cm
         :class: with-boarder no-scaled-link

|

**2. Set the master password**

You will be prompted to set a new `master authentication password <https://docs.qgis.org/3.28/en/docs/user_manual/auth_system/auth_overview.html#master-password>`_ - qgis feature to ensure the security of sensitive information storage.

.. figure:: _static/oauth2_login/master_password.png
         :align: center
         :width: 9cm
         :class: with-boarder no-scaled-link

|

**3. Click** ``Log in`` **button**

You will receive the following message, **restart** QGIS before the next steps.

.. figure:: _static/oauth2_login/oauth_restart_qgis_message.png
         :align: center
         :width: 12cm
         :class: with-boarder no-scaled-link

|

**4. After restarting QGIS, click** ``Log in``

You will be redirected to the browser to log in/register in the mapflow system:

.. figure:: _static/oauth2_login/mapflow_login.png
         :align: center
         :width: 12cm
         :class: with-boarder no-scaled-link

|

After successfully logging in, you will receive a message about the successful verification of QGIS OAuth2:

.. figure:: _static/oauth2_login/oauth_message.png
         :align: center
         :width: 12cm
         :class: with-boarder no-scaled-link

|
.. note:: 
  You can close this page

**5. Go back to QGIS**

OAuth login completed!

.. important::
  If you have problems with authorization, you can delete the current authentication config by going to ``Settings -> Options -> Authentication``, select the config and remove it:

  .. figure:: _static/oauth2_login/delete_oauth_config.png
         :align: center
         :width: 15cm
         :class: with-boarder no-scaled-link

|