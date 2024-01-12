#### Description ####
Pathline and so on 

#### Instructions ####
To execute the example just run

```
./pathline_script.sh
```

If the script is not executible run the following command

```
chmod +x pathline_script.sh
```

For entering your own data, search for "OWN_DATA" comments in the volumerender_trace.py file and change the file according to the instructions.

#### Limitations ####
Tested with 'apptainer version 1.2.5-1.el8' and 'Docker version 24.0.5, build 24.0.5-0ubuntu1~22.04.1'.

Pathlines using multiple mpi ranks are currently not always correctly connected in ParaView.
