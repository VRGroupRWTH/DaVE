### Description ###
Parallel Coordinates is a visualization technique with which several scalar properties over the same spatial domain can be visualized and set in relation.
The coordinate system that is used in this visualization consists of multiple axes, one for each property being visualized.
These axes are often placed vertically side by side, hence the name parallel coordinates.
Besides mapping the values of the different properties to the corresponding axes, the method also connects values that spatially belong to the same location with a line.
This makes it easier to detect relationships between the different properties.

Based on a geological use case, this example demonstrates the use of parallel coordinates by mapping different geological properties of the earth's mantle to coordinates.
The dataset that was taken for this example was created by simulating the convection process that takes place in the earth's mantle [1](#reference_dataset).
Besides the `temperature`, the dataset also captures the properties `temperature anomality`, `thermal conductivity` and `thermal expansivity`, which are visualized using a parallel coordinate plot.
Additionally, the example also shows these attributes in isolation using multiple heatmaps.

### Instructions ###
The file archive that comes with this example contains the script file `volumerender_script` that when executed creates a parallel coordinate plot for the provided dataset.
The script can be started using the following terminal command
```bash
./parallel_coordinates_script.sh
```
In some cases it is neccessary to first mark the script as executible which can be done by running the following line in the terminal
```bash
chmod +x parallel_coordinates_script.sh
```
After a successful execution of the script, the image `parallel_coordinates.png` containing the final visualization of the provided dataset is placed in the folder `output`. 

What makes the example difficult to apply on custome dataset is the fact that changing the number of sclar field requires wider changes to the example.
This is due to the fact that the example not only creates a parallel coordinate plot but also provides a heatmap for each scalar field.
Changing the number of scalar fields therefore means that either heatmaps have to be removed or added.
When using the example on a custome dataset, all scalar fields that should be included in the parallel coordinate plot need to be listed with thier name in the following array of the `parallel_coordinates_trace.py` script
```python
extractSubset1Display.SeriesVisibility = ['temperature', 
                                          'temperature anomaly', 
                                          'thermal conductivity', 
                                          'thermal expansivity']
```
Besides that, it might be also neccessary to change the already existing four heatmaps so that they used the correct fields as well.
The lines of the `parallel_coordinates_trace.py` that describe a heatmap are always arranged in a block as shown in the following
```python
# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# get 2D transfer function for 'thermalexpansivity'
thermalexpansivityTF2D = pvs.GetTransferFunction2D('thermalexpansivity')

...

thermalexpansivityLUTColorBar.ScalarBarLength = 0.8530125523012553
thermalexpansivityLUTColorBar.Visibility = 1
```
In order to change the field that is used by a heatmap, it is neccessay to modify the lines of a block that are marked with the comment `OWN_DATA: change field name` such that they contain the name of the desired filed.
However, if fewer or even no heatmaps are needed, they can be easily removed by cutting out their blocks from the `parallel_coordinates_trace.py` script.
Adding more heatmaps on the other hand if even more complicated as they need to be integrate into the layout of the final image.
For more information on that, see the documentation of the ParaView Python API [2](#reference_python_api).

Finally, the example also assumes that input dataset stores its fields in a spherical coordinate system with the axes `latitude (lat)`, `longitude (lon)` and `radius (r)`.
The order in which these axes are read from the dataset can be controlled using the following line of the `parallel_coordinates_trace.py` script
```python
reader.Dimensions = '(lat, r, lon)'
```

### Limitations ###
Currently the `parallel_coordinates_trace.py` only supports datasets that are stored in the NetCDF (Network Common Data Form) format.
Datasets that are stored in this particular format can be identified by the file extension `.nc`.
Other file formats are theoretically possible but would require extensive changes to the `parallel_coordinates_trace.py` file as the reader used by the script would need to be replaced.

### References ###
1. [<span id="reference_dataset">2021, "SciVis Contest 2021: Earth's Mantle Convection", https://scivis2021.netlify.app/data/</span>](https://scivis2021.netlify.app/data/)
2. [<span id="reference_python_api">Kitware, Inc. , March 26, 2024, "ParaView’s Python documentation!", https://kitware.github.io/paraview-docs/v5.10.1/python/index.html.</span>](https://kitware.github.io/paraview-docs/v5.10.1/python/index.html)