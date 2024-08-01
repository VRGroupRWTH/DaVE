## Description ##
Heatmaps are a widely used visualization method with which mostly two-dimensional scalar datasets can be easily explored.
The creation of heatmaps is simple as the scalar values of the dataset are simply mapped to color values.
The mapping of the scalar dataset values to the color values can be defined using different methods, but most commonly they are defined based on a user defined look up table, which makes a given dataset value to a specific color.

This example illustrates the use of heatmaps in the context of a geological use case.
The dataset that comes with the example describes the convection process that takes places in the earth's mantel and was created by a simulation [1](#reference_dataset).
Using heatmaps, the temperature within the earth's mantel is mapped to color table ranging from dark red for low temperatures to yellow and white for high temperatures.
As expected, the inner core of the earth is colored by a bright yellow as it is by far the hottest part of the earth's mantel.
With in creasing distance to the earths center, the temperature decreases and the color turns from yellow to orange and finally to red.
At some points of the mantel, there are yellow regions of hot material reaching from the inner to the outer mantel.
These areas are caused by the convection and are most likely mantle plume.

## Instructions ##
After downloading, the example can be executed by running the script `heatmap_script.sh` using the following terminal command
```bash
./heatmap_script.sh
```
In some cases, the script file `heatmap_script.sh` is not detected by the operating system as an executable file.
If this happens, the following command can be used to mark the script file as executable
```bash
chmod +x heatmap_script.sh
```
After the execution of the example, the image `heatmap.png` containing the visualized dataset will be placed in the folder `output`.

The example assumes that the dataset serving as input contains a three-dimensional scalar field with the name `temperature`.
When using the example with a custom dataset, it might be necessary to change name of the scalar field.
For that, the lines in the script file `heatmap_trace.py` marked with the keyword `OWN_DATA` need to be changed accordingly so that they contain the name of the desired scalar field.
In the following, one for these lines is shown
```python
clip2Display.ColorArrayName = ['CELLS', 'temperature']
```
Additionally, the dataset also has to store the scalar field in a polar coordinate system defined by the axes `latitude (lat)`, `longitude (lon)` and `radius (r)`.
The order in which these axes are read from the dataset can be controlled using the following line of the `heatmap_trace.py` script
```python
reader.Dimensions = '(lat, r, lon)'
```

However, most importantly for the visualization is the look-up table that controls the coloring of the scalar field.
This lookup table is defined in the `heatmap_trace.py` as an array of floating point values.
An example for the structure of this array is given in the following
```python
temperatureLUT.RGBPoints = [100.0, 0.0, 0.0, 0.0,
                            200.0, 1.0, 0.0, 0.0,
                            300.0, 1.0, 1.0, 1.0]
```
Four consecutive values of the array define a key point of the loop up table.
The first value controls the dataset value that the key point will affect, while the remaining three values define the color of the key point.
More precisely, the color is specified in the RGB color space, where the value of each color component must lie in the interval from `0.0` to `1.0`.

## Limitations ##
Currently the `heatmap_trace.py` only supports datasets that are stored in the NetCDF (Network Common Data Form) format.
Datasets that are stored in this particular format can be identified by the file extension `.nc`.
Other file formats are theoretically possible but would require extensive changes to the `heatmap_trace.py` file as the reader used by the script would need to be replaced.

## References ##
1. [<span id="reference_dataset">2021, "SciVis Contest 2021: Earth's Mantle Convection", https://scivis2021.netlify.app/data/</span>](https://scivis2021.netlify.app/data/)