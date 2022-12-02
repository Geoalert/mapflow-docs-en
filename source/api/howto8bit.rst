How to change the data type of your image to Uint8 bit in QGIS
==============================================================



1. Check the data type of your image. 
Right-click on the imagery layer - i - Information from provider. The Data type must be Byte. Follow the next steps if the Data type is Int16, Float 32 etc.

    
    .. figure:: _static/qgis/information.png


  

2. Right click on your image Layer Properties -  Symbology tab, then customize the display of your image. Select desired channels for Band rendering, adjust brightness and contrast. 
      
    
    .. figure:: _static/qgis/symbology.png



3. Right-click on the layer’s name, go to the  Export in the context menu, Save as…

 
    .. figure:: _static/qgis/export.png
    


4. Check Output mode as Rendered Image


    .. figure:: _static/qgis/save_raster.png
    


5. Save your image  - navigate to the desired folder, input the file name then click OK



6. Use the new image layer as Imagery source when using the Mapflow plugin for QGIS


