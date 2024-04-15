<div id="description" outline_label="Description" outline_indent="0" markdown="1">
### Description ###
Visualizing a scalar dataset just by computing an isosurface is often not enough to gain a deep understanding of the data.
Depending on the use case, there may be research questions that cannot be answered by an isosurface alone and therefore require further evaluation steps.
Such an evaluation process that needs multiple steps is quite common and subject of this example.
The evaluation that that is performed in this example is consists of three steps and classifies, based on a given density field, connected areas of high density with respect to their volume.
The dataset that is provided along with this example describes the mixing behavior of a two-phase liquid, more precisely the Rayleigh–Taylor instability [1](#reference_dataset).
The first step performed by the example is an isosurface extraction, which identifies the the areas of high density within the dataset.
For more information on how to extract an isocontour, see the <a href="/visualization?name=Isocontours">Isocontour</a> example.
After that, the connected areas within the density field are identified by spliting the polygonal mesh describing the isocontour into individual pieces.
Finally, the example computes the volume of these mesh pieces and displays the resulting volume distribution in a histogram.
</div>
<div id="instructions" outline_label="Instructions" outline_indent="0" markdown="1">
### Instructions ###
The file archive that comes with this example contains the script file `volume_statistics_script` that when executed performs the volume component evaluation on the provided dataset.
The script can be started using the following terminal command
```
./volume_statistics_script.sh
```
In some cases, the script file `volume_statistics_script.sh` is not detected by the operating system as an executible file.
If this happens, the following command can be used to mark the script file as executable
```
chmod +x volume_statistics_script.sh
```
After a successful execution of the script, the image `volume_statistics.png` containing the final visualization of the provided dataset is placed in the folder `output`. 

```
isoVolume1.InputScalars = ['POINTS', 'ImageFile']
isoVolume1.ThresholdRange = [2.0, 3.000028610229492]
```

```
full_volume_range[1] -= 1
```
</div>
<div id="limitations" outline_label="Limitations" outline_indent="0" markdown="1">
### Limitations ###
The pipeline contains a programmable filter summing up the volume for each connected component. This filter does not work correctly in the distributed case.

`.nrrd`

</div>
<div id="references" outline_label="References" outline_indent="0" markdown="1">
### References ###
1. [<span id="reference_dataset">Andrew W. Cook, William Cabot and Paul L. Miller, 2004, "A time step of a density field in a simulation of the mixing transition in Rayleigh-Taylor instability.", https://klacansky.com/open-scivis-datasets/miranda/.</span>](https://klacansky.com/open-scivis-datasets/miranda/)
</div>