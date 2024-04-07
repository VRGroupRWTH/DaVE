<div id="description" outline_label="Description" outline_indent="0" markdown="1">
### Description ###
Heatmaps are a widely used visualization method with which mostly two-dimensional scalar datasets can be easily explored.
The creation of heatmaps is simple as the scalar values of the dataset are simply mapped to color values.
The mapping of the scalar dataset values to the color values can be defined using different methods, but most commonly they are defined based on a user defined set of key colors at specific input values of the dataset.
The color of every value of the dataset that lies in between these key color values is created by linear interpolation of the closest key colors.
Even though heatmaps mostly 
</div>
<div id="instructions" outline_label="Instructions" outline_indent="0" markdown="1">
### Instructions ###
To execute the example just run

```
./heatmap_script.sh
```

If the script is not executible run the following command

```
chmod +x heatmap_script.sh
```

As shown below, the script `heatmap_trace.py` assumes that the dataset stores the data in the order: `latitude`, `radius`, `longitude`.
In case this is not the case the format needs to be changed accordingly.
```
reader.Dimensions = '(lat, r, lon)'
```
Besides that the script assumes that the attribute used for the coloring has the name `temperatur`
```
clip2Display.ColorArrayName = ['CELLS', 'temperature']
```

Maybe the transfer function needs to be changed as well
```
temperatureLUT.RGBPoints = [100.0, 0.0, 0.0, 0.0, 200.0, 1.0, 0.0, 0.0, 300.0, 1.0, 1.0, 1.0]
```

</div>
<div id="limitations" outline_label="Limitations" outline_indent="0" markdown="1">
### Limitations ###
None
</div>
<div id="references" outline_label="References" outline_indent="0" markdown="1">
### References ###
1. [<span id="reference_dataset">2021, "SciVis Contest 2021: Earth's Mantle Convection", https://scivis2021.netlify.app/data/</span>](https://scivis2021.netlify.app/data/)
</div>