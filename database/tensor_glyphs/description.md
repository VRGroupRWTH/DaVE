### Description ###
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

This example demonstrates the use of ellipsoid tensor glyphs using a three-dimensional dataset that describes the stresses resulting from molecular dynamics within within an atom grid.
The example was created using standard parameters within the LAMMPS Molecular Dynamics Simulator [1](#lammps) and a grid of 4000 atoms using Nickel potentials and one disrupting Nickel atom close to the center.
The data within the simulation's dump file is converted to vtk using the `lammps2vtk.m` file provided in the resources.
The symmetric stress tensor is decomposed into the orthogonal eigenvector basis and corresponding eigenvalues and mapped onto shape and rotation of an ellipsoid glyph.
The color additionally encodes the maximum eigenvalue of the tensor.
Alternative tensor glyph representations are also available but are not included in ParaView ([2](#superquadrics), [3](#general)).

### Limitations ###
The `lammps2vtk.m` file currently assumes position and tensor files to be written into the specific dump file with certain conventions, e.g., the 6 components of the symmetric tensor instead of all 9 components defined by the 3 x 3 matrix.

### References ###
1. [<span id="lammps">A. P. Thompson et al., 2022,"LAMMPS - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales", Computer Physics Communications, doi: https://doi.org/10.1016/j.cpc.2021.108171</span>](https://doi.org/10.1016/j.cpc.2021.108171)

2. [<span id="superquadrics">Gordon Kindlmann, 2004, "Superquadric Tensor Glyphs", The Eurographics Association, doi: https://diglib.eg.org/handle/10.2312/VisSym.VisSym04.147-154</span>](https://diglib.eg.org/handle/10.2312/VisSym.VisSym04.147-154)

3. [<span id="general">T. Gerrits et al., 2016, "Glyphs for General Second-Order 2D and 3D Tensors", IEEE Transactions on Visualization and Computer Graphics, doi: https://doi.org/10.1109/TVCG.2016.2598998</span>](https://doi.org/10.1109/TVCG.2016.2598998)