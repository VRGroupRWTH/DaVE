## Description ##
This example illustrates a multivariate visualization using glyphs.
The dataset that is attached to this example was created by simulating a cylinder filled with pure water where the top of the cylinder is covered by an inexhaustible layer of salt.
Over time the salt dissolves into the water and forms regions with high salt concentration also known as viscous fingers.
Along with a field describing the salt concentration distribution within the cylinder, the dataset stores a velocity field that describes the water movement inside the container.
The example shows the concentration filed using glyphs shaped like spheres where the velocity of the water is illustrated by arrow glyphs.
To get a better understanding of the speed with which the water moves, the length of the arrows as well as their color are changed depending on the magnitude of the velocity field.
With increasing velocity magnitude the arrows get longer and the color of the arrows turns form dark red to yellow.
Similarly, the spheres are scaled and colored based on the concentration field.
As the concentration increases the spheres become larger, and their color turns from bright green to blue.

## Instructions ##
The file archive that is provided for this example contains the script file `pointcloud_script.sh` that when executed visualized a tensor field using ellipsoidal glyphs.
The script can be started using the following terminal command
```bash
./pointcloud_script.sh
```
In some cases it is necessary to first mark the script as executable which can be done by running the following line in the terminal
```bash
chmod +x pointcloud_script.sh
```
Since the example use an animation to rotate the viewer around the dataset, not a single image but instead a series of images is exported to the folder `output` after the completion of the `pointcloud_script.sh` script.

There are several parameters that need to be adjusted when applying the example to your own data.
First, the example need to be configured in such a way that it uses the desired fields of the provided dataset.
In total two fields are required, on of which must be a three-dimensional scalar field, while the other one must be a three-dimensional vector field.
By default, the example searches for a scalar field with the name `concentration` and a vector field with the name `velocity`.
The selection of the fields takes place in `pointcloud_trace.py` script and is determined by the lines marked with the keyword `OWNDATA`.
To change the selection behavior, modify these lines so that they contain the name of the desired fields.
One of the lines that would need to be modified is shown below.
```python
reader.PointArrayStatus = ['concentration', 'velocity']
```
Depending on the shape of the used dataset, it may be also necessary to scale the point and or the arrow glyphs.
The size of the point glyphs is controlled by the following line the `pointcloud_trace.py` script
```python
readerDisplay.GaussianRadius = 0.05
```
and the size of the arrow glyphs is controlled by this line of the `pointcloud_trace.py` script
```python
glyph1Display.ScaleFactor = 1.0982380867004395
```

The cylinder which surrounds the visualization of the dataset can be controlled using the following lines of the `pointcloud_trace.py` script.
```python
cylinder1 = pvs.Cylinder(registrationName='Cylinder1')
cylinder1.Resolution = 100
cylinder1.Height = 10.1
cylinder1.Radius = 5.05
cylinder1.Center = [0.0, 0.0, 5.0]
```
But there are other shapes that can be used as well to frame the dataset such as `pvs.Cylinder`, `pvs.Box` or `pvs.Sphere`.
For more information on how to configure these shapes, see the ParaView Python documentation [2](#reference_python_api).

## Limitations ##
Currently this example only accepts datasets in the `.vtu` file format as other formats would require major changes to the loading process.
Besides that there are the following known issues:
- Artifacts on the cylinder in distributed execution.

## References ##
1. [<span id="reference_dataset">2016, "SciVis Contest 2016: Simulation of viscous fingers", https://cloud.sdsc.edu/v1/AUTH_sciviscontest/2016/README.html</span>](https://cloud.sdsc.edu/v1/AUTH_sciviscontest/2016/README.html)
2. [<span id="reference_python_api">Kitware, Inc. , March 26, 2024, "ParaView’s Python documentation!", https://kitware.github.io/paraview-docs/v5.10.1/python/index.html.</span>](https://kitware.github.io/paraview-docs/v5.10.1/python/index.html)