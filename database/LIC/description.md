<div id="description" outline_label="Description" outline_indent="0" markdown="1">
### Description ###
Line-Integral Convolution is a visualization techniques that can be used to highlight the field lines of two-dimensional or three-dimensional vector fields.
Starting from an arbitarty point within the domain of the given dataset, the method traces a path that follows the vector field.
During the tracing of the path, a noise image 


used for two-dimensional or slices of three-dimensional vector fields.
Based on the vector field and an addtional noise filed, Line-Integral Convolution creates a scalar field that highlights the field lines of the vector field.





Unlike other visualization technique for vector field, 

Unlike other commonly used methods for the visualization of vector fields, such as streamlines or pathlines, line-lntegral convolution does not illustrate the vector field using tubes or lines.
Instead, it creates a scalar field using the vector field and an additional noise field, which in the end is visualized similar as a heatmap.
Starting from a point within the domain of the scalar field, the method traces a path that follows the vector field and integrates the values of the noise field along the way.
The contribution of the noise field to the integration is often modulated by a user defined convolution kernel, which in its simplest from weights the values of the noise field equaliy.
When the path reaches a user defined length, the integration porcess is stopped and the result of the integral is used to define the value of the scalar field at the starting point.

In this example, line integral convolution is demonstrated by visualizing a simulation of the convection process that takes place in the earth's mantel.
Even though the dataset that is used in this example is a three-dimensional vector field, line integral convolution can be still applied in this case as several clipping planes are used [1](#reference_dataset).

Benefits no intersection of lines or tubes, less visual luttering less occlusion problem. 
Placement of the seed points less problematic. More generak overview over the vector field.
</div>
<div id="instructons" outline_label="Instructions" outline_indent="0" markdown="1">
### Instructions ###
The file archive that is provided for this example contains the script file `lic_script.sh` that when executed visalized a dataset using line-integral convolution.
The script can be started using the following terminal command
```
./lic_script.sh
```
In some cases it is neccessary to first mark the script as executible which can be done by running the following line in the terminal
```
chmod +x lic_script.sh
```
After a successful execution of the script, the image `lic.png` containing the final visualization of the provided dataset is placed in the folder `output`. 


```
reader.Dimensions = '(lat, r, lon)'
```

```
calculator1.Function = '(iHat*vx + jHat*vy + kHat*vz) * 1e9'
```


When using a dataset other than the default dataset shipped together with the example, some modification need to be done in the file `lic_trace.py` to make sure that the correct vector field is used for the visualization.

</div>
<div id="limitations" outline_label="Limitations" outline_indent="0" markdown="1">
### Limitations ###
Currently the `lic_trace.py` only supports datasets that are stored in the NetCDF (Network Common Data Form) format.
Datasets that are stored in this particular format can be identified by the file extension `.nc`.
Other file formats are theoretically possible but would require extensive changes to the `lic_trace.py` file as the reader used by the script would need to be replaced.

Besides that there are additional limitations:
- Artifacts in distributed execution
</div>
<div id="references" outline_label="References" outline_indent="0" markdown="1">
### References ###
1. [<span id="reference_dataset">2021, "SciVis Contest 2021: Earth's Mantle Convection", https://scivis2021.netlify.app/data/</span>](https://scivis2021.netlify.app/data/)
</div>