### Description ###
Visualization techniques commonly used for two-dimensional datasets can be applied to slices of three-dimensional datasets as well.
The content of a slice is usually defined by a plane that cuts through the domain of the three-dimensional dataset.
Although the users can choose the orientation and location of the planes arbitrarily, they are often aligned with one of the three primary axes of the dataset to extract the coordinate surface at a specific location.
However, slices have the disadvantage that they only provide a limited insight into the dataset.
Since they only show a two-dimensional subset of the dataset, three-dimensional structures and the relations between them can not that easily be explored.

Based on an medical use case, this example shows the use of multple slices that are aligned to the primary axis of the dataset.
In comparison to other examples that only create a screenshot, this exmaple produces a Chinema database file which can be interactiveley explored using tools such as Cinema:View [1](#reference_cinema_view).
When loading the database using Cinema:View, the user can select the slices that are shown using slides.
In addtion ot showing the slices of the primary axis in isolation, the tool also provides a visualization that shows all three slices at once.
The dataset that was chosen for this example represents the x-ray scan of a patient's foot as an scalar field which captures the densities of bones and tissues within the foot [2](#reference_dataset).

### Instructions ###
The file archive that comes with this example when downloading it, contains the script file `multiple_slice_script` that when executed creates the Chinema database for the provided dataset.
The script can be started using the following terminal command
```
./multiple_slice_script.sh
```
In some cases it is neccessary to first mark the script as executible which can be done by running the following line in the terminal
```
chmod +x multiple_slice_script.sh
```
After a successful execution of the script, the Chinema database file `multiple_slice.cdb` containing the slices is placed in the folder `output`. 

In case the example is used together with a custom dataset, the lines of the script `multiple_slice_trace.py` that are marked with the key word `OWN_DATA` need to be changed.
These lines, as for example the line shown below, need to be changed so that they match with the name of the attribut of the dataset that should be used for the visualization.
```
reader.PointArrayStatus = ['Scalars_']
```
By default, the script uses the attribute with the name `Scalars_` for the visualization.

<!--One of the tools with which the resulting Chinema database can be shown is the tool Cinema:View which needs to be downloaded seperatly [1](#reference_cinema_view).
After downloading the Github repository as an zip-File, -->

### Limitations ###
Currently the example only supports datasets in the `.vti` file format.
Other dataset format are possible but would require extensive changes to the `multiple_slice_trace.py` script file as the reader used by it would need to be changed.

### References ###
1. [<span id="reference_cinema_view">"Cinema:View: A simple viewer that displays a single or multiple Cinema databases.", https://github.com/cinemascience/cinema_view</span>](https://github.com/cinemascience/cinema_view)
2. [<span id="reference_dataset">Philips Research, "Rotational C-arm x-ray scan of a human foot", Hamburg, Germany, https://github.com/topology-tool-kit/ttk-data/blob/dev/ctBones.vti.</span>](https://github.com/topology-tool-kit/ttk-data/blob/dev/ctBones.vti)