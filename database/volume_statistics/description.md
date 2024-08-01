## Description ##
Visualizing a scalar dataset just by computing an isosurface is often not enough to gain a deep understanding of the data.
Depending on the use case, there may be research questions that cannot be answered by an isosurface alone and therefore require further evaluation steps.
Such an evaluation process that needs multiple steps is quite common and subject of this example.
The evaluation that that is performed in this example is consists of three steps and classifies, based on a given density field, connected areas of high density with respect to their volume.
The dataset that is provided along with this example describes the mixing behavior of a two-phase liquid, more precisely the Rayleigh–Taylor instability [1](#reference_dataset).
The first step that the example performs is an isovolume extraction, which identifies the areas of high density within the dataset.
An isovolume is simply computed by clipping away all cells of the dataset whose interior values do not lie in a user defined range.
After that, the connected areas within the density field are identified by checking which cells of the remaining cells of the dataset are adjacent to each other.
Finally, the example computes the volume of these mesh pieces and displays the resulting volume distribution in a histogram.

## Instructions ##
The file archive that comes with this example contains the script file `volume_statistics_script.sh` that when executed performs the volume component evaluation on the provided dataset.
The script can be started using the following terminal command
```bash
./volume_statistics_script.sh
```
In some cases, the script file `volume_statistics_script.sh` is not detected by the operating system as an executable file.
If this happens, the following command can be used to mark the script file as executable
```bash
chmod +x volume_statistics_script.sh
```
After a successful execution of the script, the image `volume_statistics.png` containing the final visualization of the provided dataset is placed in the folder `output`. 

When using a custom dataset, it is important to make sure that the example uses the correct scalar field.
By default, the example always uses the field within the dataset named `Images`, but in the case of a custom dataset, a field with a different name may need to be selected.
To configure the name of the field accessed by the example, change the lines of the `volume_statistics_trace.py` script file that are marked with the keyword `OWN_DATA`.
Instead of the default field `Images`, these lines must contain the name of the desired field.
One of the lines that needs to be modified when changing the field name is shown below.
```python
isoVolume1.InputScalars = ['POINTS', 'ImageFile']
```

The range that the user can choose for the creation of the isovolume is controlled by the following line of the `volume_statistics_trace.py script.
```python
isoVolume1.ThresholdRange = [2.0, 3.000028610229492]
```
The first value defines the lower and the second number defines the upper bound of the range.
By default, the example discards the area with the largest volume which might be not necessary for custom datasets.
To disable this behavior, removed the following line of the `volume_statistics_trace.py` script file
```python
full_volume_range[1] -= 1
```
## Limitations ##
Currently this example only accepts dataset in the `.nrrd` file format as other formats would require wider changes to the loading process.
Besides that, the pipeline contains a programmable filter summing up the volume for each connected component.
The problem with this particular type of filter is that it does not properly work in the distributed case.

## References ##
1. [<span id="reference_dataset">Andrew W. Cook, William Cabot and Paul L. Miller, 2004, "A time step of a density field in a simulation of the mixing transition in Rayleigh-Taylor instability.", https://klacansky.com/open-scivis-datasets/miranda/.</span>](https://klacansky.com/open-scivis-datasets/miranda/)