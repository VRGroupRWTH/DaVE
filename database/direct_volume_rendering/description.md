<div id="description" outline_label="Description" outline_indent="0" markdown="1">
### Description ###
Direct volume rendering is one of the most commonly used methods for the visualization of three-dimensional scalar datasets.
Especially in the medical field, direct volume rendering is widely used for the visualzation of CT or MRI scans of patients.
But there are also other research areas where direct volume rendering is used, such as the field of energy conversion, where it is used for the visualization of gasses in a simulated combustion process.
Compared to for example iso-surface extraction or similar methods for the exploration of three-dimensional scalar datasets, direct volume rendering does not create an alternative representation of the dataset as for example a polygon mesh.
This direct approach has the disadvantage that the dataset can not be further simplified before it is visualized which makes this techniuqe sometimes more computationally demainding if an interactive visualization is needed.
However, what makes direct volume rendering particularly interesting is its ability to provide a in-depth view into the dataset, allowing multiple structures at different depths of the dataset to be examined simultaneously.

This example illustrates the usage of direct volume rendering in a medical context.
The dataset used in the example describes the x-ray scan of a patiens foot as a scalar field that represents the density of tissues and bones within the foot [1](#reference_dataset).
A common practice when using direct volume rendering is color the reulitng volume using a user defined look up table that assignes every value of the field a specific color.
This makes it then easier to identify different structures in the volume, as for example in this case, the bones in the foot colored in red and the less dense tissue colored in blue.
Beisdes that is also possible to coltroll the opacity of structures based on the values of the scalar field which makes it possible to cut away structures that are not of interset.
In this example, dense structures such as the bones were set to fully opaque while the tissue of the foot was made semi-transparent.

</div>
<div id="instructions" outline_label="Instructions" outline_indent="0" markdown="1">
### Instructions ###
The file archive that comes with this example when downloading it, contains the script file `volumerender_script` that when executed visualizes the provided dataset using direct volume rendering.
The script can be started using the following terminal command
```
./volumerender_script.sh
```
In some cases it is neccessary to first mark the script as executible which can be done by running the following line in the terminal
```
chmod +x volumerender_script.sh
```
After a successful execution of the script, the image `volumerender.png` containing the final visualization of the provided dataset is placed in the folder `output`. 

In case the example is used together with a custom dataset, the lines of the script `volumerender_trace.py` that are marked with the key word `OWN_DATA` need to be changed.
These lines, as for example the line shown below, need to be changed so that they match with the name of the attribut of the dataset that should be used for the visualization.
```
reader.PointArrayStatus = ['Scalars_']
```
By default, the script uses the attribute with the name `Scalars_` for the visualization.
</div>
<div id="limitations" outline_label="Limitations" outline_indent="0" markdown="1">
### Limitations ###
Currently the example only supports datasets in the `.vti` file format.
Other dataset format are possible but would require extensive changes to the `volumerender_trace.py` script file as the reader used by it would need to be changed.
</div>
<div id="references" outline_label="References" outline_indent="0" markdown="1">
### References ###
1. [<span id="reference_dataset">Philips Research, "Rotational C-arm x-ray scan of a human foot", Hamburg, Germany, https://github.com/topology-tool-kit/ttk-data/blob/dev/ctBones.vti.</span>](https://github.com/topology-tool-kit/ttk-data/blob/dev/ctBones.vti)
</div>