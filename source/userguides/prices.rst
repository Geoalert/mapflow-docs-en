Mapflow pricing
===============


How to top up your balance
--------------------------

.. note::
   Each user gets free balance of credis to get started with functionality and features of Mapflow

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

.. note::
   Each user gets free balance of **250** credits to get started with functionality and features of Mapflow
   You can always buy more in your `account <https://app.mapflow.ai/account/balance>`_ section.

The price in credits is counted as:
1 Credit = 0.1$ with the progressive discount depending on the amount of credits you buy:

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

Maflow Web models pricing
-------------------------

.. csv-table::
  :file: _static/csv/web_processing_prices.csv
  :header-rows: 1
  :class: longtable
  :widths: 1 1 1

Mapflow Web also shows transparent price breakdown during processing creation.

Mapflow-QGIS models pricing
---------------------------

.. warning::
   Mapflow-QGIS has slightly different set of models, and you cannot choose the model options.
   All models are launched with postprocessing options turned ON.
   If you want to customize your experience, for example to have a basic model with lower price,
   apply for `Mapflow Premium <https://mapflow.ai/pricing>`_.
   Also, Mapflow QGIS provides access to paid imagery services, so the cost calculation is a bit more complex.

Cost of processing consists of **data cost** and **processing cost**

``Cost = Area * (Processing Price + Data Price)``

.. note::
    all the processings having area less than 1 sq.km are rounded up to 1 sq.km before price calculation!

.. note::
    total processing cost is rounded up to the nearest integer number of credits

Processing price
~~~~~~~~~~~~~~~~

As all the model options are turned on for Mapflow QGIS,
processing cost is the same as in Mapflow Web with the options, where applicable:

.. csv-table::
  :file: _static/csv/api_processing_prices.csv
  :header-rows: 1
  :class: longtable
  :widths: 1 1 1

Data price
~~~~~~~~~~
Data price when using data providers (Mapbox, Arcgis Satellite), your basemap links, and your uploaded imagery is zero.

If you are using paid providers (Maxar SecureWatch, and others that might be available),
the cost of the data depends on the zoom level, changing 4-fold with each zoom level. We partner with streaming data providers,
which means that the cost of the service depends on the traffic,
therefore we scale prices depending on the imagery resolution for a more accurate pricing model.

.. csv-table::
  :file: _static/csv/data_prices.csv
  :header-rows: 1
  :class: longtable
  :widths: 20 10 10 10

.. note:: Most default models work at 18 zoom. Exception is Fields high-res model (17 zoom).
          `What is zoom? <https://wiki.openstreetmap.org/wiki/Zoom_levels>`_

Example
-------

I want to process 3.3 sq.km of Maxar SecureWatch data at 18 zoom
(72 credits for per sq.km) with Buildings model
(13 credit per sq.km).
Cost = 3.3*(13+72) = 280.5, rounded up to **281 credits**.

I want to process 0.01 sq.km of my own imagery
with the Forest model.
Area is rounded up to 1 sq.km, so the cost will be 1*(8+0) = **8 credits**
