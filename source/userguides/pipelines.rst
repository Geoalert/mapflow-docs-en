.. meta::
   :description: Mapflow AI-mapping models for buildings, forest, roads and more: what each model returns, the imagery it needs and what it costs.

.. _Models:

.. rst-class:: mf-page mf-index

AI-Mapping Models
*****************

.. rst-class:: mf-lede

Mapflow models find buildings, trees, roads and other objects in satellite, aerial and drone imagery,
and return them as editable vector layers. Open a model to see what it returns,
the imagery it needs and what it costs.

.. rst-class:: mf-quicklinks

* :ref:`Data requirements <Model_requirements>`
* :doc:`Pricing <prices>`
* `Request a custom model <https://mapflow.ai/custom-models>`__

.. mf-heading:: Popular tasks

.. mf-task-links::

.. mf-heading:: Default models

Available to every account in Mapflow Web, the QGIS plugin and the API.

.. mf-model-gallery::
   :availability: default, no-ai

.. mf-heading:: Bring your own imagery

Every model runs on imagery you upload, a raster already in your QGIS project,
or a fresh image from the satellite catalog.

.. mf-workflow-gallery::

.. mf-heading:: Custom models

Trained for specific use cases. We connect them to your account on request.
See :doc:`how custom models work <custom_pipelines>`.

.. mf-model-gallery::
   :availability: custom

.. mf-cta::

.. toctree::
   :hidden:
   :maxdepth: 1

   buildings_model
   forest_model
   roads_model
   combo_model
   open-data
   custom_pipelines
