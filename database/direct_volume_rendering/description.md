#### Description ####
Direct volume rendering **(DVR)** is one of the most commonly used methods for the visualization of three-dimensional scalar datasets.
Especially in the medical field, DVR is widely used for the visualzation of CT or MRI scans of patients.
But there are also other research areas where DVR is used, such as the field of energy conversion, where it is used to visualize gases and fumes simulated for a combustion process.
Compared to other methods 



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
However, there is still the problem that features with the same dataset value are mapped to the same opacity and color.
This means that independent of how the transfer function is defined, features with the same dataset value are always shown at the same time.

There are many different rendering techniuqes with which the opacity field defined by the transfer function can be turned into an images.
Rendering using volume ray casting
the accumulation using volme ray casting can be aplied in regular steps or using an adaptive approach
accumulation of values along a ray. it is more like an integration process. there are many ways how this intergation process can be done.

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
