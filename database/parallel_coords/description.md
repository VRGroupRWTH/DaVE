<div id="description" outline_label="Description" outline_indent="0" markdown="1">
### Description ###
Parallel Coordinates is a visualization technique with which several scalar properties over the same spatial domain can be visualized and set in relation.
The coordinate system that is used in this visualization consists of multiple axes, one for each property being visualized.
These axes are often placed vertically side by side, hence the name parallel coordinates.
Besides mapping the values of the different properties to the corresponding axes, the method also connects values that spatially belong to the same location with a line.
This makes it easier to detect relationships between the different properties.

Based on a geological use case, this example demonstrates the use of parallel coordinates by mapping different geological properties of the earth's mantle to coordinates.
The dataset that was taken for this example was created by simulating the convection process that takes place in the earth's mantle [1](#reference_dataset).
Besides the temperature, the dataset also captures the properties `temperature anomality`, `thermal conductivity` and `thermal expansivity`, which are visualized using a parallel coordinate plot.
Additionally, the example also shows these attributes in isolation using multiple heatmaps.
</div>
<div id="instructions" outline_label="Instructions" outline_indent="0" markdown="1">
### Instructions ###
To execute the example just run

```
./parallel_coordinates_script.sh
```

If the script is not executible run the following command

```
chmod +x parallel_coordinates_script.sh
```
</div>
<div id="limitations" outline_label="Limitations" outline_indent="0" markdown="1">
### Limitations ###
Currently the `parallel_coordinates_trace.py` only supports datasets that are stored in the NetCDF (Network Common Data Form) format.
Datasets that are stored in this particular format can be identified by the file extension `.nc`.
Other file formats are theoretically possible but would require extensive changes to the `parallel_coordinates_trace.py` file as the reader used by the script would need to be replaced.
</div>
<div id="references" outline_label="References" outline_indent="0" markdown="1">
### References ###
1. [<span id="reference_dataset">2021, "SciVis Contest 2021: Earth's Mantle Convection", https://scivis2021.netlify.app/data/</span>](https://scivis2021.netlify.app/data/)
</div>