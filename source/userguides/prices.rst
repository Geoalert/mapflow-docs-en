Mapflow pricing
===============

How to top up your balance
--------------------------

.. note::
   Each user gets the free balance of **250** credits to get started with Mapflow AI.
   You can always buy more in your `account profile <https://app.mapflow.ai/account/balance>`_.

In order to top up you balance with more credits go to `your Mapflow profile <https://app.mapflow.ai/account/balance>`_ and choose one of the options.
You will be asked to pay online.

.. image:: _static/topup.png
   :alt: Top up you balance
   :align: center
   :width: 15cm
   :class: with-border no-scaled-link

|

.. important::
   If you want to buy a custom number of credits, use another payment method or consider using Mapflow on a large scale, check `Mapflow commercial plans <https://mapflow.ai/pricing>`_.


Mapflow credits
---------------

The price in credits is counted as:
1 Credit = 0.1$ with the progressive discount depending on the number of credits you buy:

.. list-table::
   :widths: 30 15 15 15
   :header-rows: 1

   * - Mapflow Credits
     - 500
     - 1000
     - 10000
   * - You pay
     - $50
     - | :del:`$100`
       | $90
     - | :del:`$1000`
       | $800

All prices below are given in Mapflow credits

Maflow Web models pricing
-------------------------

.. csv-table::
  :file: _static/csv/web_processing_prices.csv
  :header-rows: 1
  :class: longtable
  :widths: 1 1 1

Mapflow Web also provides a transparent price breakdown in the processing pipeline.

Mapflow-QGIS / API models pricing
----------------------------------

.. warning::
   Mapflow-QGIS plugin has a slightly different set of models, and you cannot choose the model options.
   All models are launched with postprocessing options **turned ON**.
   If you want to customize your workflow, for example to have a basic model with another set of options, consider
   applying for `Mapflow Premium plan <https://mapflow.ai/pricing>`_.
   Also, Mapflow QGIS provides access to paid imagery services, so the cost calculation is a bit more complex.

Cost of processing consists of **data cost** and **processing cost**

``Cost = Area * (Processing Price + Data Price)``

.. note::
   * All the processings having an area less than 1 sq.km are rounded up to 1 sq.km before price calculation!
   * Total processing cost is rounded up to the nearest integer number of credits

Processing price
~~~~~~~~~~~~~~~~

As all the model options are turned on for Mapflow QGIS,
processing cost is the same as in Mapflow Web with the options, where it's applicable:

.. csv-table::
  :file: _static/csv/api_processing_prices.csv
  :header-rows: 1
  :class: longtable
  :widths: 1 1 1

Data price
~~~~~~~~~~
When using default data providers (Mapbox, Arcgis Satellite), your own TMS, or your uploaded imagery the price is zero.
If you are using commercial providers (Maxar SecureWatch, and others that might be available), the cost of the data depends on the zoom level. We partner with streaming data providers, which means that the cost of the service depends on the paid traffic therefore we scale prices depending on the imagery resolution for a more accurate pricing model.

.. csv-table::
  :file: _static/csv/data_prices.csv
  :header-rows: 1
  :class: longtable
  :widths: 20 10 10 10

.. note::
   Most default models work at 18 zoom. The exceptions are Fields high-res model (17 zoom) and Segment-anything that has an optional zoom. `What is zoom? <https://wiki.openstreetmap.org/wiki/Zoom_levels>`_

.. epigraph::
    *I want to process 3.4 sq.km of Maxar SecureWatch data at 18 zoom
    (35 credits per sq.km) with Buildings model
    (13 credits per sq.km).*
    ``Cost = 3.4*(13+35) = 163.2 => 164 credits``

.. epigraph::
    *I want to process 0.01 sq.km of my own imagery
    with the Forest model.
    Area is rounded up to 1 sq.km, so the cost will be:* 
    ``Cost = 1*8 = 8 credits``