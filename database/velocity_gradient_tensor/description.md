## Description ##
Tensors are used in many research areas such as mechanics of physics, but they are notoriously difficult to visualize as they often require more than three dimensions to be displayed.
Due to that they are mostly visualized by deriving certain properties from them and then visualizing these properties instead.
Second order tensors describing a mapping from vector to vector on the other hand are often visualized by showing their effect on three-dimensional objects.
The linear mapping that this class of tensors describes can be interpreted as a geometrical transformation that can be used to modify the shape of an object.
Applying such a tensor, for example, to a unit sphere creates an ellipsoid whose shape makes certain properties of the tensor, such as the eigenvectors and eigenvalues, visible.
The resulting visualization is similar to a glyph based visualization as demonstrated in <a href="/visualization?name=Vector Glyphs of Fluid Flow">this</a> example.

Based on a dataset coming from a mechanical simulation, this example visualizes a given tensor field by showing the affect of the tensors on unit spheres.
The example derives the tensor field form a dataset that captures the exhaust flow of a running jet engine [1](#reference_dataset).
More precisely, the gradient of the velocity field is computed which is a field of second order tensors.
After that, the example spawns a set of unit spheres in the domain of the dataset and uses the tensor field to transform the spheres.
Finally, the example computes the magnitude of the velocity field and uses the resulting scalar field to color the transformed spheres.

## Instructions ##
The file archive that is provided for this example contains the script file `velocity_gradient_tensor_script.sh` that when executed visualizes a tensor field using ellipsoidal glyphs.
The script can be started using the following terminal command
```bash
./velocity_gradient_tensor_script.sh
```
In some cases it is necessary to first mark the script as executable which can be done by running the following line in the terminal
```bash
chmod +x velocity_gradient_tensor_script.sh
```
After a successful execution of the script, the image `velocity_gradient_tensor.png` containing the final visualization of the provided dataset is placed in the folder `output`. 

The vector field that the example uses for the visualization is determined by the lines of the `velocity_gradient_tensor_trace.py` script that are marked with the keyword `OWN_DATA`.
By default, the example used the field with the name `ImageFile`, but when using a custom dataset it might be necessary to select field with a different name.
One of the lines need to be modified when changing the name of the field is shown in the following
```python
reader.PointArrayStatus = ['ImageFile']
```

## Limitations ##
Currently this example only supports dataset that are stored in the `.vti` file format.
Other file formats are theoretically possible but would require wider changes to the script `velocity_gradient_tensor_trace.py` as a different file reader would be required.

## References ##
1. [<span id="reference_dataset">Christoph Garth, March 9, 2020, "Simulation of a jet flow", IEEE Dataport, doi: https://dx.doi.org/10.21227/qjxp-kc31.</span>](https://dx.doi.org/10.21227/qjxp-kc31)