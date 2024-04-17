### Description ###
A popular way to get a quick overview over a set of variables of an experiment and find possible correlations between them is by plotting them in several scatter plots.
These scatter plots are often arranged in a matrix where each row and column is dedicated to a single experiment variable.
Each cell of the matrix then contains the scatter plot that compares the variable of the column with the variable of the row.
Since this matrix is symmetric, the upper or lower half of the matrix is often removed, similar to the diagonal which would only contain scatter plots comparing a variable to itself.

This example demonstrates the visualization of several variables using scatter plots based on a dataset describing the material flow in the earth's mantel.
This material flow is caused by the convection process in the earth's mantel which forces hot material at the center of the earth to travel to the cooler outer shells.
At the same time cool material flows back to the hotter center of the earth.
The velocity field of the simulated flow of material is stored in the dataset provided along with this example.
For the visualization, the example takes only a slice of the three-dimensional scalar fields that cuts right through the earth.
The sample point of the dataset that lie in the slice are then plotted in several scatter plots that juxtapose the variables `spin transition-induced density anomaly`, `temperature`, `temperature anomaly`, `thermal conductivity` and `thermal expansivity`.
In addition to that, the example also shows the variables in isolation using several heatmaps placed left to the grid of scatter plots.

### Instructions ###
The file archive that comes with this example contains the script file `scatterplots_script.sh` that when executed creates a matrix of scatter plots for the provided dataset.
The script can be started using the following terminal command
```bash
./scatterplots_script.sh
```
In some cases, the script file `scatterplots_script.sh` is not detected by the operating system as an executable file.
If this happens, the following command can be used to mark the script file as executable
```bash
chmod +x scatterplots_script.sh
```
After a successful execution of the script, the image `scatterplots.png` containing the final visualization of the provided dataset is placed in the folder `output`.

Using this example with your own data can be complicated as the example not only creates scatter plots but also generates heatmaps for all variables to be visualized.
Both visualizations need to be adjusted such that they use the correct variables of the provided datasets.
The variables that are taken into account when creating the scatter plot matrix are controlled by the following line of the `scatterplots_trace.py` file.
```python
scatterPlot1Display.SeriesVisibility = ['spin transition-induced density anomaly', 
                                        'temperature', 
                                        'temperature anomaly', 
                                        'thermal conductivity', 
                                        'thermal expansivity']
```
In this line there is a list that contains the names of the variables that are shown in the scatter plot matrix.
For more information on how to change the additional heatmaps, see the <a href="/visualization?name=Parallel Coordinates">Parallel Coordinates</a> example.

The slice that the example derives from the input dataset is controlled by the following line of the `scatterplots_trace.py` file.
```python
extractSubset1.VOI = [0, 360, 0, 201, 90, 90]
```
The first three values of the list in this line define the minimal `x`, `y` and `z` extend of the slice while the last three values define the maximal extend.

Finally, the example also assumes that input dataset stores its fields in a spherical coordinate system with the axes `latitude (lat)`, `longitude (lon)` and `radius (r)`.
The order in which these axes are read from the dataset can be controlled using the following line of the `scatterplots_trace.py` script
```python
reader.Dimensions = '(lat, r, lon)'
```

### Limitations ###
Currently the `scatterplots_trace.py` only supports datasets that are stored in the NetCDF (Network Common Data Form) format.
Datasets that are stored in this particular format can be identified by the file extension `.nc`.
Other file formats are theoretically possible but would require extensive changes to the `scatterplots_trace.py` file as the reader used by the script would need to be replaced.

### References ###
1. [<span id="reference_dataset">2021, "SciVis Contest 2021: Earth's Mantle Convection", https://scivis2021.netlify.app/data/</span>](https://scivis2021.netlify.app/data/)