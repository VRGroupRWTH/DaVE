<div id="description" outline_label="Description" outline_indent="0" markdown="1">
### Description ###
Iso volume extraction followed by a computation of volumes on connected components. A threshold is applied on the volume and the results are rendered and the distribution of volumes of the connected components is shown in a histogram.

</div>
<div id="instructions" outline_label="Instructions" outline_indent="0" markdown="1">
### Instructions ###
To execute the example just run

```
./volume_statistics_script.sh
```

If the script is not executible run the following command

```
chmod +x volume_statistics_script.sh
```

</div>
<div id="limitations" outline_label="Limitations" outline_indent="0" markdown="1">
### Limitations ###
The pipeline contains a programmable filter summing up the volume for each connected component. This filter does not work correctly in the distributed case.

</div>
<div id="references" outline_label="References" outline_indent="0" markdown="1">
### References ###
1. Dataset ?
</div>