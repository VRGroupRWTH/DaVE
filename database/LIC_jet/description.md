### Description ###
This example shows the use of Line-Integral Convolution on a dataset that was created by simulaing the exhaustion flow of a running jet engine [1](#reference_dataset).
In order to get a getter understanding of the flow field, the result of the Line-Integral Convolution was colored based on the velocity of the flow.
Areas of high velocity, such as the center of the exhaustion jet, are colored in yellow where as areas of low velocity, such as the more turbulent edges of the jet, are colored in purple.
The resulting image shows that the exhaustion stream starts at the left side and slowly decays towards the right.
With increasing distance to the jet engine, the stream gets slower and becomes turbulent.

For more information on Line-Integral Convolution in general, see the <a href="/visualization?name=Line-Integral Convolution (LIC)">Line-Integral Convolution (LIC)</a> example.

### Instructions ###
The file archive that is provided for this example contains the script file `lic_jet_script.sh` that when executed visalized a dataset using line-integral convolution.
The script can be started using the following terminal command
```bash
./lic_jet_script.sh
```
In some cases it is neccessary to first mark the script as executible which can be done by running the following line in the terminal
```bash
chmod +x lic_jet_script.sh
```
After a successful execution of the script, the image `lic_jet.png` containing the final visualization of the provided dataset is placed in the folder `output`. 

The vector field that the example uses for the visualization is determined by the lines of the `lic_jet_trace.py` script that are marked with the keyword `OWN_DATA`.
By default the example used the field with the name `ImageFile`, but when using a custome dataset it might be neccessary to select field with a different name.
One of the lines nedd to be modified when changing the name of the field is shown in the following
```python
sliceWithPlane1Display.SelectInputVectors = ['POINTS', 'ImageFile']
```

### Limitations ###
Currently this example only supports dataset that are stored in the `.vti` file format.
Other file formats are thoretically possible but would require wider chnages to the script `lic_jet_trace.py` as a different file reader would be required.

Besides that, there are the following limitations:
- Artifacts in distributed execution

### References ###
1. [<span id="reference_dataset">2021, "SciVis Contest 2021: Earth's Mantle Convection", https://scivis2021.netlify.app/data/</span>](https://scivis2021.netlify.app/data/)