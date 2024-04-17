### Description ###
Pathlines are frequently used in fluid dynamics for the visualization of unsteady flows, such as the flow of gases in a running combustion engine.
Unsteady flow, also known as transient flow, is characterized by the fact that certain properties affecting the flow are time-dependent.
For instance, if the velocity field of the flow changes over time, the flow is considered unsteady.
As the name already suggests, the visualization of a two or three-dimensional vector field using path lines consists of a finite number set of lines.
Each line shows the path of a hypothetical particle whose movement is determined by the given vector field.
The position of such a particle over time is calculated using numerical integration methods such as the Euler method.
On the other hand, the staring points of the lines are often chosen randomly where the user only controls the number of the seed points and the area in which they should be spawned.

<!--In comparison to stream lines which also visualize a dataset using lines, 
The computation of pathlines makes only sense if the given dataset is time-depenedent.
Otherwise they are identical to steamlines.-->

In this example, path lines are demonstrated using a time dependent two-dimensional dataset that models a changing vector field [1](#reference_dataset).
For the visualization, some seed points are placed on the left side of the dataset which define the starting points of the path.
Over time, the path mostly grow to the right as the general direction within the dataset points to the right.
In case the hypothetical particle runs into the more turbulent areas at the edge pf the vector field, the path will also from loops.
To make the different paths more distinguishable, each is colored using a different color.
This also highlights a potential disadvantage of this visualization approach, as with increasing number of paths, the resulting image becomes more visually cluttered.
As a result, it is sometimes difficult to make out the path that a particular particle has taken.

### Instructions ###
The file archive that comes with this example contains the script file `pathline_script.sh` that when executed creates pathlines for the provided dataset.
The script can be started using the following terminal command
```bash
./pathline_script.sh
```
In some cases, the script file `volume_statistics_script.sh` is not detected by the operating system as an executable file.
If this happens, the following command can be used to mark the script file as executable
```bash
chmod +x pathline_script.sh
```
After a successful execution of the script, the image `pathline_script.png` containing the final visualization of the provided dataset is placed in the folder `output`. 

When entering your own data, it is likely that the example and some of its scripts need to be adapted.
For example, the example assumes that your dataset contains a scalar filed with the name `ImageFile`.
If such a field does not exist, the example will not know what to visualize and may return with an error.
To change the name of the field, the lines of the script filed `volume_statistics_trace.py` marked with the keyword `OWN_DATA` need to be modified so that they contain the name of the desired field.
On of these lines is shown below
```python
reader.PointArrayStatus = ['ImageFile']
```
Another important parameter of this example, that may need to be adjusted when using custom data, is the number of pathlines.
This parameter is controlled by the following line of the `volume_statistics_trace.py` file
```python
maskPoints1.MaximumNumberofPoints = 99
```

### Limitations ###
Currently this example only accepts datasets in the `.vti` file format as other formats would require major changes to the loading process.
Also, the example has only been tested with apptainer version `1.2.5-1.el8` and Docker version `24.0.5, build 24.0.5-0ubuntu1~22.04.1`.

Besides that, there are additionally the following limitations:
- Pathlines using multiple MPI ranks are currently not always correctly connected in ParaView.