## Description ##
Line-Integral Convolution is a visualization technique that can be used to highlight the field lines of two- or three-dimensional vector fields. 
The method calculates the color for a specific point by integrating a noisy scalar field along a curve.
This curve starts at the point where the color is to be calculated and follows the vector field for a user-defined length.
The contribution of the noise field to the integration is often modulated by a user-defined convolution kernel, which in its simplest form weights the values of the noise field equally.
At the first glance, the result of this visualization technique is just a noisy representation of the dataset.
However, points that belong to the same field line are colored almost equally, as the curves that are traced form them are nearly identically.

In this example, line integral convolution is demonstrated in the context of a geological application.
The dataset that is provided along with this example was created by simulating the convection process that takes place in the earth's mantel [1](#reference_dataset).
Based on this dataset, the example uses Line integral convolution to visualize the velocity with which material moves in the earth's mantel.
This example nicely illustrates the advantages of this line integral convolution over other visualization techniques for vector field such as, for example, streamlines or glyphs.
These approach in particular visualize the dataset using lines or arrows which cause visual cluttering if too many of them are use or only give a rough overview of the dataset if not enough of them are used.
This problem in particular does not arise when using line integration convolution.

## Instructions ##
The file archive that is provided for this example contains the script file `lic_script.sh` that when executed visualized a dataset using line-integral convolution.
The script can be started using the following terminal command
```bash
./lic_script.sh
```
In some cases it is necessary to first mark the script as executable which can be done by running the following line in the terminal
```bash
chmod +x lic_script.sh
```
After a successful execution of the script, the image `lic.png` containing the final visualization of the provided dataset is placed in the folder `output`. 

The example assumes that the dataset owns three scalar fields named `vx`, `vy` and `vz`.
Based on these scalar fields, the velocity field is derived using the following line of the `lic_trace.py` script
```python
calculator1.Function = '(iHat*vx + jHat*vy + kHat*vz) * 1e9'
```
When using a custom dataset, it might be necessary to ether adapt this formula or down right skip this computation entirely if a vector field is already provided by the dataset.

Besides that, the dataset also has to store the scalar field in a spherical coordinate system defined by the axes `latitude (lat)`, `longitude (lon)` and `radius (r)`.
The order in which these axes are read from the dataset can be controlled using the following line of the `lic_trace.py` script
```python
reader.Dimensions = '(lat, r, lon)'
```

## Limitations ##
Currently the `lic_trace.py` only supports datasets that are stored in the NetCDF (Network Common Data Form) format.
Datasets that are stored in this particular format can be identified by the file extension `.nc`.
Other file formats are theoretically possible but would require extensive changes to the `lic_trace.py` file as the reader used by the script would need to be replaced.

Besides that, there are the following limitations:
- Artifacts in distributed execution

## References ##
1. [<span id="reference_dataset">2021, "SciVis Contest 2021: Earth's Mantle Convection", https://scivis2021.netlify.app/data/</span>](https://scivis2021.netlify.app/data/)