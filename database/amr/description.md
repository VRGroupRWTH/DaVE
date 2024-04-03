<div id="description" outline_label="Description" outline_indent="0" markdown="1">
### Description ###
Datasets that describe a two- or three-dimensional fields most oftenly contain just an two- or three-dimensonal array which describes the field at a descrete set of sample points.
These sample points are often disributes in a regular grid ofer the domain of the field where by the resolution of the grid is controlled by the user during the creation of the dataset.
Choosing a the right resolution is not always easy as a too high resolution would easily lead to an enormously large dataset where as a too low grid resolution would lead to an inprecise representation and a loss of smaller features of the field.
Besides that, using a grid for the placement of the sample points is not always optimal.
When storing a three-dimensional field that is only defined on the surface of an object, for example, many sample points would fall into the empty space where the field is undefined.
As such a lot of space would be wasted by sample points that are undefined.

In this example, Adaptive Mesh Refinement is demonstrated which allows for a more optimal placement of the sampling points.
Instad of using a single resolution of the entire dataset, Adaptive Mesh Refinement allows for higher resolutions in areas where the field exhibits fine details and lower resolutions in areas where the field is constant or not defined at all.
For the illustration of this otimization strategy a dataset was chosen that describes the Mandelbrot set [1](#reference_dataset).
The image that is created when executing the example shows the adaptive grid structure that is sued to store the Mandelbrot set where by the color of te grid indicates how many times the grid was subdivided.
Due to the infietly complicated boundary of the Mandelbrot set that comes from it fractal nature, the grid is subdivided mutliple times at the boundary to capture the field as closley as possible.
In the center however, a very spares grid is used as the field is constant in this area.

As this example can be used with costume datasets, it is a valiable debug tool with which the grid structure of a dataset can be explored and potential sampling problems can be identified.
</div>
<div id="instructions" outline_label="Instructions" outline_indent="0" markdown="1">
### Instructions ###
Under the files that can be downloaded for this particular example, there is the script file `amr_script.sh` that when executed visualizes the grid structure of the provided dataset. 
The script can be started using the following terminal command
```
./amr_script.sh
```
In some cases it is neccessary to first mark the script as executible which can be done by running the following line in the terminal
```
chmod +x amr_script.sh
```
After a successful execution of the script, the image `arm.png` containing the final visualization of the provided dataset is placed in the folder `output`. 
</div>
<div id="limitations" outline_label="Limitations" outline_indent="0" markdown="1">
### Limitations ###
Currently the example only accepts dataset in the `.vthb` or `.vth` format.
Other file formats are tehoretically possible but would required extensive changes to the `amr_script.py` script file as the reader used by it would need to be replaced.
</div>
<div id="references" outline_label="References" outline_indent="0" markdown="1">
### References ###
1. <span id="reference_dataset">Dataset ?</span>
</div>