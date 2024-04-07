<div id="description" outline_label="Description" outline_indent="0" markdown="1">
### Description ###
Point Cloud ...



Glyph simulation of a vector field and a scalar field that describes the conzentration of salt solved in pure water.
The process is simulated within a cylinder that is filled with pure water.
At the top of the cylinder there is an inexhaustible layer of salt that disolves over tim into the water below.

the contentraion is simulated using glyphs that are shaped like sphere where as the velocity of the water is illustrated by arrow glyphs.
The length of the arrows is scaled depending on the velocity magnitued and the color of the arrow is also dependent on it.
Within increasing velocity magnitute the arrow truns from dark red to yellow.
The spehere that describe the concetntration scale with the concentration and are also colored differently.
with increasing concentration they are colored from birght green to blue.
</div>
<div id="instructions" outline_label="Instructions" outline_indent="0" markdown="1">
### Instructions ###
To execute the example just run

```
./pointcloud_script.sh
```

If the script is not executible run the following command

```
chmod +x pointcloud_script.sh
```

The example exports the animation as a series of images.
The animation rotates the users view around the cylinder.

</div>
<div id="limitations" outline_label="Limitations" outline_indent="0" markdown="1">
### Limitations ###
- artifacts on the cylinder in distributed execution

</div>
<div id="references" outline_label="References" outline_indent="0" markdown="1">
### References ###
1. [<span id="reference_dataset">2016, "SciVis Contest 2016: Simulation of viscous fingers", https://cloud.sdsc.edu/v1/AUTH_sciviscontest/2016/README.html</span>](https://cloud.sdsc.edu/v1/AUTH_sciviscontest/2016/README.html)
</div>