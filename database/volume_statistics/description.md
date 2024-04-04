#### Description ####
Iso volume extraction followed by a computation of volumes on connected components. A threshold is applied on the volume and the results are rendered and the distribution of volumes of the connected components is shown in a histogram.

#### Instructions ####
To execute the example just run

```
./volume_statistics_script.sh
```

If the script is not executible run the following command

```
chmod +x volume_statistics_script.sh
```

#### Limitations ####
The pipeline contains a programmable filter summing up the volume for each connected component. This filter does not work correctly in the distributed case.
