Mapflow FAQ
============

Payment
---------
**How to buy credits for using the platform? How much is it?**

    The cost of the Services is determined in conventional units, Credits, where 1 Credit is equal to USD 0.1. To make a payment, go to the Settings of your personal account, or click on the balance icon and select the required number of credits ($50, $90 or $800). See :doc:`Mapflow prices </userguides/prices>`.

**I represent a company and would like to perform large volume of processing. Do you have corporate rates?**

    Check our `commercial plans <https://mapflow.ai/pricing>`_ for Enterprise. Contact our `sales <https://geoalert.io/#contacts>`_ to send your inquiry and get the quotation.

**What if I'm not satisfied with the output? Do you make a refund?**

    * For Free Users: You can use evaluation credits to test our software. If you are unsatisfied with the output, we encourage you to leave feedback and rate the results. We review all ratings from free users, and if we determine the output was unsatisfactory, we may refund the evaluation credits.

    * For Paid Users: If you are on a corporate plan, we commit to meeting a specific level of accuracy. If the output does not meet these requirements, we will refund your credits according to our refund policy.

.. _Satellite images:

Satellite imagery
------------------

**What satellite imagery do you use? What are their resolution, alignment accuracy and other characteristics?**

    Currently, we only support RGB or PAN images as raw data. By default, Mapflow uses the `Mapbox Satellite <https://www.mapbox.com/maps/satellite>`_ satellite mosaic, which primarily consists of **Vivid Basic** imagery from Maxar. These images have a spatial resolution of 0.5m, the georeferencing accuracy is about 3-5m and the age is no more than two years. A complete list of Maxar satellite imagery specifications can be found :download:`here <userguides/_static/_downloads/imagery-basemaps.pdf>`.

**Can I choose another satellite mosaic?**

    Yes, the user has the ability to set his own XYZ or TMS layers. To use Google or some other services you should beware of their terms of use. Under the Mapflow commercial plans, we provide commercial providers access, a services that provide basemaps and imagery updates. We are continuosly working on adding more commercial providers.

**Can I upload my own images for processing?**

    Yes, and we keen on improving the experience of using your data with the Mapflow. Check our :doc:`user guide <> `on how to do it.


**Can I buy satellite imagery from you? How can I validate the results?**

    You can't buy as we don't resell images. We provide service to extract data from images. However you can preview the input images as XYZ layer to conduct the results validation.   

**Can I use non-RGB data like radar data?**

    No, you can’t for default models. You can contact us about the development of the custom model.

Vector data
------------

**Is it possible to process multiple areas in one request?**

    Only one area can be drawn or loaded for one processing at a time. If your GeoJSON has multiple scopes in the FeatureCollection, only the first one will be used (if you start processing via :doc:`our plugin for QGIS <api/qgis_mapflow>`, or *Select object (s)* tool to select one area from the loaded layer with multiple areas). Alternatively, you can convert your GeoJSON into *Mulipolygon*.

**Results contain gaps / false contours / inaccuracies / errors in classification and / or heights. Why?**

    The images are processed by artificial intelligence, so inaccuracies may occur. We are constantly improving our models and neural networks, but 100% of the result can be achieved only by combining automatic processing with subsequent validation.

**Do you provide validation service for automatic results?**

    Mostly, we provide service and a reasonable customization to the project requirements (model fine-tuning). However, depending on the project requirements the validation can be provided by request, contact our `sales <https://geoalert.io/#contacts>`_.


Projects and processings
--------------------------

**What is a “project”? Do I have to create every new processing in a new project?**

    **Project** allows you to collect all logically related processing for a more efficient and faster search for the one you need. It's like a folder on your computer. One project can have many jobs.

**Immediately after registration, I got a project called “Demo processings”. What is it and why?**

    This project allows you to get acquainted with the capabilities of Mapflow without spending Credits. In the History of processings, you can view and check the results. It is also possible to view the selected processing parameters, to do this, click **source details**.

**Are there any restrictions on the processing area?**

    The processing area may be smaller but the price is rounded up to 1 sq. km. There is the default limit of no more than 50 sq. km (free account). If you need to process a large area, you can divide the area to be treated into several smaller areas, one per processing. Alternatively you can consider switching to a paid plan.

User data
-------------------

**What is an imagery mosaic?**

    *Mosaic* - a set of images covering a specific area. Using My Imagery you collect separate aerial images in a single mosaic to analyse with the Mapflow models.

**What are the limots for my data?**

    Your input data must meet the :ref:`Mapflow models requirements <Model requirements>` and the :ref:`files upload requirements <Upload requirements>`. 

**How to delete my account?**

    Currently you cannot delete your account right in the Mapflow web app. Please request us to delete your account by sending an email to help@geoalert.io or by prompting the Mapflow chatbot, and all your personal data will be completely removed.


Support and other questions
----------------------------

**Do you have an API?**

    :doc:`Yes, we do <api/mapflow_api>`.

**Do you have GIS integration?**

    Yes, we do. You can use our open source plugin  :doc:`plugin Mapflow <api/qgis_mapflow>` for the GIS `QGIS <https://qgis.org/ru/site/forusers/download.html>`_.

**What is API token and why do I need it?**

     The API token is used as password in external applications that use the resources of the Mapflow platform. It is passed as the Basic Auth authorization parameter. You can `obtain an API token in your personal Mapflow profile <https://app.mapflow.ai/account/api>`_. 
    
**I have another question, where can I ask it?**

    You can ask your question on the Mapflow website in the online chat, where we will try to answer your questions in real time. Also, you are welcome to write to us at `help@geoalert.io <mailto:help@geoalert.io>`_.
