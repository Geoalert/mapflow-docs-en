Mapflow pricing
===============

How to top up your balance
--------------------------

.. note::
   Each user gets the free balance of **250** credits to get started with Mapflow AI.
   You can always buy more credits in your `account profile <https://app.mapflow.ai/account/balance>`_.

In order to top up you balance go to `your Mapflow profile <https://app.mapflow.ai/account/balance>`_ and choose one of the options.
You will be asked to pay online.

.. image:: _static/topup.png
   :alt: Top up you balance
   :align: center
   :width: 15cm
   :class: with-border no-scaled-link

|

.. important::
   If you want to buy a custom number of credits, use another payment method, or consider using Mapflow on a large scale, check `Mapflow commercial plans <https://mapflow.ai/pricing>`_.

.. _credits:

Mapflow credits
---------------

Cost of processing makes the sum of **data cost** and **processing cost** given the requested area:

``Cost = Area * (Processing Price + Data Price)``

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

All prices below are given in Mapflow credits. Mapflow Web also provides a transparent price breakdown in the processing pipeline.

.. note::
   * All the processings having an area less than 1 sq.km are rounded up to 1 sq.km before price calculation!
   * Total processing cost is rounded up to the nearest integer number of credits

.. note::
   Most default models work at 18 zoom. The exceptions are Fields high-res model (17 zoom) and Segment-anything that has an optional zoom. `What is zoom? <https://wiki.openstreetmap.org/wiki/Zoom_levels>`_

Maflow pricing
-------------------------

Default Mapflow models
~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
  :file: _static/csv/web_processing_prices.csv
  :header-rows: 1
  :class: longtable
  :widths: 1 1 1

.. note::
   If you want to have a custom model with another set of options, consider
   applying for `Mapflow Premium plan <https://mapflow.ai/pricing>`_.


.. note::

   Custom model pricing depends on the complexity of the task and the total project size. To get the quotation and apply the discount, please contact us to share your project requirements.  


Data price
~~~~~~~~~~~~~~
When using default data providers (Mapbox, Arcgis WorldView Imagery), your own TMS, or your uploaded imagery the price is zero.
If you are using connected commercial providers ("Global mosaic" and others that might be available), the cost of the data depends on the zoom level. We partner with streaming data providers, which means that the cost of the service depends on the paid traffic – therefore we quote the prices depending on the imagery resolution for a more accurate and flexible pricing model.

.. csv-table::
  :file: _static/csv/data_prices.csv
  :header-rows: 1
  :class: longtable
  :widths: 20 10 10



Examples of quotations
~~~~~~~~~~~~~~~~~~~~~~~

.. epigraph::
    *I want to process 3.3 sq.km of Global Mosaic data at 18 zoom using the Buildings model*

    ``Cost = 3.3 * (10+5) = 50 credits``

.. epigraph::
    *I want to process 0.01 sq.km of my own imagery using the Buildings Aerial model and applying the simplification option.*
    
    Area is rounded up to 1 sq.km, so the cost will be: 
    ``Cost = 1 * (25+3) = 28 credits``