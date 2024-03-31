#### Description ####
Perhaps the most common method of visualizing vector fields or fields comprising multiple scalar attributes is by using glyphs.
In the field of data visualization, glyphs are markers that describe the properties of a given field at a specific location.
These glyphs are often distributed in a regular grid within the domain of the given input field.
The field is then used to control different properties of the glyphs such as the color, size or orientation.
There are several types of glyphs that can be used, such as circles, spheres or arrows.
This is just a small selection of the most widely used glyphs, but there are many more, as basically any shape can be used as a glyph.
However, each glyph type has advantages and disadvantages that make it more or less suitable for representing certain attributes.
For example, arrows are well suited for the visualization of attributes describing directions or orientations, such as flow directions, but they are less fitting for non-directional scalar attributes, such as pressures or temperatures.
What makes glyphs particularly interesting is their ability to visualize multiple quantities at once, which is also known as multivariate data visualization.
For example, arrow glyphs can be used to visualize more than just the flow of gas in a running combustion engine.
At the same time, the lengths of the arrows can be used to visualize the velocity of the gas, while the color of the arrow can be changed to reflect the temperature of the gas.

#### Instructions ####
The visualization template that can be configured and downloaded below contains the shell script `glyphs_script.sh` that when executed visualizes the provided dataset using glaphs.
The script can be started by ruinning the following command in the terminal
```
./glyphs_script.sh
```
In some cases it is neccessary to first mark the script as executible which can be done by running the following line in the terminal
```
chmod +x glyphs_script.sh
```
After a successful execution of the script, the image `glyphs.png` containing the final visualization of the provided dataset is placed in the folder `output`.

A dataset may contain more than one attribute that can be visualized using glyphs.
The selection of the attribute is determined by the lines in the file `glyphs_script.py` that are marked with the keyword `OWN_DATA`.
When changing the attribute, these lines need to be modified such that they contain the name of the desired attribute.
Especially when using custom data, it is important to make sure that the correct attribute is selected for the creation of the glyphs.
One of the lines that would need to be changed when using a different dataset is shown below
```
glyph1.OrientationArray = ['POINTS', 'ImageFile']
```
By default the script uses the attribute with the name `ImageFile`.

There are many options with which the glyphs can be customized. 
For example the shape of the glyphs can be controlled using the following line of the `glyphs_script.py` script
```
glyph1 = pvs.Glyph(registrationName='Glyph1', Input=reader, GlyphType='Arrow')
```
By default the script uses `GlyphType='Arrow'` meaning that arrows are used for the visualization.
Alternatives are `GlyphType='Cone'` for cones or `GlyphType='Box'` for boxes.
Depending on the dataset it might be also neccessary to change the scale of the glyphs which can be controlled using the following line of the `glyphs_script.py` script
```
glyph1.ScaleFactor = 0.025
```
For further options please look at the documentation of the ParaView Python API <span class="visualization-reference">[[1](#citation_paraview_python_api)]</span>. Otherwise it is also possible to load the file `glyphs_script.py` directly into ParaView granting even more options for costumizations.

#### Limitations ####
Currently only a shell script is provided which can be not that easily executed under Windows.

### References ###
<span id="citation_paraview_python_api" class="ms-2 visualization-reference">[1]</span> [Kitware, Inc. , March 26, 2024, "ParaView’s Python documentation!", https://kitware.github.io/paraview-docs/v5.10.1/python/index.html.](https://kitware.github.io/paraview-docs/v5.10.1/python/index.html)

<span id="citation_preview_dataset" class="ms-2 visualization-reference">[2]</span> [Christoph Garth, March 9, 2020, "Simulation of a jet flow", IEEE Dataport, doi: https://dx.doi.org/10.21227/qjxp-kc31.](https://dx.doi.org/10.21227/qjxp-kc31)