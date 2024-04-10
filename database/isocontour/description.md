<div id="description" outline_label="Description" outline_indent="0" markdown="1">
### Description ###
The extraction of isocontours is a fundamental visualization technique used in many research areas for the exploration of primarily three-dimensional scalar datasets.
In this example, the extraction of an isocontour is demonstrated for a medical use case in which the x-ray scan of a paitents foot needs to be visualized.
The dataset used in this example contains a dimensional scalar field that captures the density of the tissues and bones within the foot of a patient [1](#reference_dataset).
The extraction of isocontours is particularly interesting in this use case as it allows for an isolated view on specific structures within the foot.
By selecting an appropriate threshold for the extraction, it is for example possible to visualize only the bones in the foot, which enables the diagnosis of potential fractures.
</div>
<div id="instructions" outline_label="Instructions" outline_indent="0" markdown="1">
### Instructions ###
The archive that can be downloaded after the configuration of the example contains the shell script `isocontour_script.sh` that creates an isocontour for the provided dataset.
The script can be started by ruinning the following command in the terminal
```
./isocontour_script.sh
```
In some cases it is neccessary to first mark the script as executible which can be done by running the following line in the terminal
```
chmod +x isocontour_script.sh
```
After a successful execution of the script, the image `isocontour.png` containing the final visualization of the provided dataset is placed in the folder `output`.


```
contour1.ContourBy = ['POINTS', 'Scalars_']
```

An important property for the extration of the isocontour is the iso surface threshold that defines the target surface.
This parameter is controlled by the following line of the `isocontour_trace.py` file
```
contour1.Isosurfaces = [100.0]
```


</div>
<div id="limitations" outline_label="Limitations" outline_indent="0" markdown="1">
### Limitations ###
Currently this example only accepts dataset in the `.vti` file format as other formats would required wider changes to the loading process.
</div>
<div id="references" outline_label="References" outline_indent="0" markdown="1">
### References ###
1. [<span id="reference_dataset">Philips Research, "Rotational C-arm x-ray scan of a human foot", Hamburg, Germany, https://github.com/topology-tool-kit/ttk-data/blob/dev/ctBones.vti.</span>](https://github.com/topology-tool-kit/ttk-data/blob/dev/ctBones.vti)
</div>