#### Description ####
Direct volume rendering **(DVR)** is an common approach for the visualization of volumetric datasets.
The samples of these volumetic datasets are aranged in a regular grid structure such that every slice of the dataset would be equvivalent to an image.
The sample values it self are real-valued meaning that they do not contain vectors or other higher dimensional structrues such as tensors.
In the medical field, DVR is oftent used for the visualization of CT or MRI scans and in the field of energy conversion, DVR is used for the visualization of combustion simulations.
In general, DVR is often used for materials that are semi-transparaent in the real world such as luquids, fluids, gases or fumes.
Compared to other methos with which volumetric datasets can be rendered such as iso-surface extraction, direct volume rendering does not convert the volume into another representation such as an polygon mesh.
Instead, the image is directly derived from the volumetric dataset which has disadvantages and also advantages.
First, direct volume rendering mostly more computationally demanding as for example an mesh representation of the volume.
On the other hand however, the rendering can show different layers of the volumes ad once and also no pre-processing is required.

An fundamental part of direct volume rendering is the transfer function **(TF)** which is used to derive the parameters required for rendering from the input dataset.
The transfer function is used to define two parameters, the opacity which defines how strong the view into the volume is blocked by at a given location as well as the color at a give location of the volume.
The transfer function defines a mapping from dataset sample to opacity and color.
There are different approaches how the transfer function can be defined.
One way would be using a piecewise linear function over the domain of the input samples.
Another way would be using lookup tables such as gradient textures.

In most cases the transfer function has to be defined by the user which can be difficult as it often requires many changes to highlight a specifiy feature within the dataset.
There are technique with which the definition of the transfer function can be automated **[[1](#citation_1), [2](#citation_2)]**.
However, there is still the problem that features with the same dataset value are mapped to the same opacity and color.
This means that independent of how the transfer function is defined, features with the same dataset value are always shown at the same time.

There are many different rendering techniuqes with which the opacity field defined by the transfer function can be turned into an images.

The most common apprach for the redering of volumes is volume ray casting.



Rendering using volume ray casting
the accumulation using volme ray casting can be aplied in regular steps or using an adaptive approach
accumulation of values along a ray. it is more like an integration process. there are many ways how this intergation process can be done. [Maybe some references for different integration strategies]

Rendering using textures and 3D slices

Rendering using splats


Lighting and scattering for the vizualization. [Reference for different physically based scattering models for volume datasets, other references for the lighting of the dataset.]
Different models for the simulation of light scattering for the shading of the dataset.
Computation of the normal based on the gradient of the scalar field.

#### Instructions ####
To execute the example just run

```
./volumerender_script.sh
```

If the script is not executible run the following command

```
chmod +x volumerender_script.sh
```

For entering your own data, search for "OWN_DATA" comments in the volumerender_trace.py file and change the file according to the instructions.

#### Limitations ####
Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

#### References ####
<strong id="citation_1">[1]</strong> Ljung, P., et al. "State of the Art in Transfer Functions for Direct Volume Rendering", in *Computer Graphics Forum*, vol. 35, no. 3, pp. 669-691, 2016.

<strong id="citation_2">[2]</strong> Ljung, P., et al. "State of the Art in Transfer Functions for Direct Volume Rendering", in *Computer Graphics Forum*, vol. 35, no. 3, pp. 669-691, 2016.