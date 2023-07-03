🏠 Buildings (Aerial imagery)
-----------------------------

This model is specifically designed to make use of very high resolution aerial imagery (10 cm per pixel) for extraction of small buildings and structures. It is best suited for rural and suburban residential areas.

We do not recommend using this model in areas with high-dense urban buildings. Use :doc:`Buildings model <buildings_model>` instead, even for aerial imagery.

**Processing results samples**

    .. figure:: _static/processing_result/aerial_model_1.jpg
        :alt: Processing result of Buildings (Aerial) model
        :align: center
        :width: 15cm
        :class: with-border no-scaled-link
    
        Processing example rural residential area with a Building model (Aerial photo)

    .. figure:: _static/processing_result/aerial_model_2.jpg
        :alt: Processing result of Buildings (Aerial) model
        :align: center
        :width: 15cm
        :class: with-border no-scaled-link

        Standard model for buildings segmentation, with polygon simplification

    .. figure:: _static/processing_result/aerial_model_3.jpg
        :alt: Processing result of Buildings (Aerial) model
        :align: center
        :width: 15cm
        :class: with-border no-scaled-link
        
        Objects that have been detected in an aerial image by the Building (Aerial imagery) model as opposed to the standard model Buildings.