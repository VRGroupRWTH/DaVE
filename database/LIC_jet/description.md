<div id="description" outline_label="Description" outline_indent="0" markdown="1">
### Description ###
Line-Integral Convolution ...

</div>
<div id="instructions" outline_label="Instructions" outline_indent="0" markdown="1">
### Instructions ###
To execute the example just run

```
./lic_jet_script.sh
```

If the script is not executible run the following command

```
chmod +x lic_jet_script.sh
```

</div>
<div id="limitations" outline_label="Limitations" outline_indent="0" markdown="1">
### Limitations ###
Currently this example only supports dataset that are stored in the `.vti` file format.
Other file formats are thoretically possible but would require wider chnages to the script `lic_jet_trace.py` as a different file reader would be required.

Besides that, there are the following limitations:
- artifacts in distributed execution
</div>
<div id="references" outline_label="References" outline_indent="0" markdown="1">
### References ###
1. [<span id="reference_dataset">2021, "SciVis Contest 2021: Earth's Mantle Convection", https://scivis2021.netlify.app/data/</span>](https://scivis2021.netlify.app/data/)
</div>