Buildings (Aerial imagery)
--------------------------

This model is specifically designed to make use of very high resolution aerial imagery (10 cm per pixel) for extraction of small buildings and structures. It is best suited for rural and suburban residential areas.

We do not recommend using this model in areas with high urban residential or commercial buildings. Use :doc:`Buildings <buildings_model>` model instead, even for aerial imagery.

**Processing results samples**

    .. figure:: ../_static/processing_result/aerial_model_1.png
        :alt: Processing result of Buildings (Aerial) model
        :align: center
        :width: 18cm
    
        Processing example rural residential area with a Building model (Aerial photo)

    .. figure:: ../_static/processing_result/aerial_model_2.png
        :alt: Processing result of Buildings (Aerial) model
        :align: center
        :width: 18cm

        Standard model for buildings segmentation, with polygon simplification

    .. figure:: ../_static/processing_result/aerial_model_3.png
        :alt: Processing result of Buildings (Aerial) model
        :align: center
        :width: 18cm
        
        Objects that have been detected in an aerial image by the Building (Aerial imagery) model as opposed to the standard model Buildings.