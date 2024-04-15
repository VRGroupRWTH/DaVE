<div id="description" outline_label="Description" outline_indent="0" markdown="1">
### Description ###
Pathlines are frequently used in fluid dynamics for the visualization of unsteady flows, such as the flow of gases in a running combustion engine.
Unsteady flow, also known as transient flow, is characterized by the fact that certain properties affecting the flow are time-dependent.
For instance, if the velocity field of the flow changes over time, the flow is considered unsteady.
As the name already suggests, the visualization of a two or three-dimensional vector field using path lines consists of a finite number set of lines.
Each line shows the path of a hypotetical particle whose movement is determined by the given vector field.
The position of such a particle over time is calculated using numerical integration methods such as the euler method.
On the other hand, the staring points of the lines are often chosen randomly where by the user only controlls the number of the seed points and the area in which they should be spawned.

<!--In comparison to stream lines which also visualize a dataset using lines, 
The computation of pathlines makes only sense if the given dataset is time-depenedent.
Otherwise they are identical to steamlines.-->

In this example, path lines are demonstratted using a time dependent two dimensional dataset that models a changing vector field [1](#reference_dataset).
For the visualization, a small number of seed points are placed on the left side of the dataset which define the starting points of the path.
Over time, the path mostly grow to the right as the general direction within the dataset points to the right.
In case the hypotetical particel runs into the more turbulent areas at the edge pf the vector field, the path will also from loops.
To make the different paths more distibgushable, each is colored using a different color.
This also highlights a potential diosadvantage othis veisalization approach, as with increasing number of paths, the resuling image beomes more visually cluttered.
As a result, it is sometimes difficult to make out the path that a particular particle has taken.
</div>
<div id="instructions" outline_label="Instructions" outline_indent="0" markdown="1">
### Instructions ###
To execute the example just run

```
./pathline_script.sh
```

If the script is not executible run the following command

```
chmod +x pathline_script.sh
```

The example exports the animation as a series of images

For entering your own data, search for "OWN_DATA" comments in the volumerender_trace.py file and change the file according to the instructions.

asd
</div>
<div id="limitations" outline_label="Limitations" outline_indent="0" markdown="1">
### Limitations ###

- Tested with 'apptainer version 1.2.5-1.el8' and 'Docker version 24.0.5, build 24.0.5-0ubuntu1~22.04.1'.
- Pathlines using multiple mpi ranks are currently not always correctly connected in ParaView.
- Time series data is currently unavailable

</div>