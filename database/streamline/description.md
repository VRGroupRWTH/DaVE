### Description ###
Streamlines are commonly used for the visualization of steady flows or the visualization of flow states at specific points in time.
They are quite similar to pathlines in that they also use lines to visualize a vector field, but there is a distinct difference between those techniques.
In comparison to path lines, streamlines visualize a vector field for an isolated point in time and therefore allow for a more direct insight into how the vector field changes over time.
From a technical point of view, streamlines are computed similarly to pathlines only that they use the same vector field for each time step of the integration process with which the paths of the hypothetical points are calculated.
More information on the definition of the lines and pathlines in general can be found in the <a href="/visualization?name=Pathlines of Fluid Flow">Pathline</a> example.

In this example a mechanical simulation of a jet engine's exhaust flow is illustrated using streamlines.
The dataset created by the simulation contains the velocity for an isolated point in time [1](#reference_dataset).
The example not only shows the lines but also colors them based on the magnitude of the velocity.
Line segments that pass through an area of high velocity are colored red and blue if they pass though low velocity areas.
As it can be clearly seen, the exhaust stream of the jet engine is quite concentrated and therefore a lot of lines passing from left to right stay in the middle of the simulation domain.
Only a few lines diverge from the cluster in the middle and from loops in the more turbulent outer parts of the exhaust stream.

### Instructions ###
The file archive that comes with this example contains the script file `streamline_script.sh` that when executed visualizes the provided vector field using streamlines.
The script can be started using the following terminal command
```bash
./streamline_script.sh
```
In some cases, the script file `streamline_script.sh` is not detected by the operating system as an executable file.
If this happens, the following command can be used to mark the script file as executable
```bash
chmod +x streamline_script.sh
```
After a successful execution of the script, the image `streamline.png` containing the final visualization of the provided dataset is placed in the folder `output`. 

The vector field that the example uses for the visualization is determined by the lines of the `streamline_trace.py` script that are marked with the keyword `OWN_DATA`.
By default, the example used the field with the name `ImageFile`, but when using a custom dataset it might be necessary to select field with a different name.
One of the lines need to be modified when changing the name of the field is shown in the following
```python
reader.PointArrayStatus = ['ImageFile']
```
The number of lines that are spawned can be controlled using the following line of the `streamline_trace.py` script
```python
maskPoints1.MaximumNumberofPoints = 100
```

### Limitations ###
Currently this example only supports dataset that are stored in the `.vti` file format.
Other file formats are theoretically possible but would require wider changes to the script `streamline_trace.py` as a different file reader would be required.

### References ###
1. [<span id="reference_dataset">Christoph Garth, March 9, 2020, "Simulation of a jet flow", IEEE Dataport, doi: https://dx.doi.org/10.21227/qjxp-kc31.</span>](https://dx.doi.org/10.21227/qjxp-kc31)