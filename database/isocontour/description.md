### Description ###
The extraction of isocontours is a fundamental visualization technique used in many research areas for the exploration of primarily three-dimensional scalar datasets.
In this example, the extraction of an isocontour is demonstrated for a medical use case in which the x-ray scan of a patients foot needs to be visualized.
The dataset used in this example contains a dimensional scalar field that captures the density of the tissues and bones within the foot of a patient [1](#reference_dataset).
The extraction of isocontours is particularly interesting in this use case, as it allows for an isolated view on specific structures within the foot.
By selecting an appropriate threshold for the extraction, it is for example possible to visualize only the bones in the foot, which enables the diagnosis of potential fractures.

### Instructions ###
The file archive that is provided for this example contains the shell script `isocontour_script.sh` that creates an isocontour for the input dataset.
The script can be started by running the following command in the terminal
```bash
./isocontour_script.sh
```
In some cases it is necessary to first mark the script as executable which can be done by running the following line in the terminal
```bash
chmod +x isocontour_script.sh
```
After a successful execution of the script, the image `isocontour.png` containing the visualized dataset is placed in the folder `output`.

An important aspect to keep in mind is that a dataset can contain multiple scalar fields at the same time.
By default, the example uses the scalar field with the name `Scalars_`, but depending on the dataset it might be necessary to select another field with a different name.
The field that is used by the example can be changed by modifying the lines of the script file `isocontour_trace.py` that are marked with the comment `OWN_DATA`.
More precisely, the default field name `Scalars_` needs to be replaced by the name of the desired scalar field.
On of the lines that need to be adapted is shown in the following 
```python
contour1.ContourBy = ['POINTS', 'Scalars_']
```

An important property for the extraction of the isocontour is the threshold that defines the target surface.
This parameter is controlled by the following line of the `isocontour_trace.py` file
```python
contour1.Isosurfaces = [100.0]
```

### Limitations ###
Currently this example only accepts dataset in the `.vti` file format as other formats would require wider changes to the loading process.

### References ###
1. [<span id="reference_dataset">Philips Research, "Rotational C-arm x-ray scan of a human foot", Hamburg, Germany, https://github.com/topology-tool-kit/ttk-data/blob/dev/ctBones.vti.</span>](https://github.com/topology-tool-kit/ttk-data/blob/dev/ctBones.vti)