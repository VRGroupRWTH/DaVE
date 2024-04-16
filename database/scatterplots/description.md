<div id="description" outline_label="Description" outline_indent="0" markdown="1">
### Description ###
A popular way to get a quick overview over a set of vairables of an experiment and find possible correlection between them is by plotting them in several scatter plots.
These scatter plots are often arranged in a matrix where by each row and column is dedicated to a single experiment variable.
Each cell of the matrix then contains the scatter plot that raltes the variable of the column with the variable of the row.
Since this matrix is symmetric, the upper or lower half of the matrix is often removed, similar to the diagonal which would only contain scatter plots relating the same variable to itself.

This exaple demonstrates the visualization of several variables using scatter plots based on an dataset describing the material flow in the earth's mantel.
This material flow is caused by the convection process in the earth's mantel which forces hot material at the center of the earth to travel to the more cooler outer shells.
At the same time cool material flows back to the hotter center of the earth.
The velocity field of the simulated flow of material is stored in the dataset provided along with this example.
For the visulization, the example takes only a slice of the three-dimensional scalar fields that cuts right through the earth.





Subset of the mantle data set from SciVis contest with four heatmaps for four different fields. Additionally scatterplots are provided.

</div>
<div id="instructions" outline_label="Instructions" outline_indent="0" markdown="1">
### Instructions ###
The file archive that comes with this example contains the script file `scatterplots_script.sh` that when executed visualizes the provided vector field using stream lines.
The script can be started using the following terminal command
```
./scatterplots_script.sh
```
In some cases, the script file `streamline_script.sh` is not detected by the operating system as an executible file.
If this happens, the following command can be used to mark the script file as executable
```
chmod +x scatterplots_script.sh
```
After a successful execution of the script, the image `scatterplots.png` containing the final visualization of the provided dataset is placed in the folder `output`. 



```
reader.Dimensions = '(lat, r, lon)'
```



```
extractSubset1.VOI = [0, 360, 0, 201, 90, 90]
```

```
scatterPlot1Display.SeriesVisibility = ['spin transition-induced density anomaly', 
                                        'temperature', 
                                        'temperature anomaly', 
                                        'thermal conductivity', 
                                        'thermal expansivity']
```

More information on how to remove or change heatmaps in an grid layout, see the <a href="/visualization?name=Parallel Coordinates">Paralel Coordinates</a> example

</div>
<div id="limitations" outline_label="Limitations" outline_indent="0" markdown="1">
### Limitations ###
Currently the `scatterplots_trace.py` only supports datasets that are stored in the NetCDF (Network Common Data Form) format.
Datasets that are stored in this particular format can be identified by the file extension `.nc`.
Other file formats are theoretically possible but would require extensive changes to the `scatterplots_trace.py` file as the reader used by the script would need to be replaced.
</div>
<div id="references" outline_label="References" outline_indent="0" markdown="1">
### References ###
1. [<span id="reference_dataset">2021, "SciVis Contest 2021: Earth's Mantle Convection", https://scivis2021.netlify.app/data/</span>](https://scivis2021.netlify.app/data/)
</div>