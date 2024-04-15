<div id="description" outline_label="Description" outline_indent="0" markdown="1">
### Description ###
Subset of the mantle data set from SciVis contest with four heatmaps for four different fields. Additionally scatterplots are provided.

</div>
<div id="instructions" outline_label="Instructions" outline_indent="0" markdown="1">
### Instructions ###
To execute the example just run

```
./scatterplots_script.sh
```

If the script is not executible run the following command

```
chmod +x scatterplots_script.sh
```

</div>
<div id="limitations" outline_label="Limitations" outline_indent="0" markdown="1">
### Limitations ###
Currently the `scatterplots_trace.py` only supports datasets that are stored in the NetCDF (Network Common Data Form) format.
Datasets that are stored in this particular format can be identified by the file extension `.nc`.
Other file formats are theoretically possible but would require extensive changes to the `scatterplots_trace.py` file as the reader used by the script would need to be replaced.

</div>
<div id="references" outline_label="References" outline_indent="0" markdown="1">
### References ###
1. [<span id="reference_dataset">2021, "SciVis Contest 2021: Earth's Mantle Convection", https://scivis2021.netlify.app/data/</span>](https://scivis2021.netlify.app/data/)
</div>