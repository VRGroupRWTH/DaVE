### Description ###
This example shows the use of Line-Integral Convolution on a dataset that was created by simulating the exhaust flow of a running jet engine [1](#reference_dataset).
In order to get a getter understanding of the flow field, the result of the Line-Integral Convolution was colored based on the velocity of the flow.
Areas of high velocity, such as the center of the exhaust flow, are colored in yellow where areas of low velocity, such as the more turbulent edges of the jet, are colored in purple.
The resulting image shows that the exhaust stream starts on the left side and slowly decays towards the right.
With increasing distance to the jet engine, the stream gets slower and becomes turbulent.

For more information on Line-Integral Convolution in general, see the <a href="/visualization?name=Line-Integral Convolution (LIC) of Earth Mantel Convection">this</a> example.

### Instructions ###
The file archive that is provided for this example contains the script file `lic_jet_script.sh` that when executed visualized a dataset using line-integral convolution.
The script can be started using the following terminal command
```bash
./lic_jet_script.sh
```
In some cases it is necessary to first mark the script as executable which can be done by running the following line in the terminal
```bash
chmod +x lic_jet_script.sh
```
After a successful execution of the script, the image `lic_jet.png` containing the final visualization of the provided dataset is placed in the folder `output`. 

The vector field that the example uses for the visualization is determined by the lines of the `lic_jet_trace.py` script that are marked with the keyword `OWN_DATA`.
By default, the example used the field with the name `ImageFile`, but when using a custom dataset it might be necessary to select field with a different name.
One of the lines need to be modified when changing the name of the field is shown in the following
```python
sliceWithPlane1Display.SelectInputVectors = ['POINTS', 'ImageFile']
```

### Limitations ###
Currently this example only supports dataset that are stored in the `.vti` file format.
Other file formats are theoretically possible but would require wider changes to the script `lic_jet_trace.py` as a different file reader would be required.

Besides that, there are the following limitations:
- Artifacts in distributed execution

### References ###
1. [<span id="reference_dataset">Christoph Garth, March 9, 2020, "Simulation of a jet flow", IEEE Dataport, doi: https://dx.doi.org/10.21227/qjxp-kc31.</span>](https://dx.doi.org/10.21227/qjxp-kc31)