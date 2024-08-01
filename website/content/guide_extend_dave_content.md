## DaVE's Architecture ##

### Database ###
The database of DaVE contains a selection of commonly used visualization techniques and provides documentation and additional resources for them. Each entry comes with an easy-to-use, easy-to-extend example that can be downloaded and executed on your local hardware or on HPC clusters with slurm and MPI, provided slurm and singularity/apptainer (or docker) are available.

#### Database Structure ####
DaVE's database is a simple file hierarchy, where each entry is represented by a directory. Each example contains further subdirectories. The _images_ folder stores all images to show in the gallery view and the example page. The _scene_ folder contains information for the interactive preview that some examples provide. The _resources_ directory contains all necessary files for executing this example. In general, this entails a shell script for execution and in the case of [ParaView](https://www.paraview.org/) visualizations, a Python trace file. The description markdown file contains all the text describing the visualization, its application, providing additional references and instructions for executing and adapting the example. The [visualization.yaml](#Visualization_Metadata) contains all the information about the tags, which container image to use, which images to show etc.

```text
database/
├─ example/
│  ├─ images/
│  ├─ resources/
│  ├─ scene/
│  ├─ description.md
│  ├─ visualization.yaml
```

### Visualizations ###
DaVE tries to cover a wide range of visualization methods from different applications.
Additionally, the provided examples should be executable on a diverse set of computing resources. In order to categorize and organize each of the example visualizations the meta data for each example is stored in a yaml file.

#### Visualization Metadata ####
At the top name and date of creation are given.

```yaml
name: "<Name of the example>"
date: 1900-01-01
```

These are followed by the [tags](#Tags), which have a name, a type (technique | domain) and an abbreviation if they are long.

```yaml
tags:
- name: "Name of technique related tag"
  type: "technique"
- name: "Name of domain related tag"
  type: "domain"
  abbreviation: "Abbreviation of tag name"
```

Next, paths for images and the interactive scene are given. Multiple images can be listed here, but only the first is shown as thumbnail. The scene can be omitted if no interactive preview is available.

```yaml
images:
  - "images/volumerender.png"

scene: "scene/index.json"
```

The list of resources at the bottom of each example page is defined here. Each resource has a name, type and date. Depending on, where the resource resides a path or url is given.

```yaml
resources:
  - name: "volumerender_trace.py"
    type: "Script"
    date: 2023-11-29
    path: "resources/volumerender_trace.py"
  - name: "ctBones.vti"
    type: "Dataset"
    date: 2023-11-29
    url: "https://raw.githubusercontent.com/topology-tool-kit/ttk-data/dev/ctBones.vti"
  - name: "ParaView 5.11.1"
    type: "Docker Image"
    date: 2024-01-09
    url: "https://github.com/orgs/scivislab/packages/container/paraview/165958085?tag=5.11.1"
  - name: "ParaView 5.11.1"
    type: "Dockerfile"
    date: 2024-01-09
    path: "resources/Dockerfile"
```

For the creation of the downloadable templates the usable container techniques have to be listed. As well as, the different commands for execution. For ParaView examples a trace file has to be provided. The given script uses all information given here to execute the example, in this case the ParaView trace, with the given command and the selected container platform. Finally, a docker container URI has to be provided.

```yaml
templates:
  - techniques:
      - "docker"
      - "singularity"
    commands:
      - type: "local"
        run: "pvbatch volumerender_trace.py"
      - type: "mpi"
        run: "pvbatch volumerender_trace.py"
      - type: "slurm"
        run: "pvbatch volumerender_trace.py"
    trace: "resources/volumerender_trace.py"
    script: "resources/volumerender_script.sh"
    container:
      url: "ghcr.io/scivislab/paraview:5.11.1"
```

Each example comes with its own default dataset, which has to be specified here. The identifier is used in the execution script, while the name and description are displayed during template customization via the wizard. Datasets should have a url, where it can be downloaded. Alternatively, for small datasets these can also be stored in the resource directory and their path has to be given here in order for them to be included in the template. Multiple datasets can be defined here.

```yaml
datasets:
  - name: "Volume"
    identifier: "DATASET_VOLUME"
    description: "The volumetric dataset for which the image should be created"
    url: "https://raw.githubusercontent.com/topology-tool-kit/ttk-data/dev/ctBones.vti"
    path:
```

#### Execution Script ####
Each visualization comes with an execution script that uses the information from the yaml meta data file and the information given in the template wizard when downloading an example to execute.
For this, variables are inserted into the script after configuration. 
These are used to check for the existence of the data set, determining additional execution commands and executing inside the specified container.

```bash
#!/bin/bash
# VARIABLES are added here automatically

set -e

# check for the existence of data and use default when none found
mkdir -p data
mkdir -p output
if ! test -f "${DATASET_VOLUME_PATH}"; then
    echo "data set '${DATASET_VOLUME_PATH}' not found - using default"
    DATASET_VOLUME_PATH="./data/ctBones.vti"
    if ! test -f "${DATASET_VOLUME_PATH}"; then 
	    cd data
	    wget "${DATASET_VOLUME_URL}"
	    cd ..
    fi;
fi;

# determine additional execution commands for slurm and mpi
EXEC=""
case "${EXEC_TYPE}" in
    mpi)
        EXEC="mpirun --allow-run-as-root"
        ;;

    slurm)
        EXEC="srun -n 2 --time=2"
        ;;
esac

# assemble run command for docker
if [[ "${CONTAINER_PLATFORM}" == "docker" ]]; then
    docker run --rm -v .:/example -w /example "${CONTAINER_URL}" ${EXEC} ${COMMAND} "${DATASET_VOLUME_PATH}"
fi;

# assemble run command for singularity
if [[ "${CONTAINER_PLATFORM}" == "singularity" ]]; then
    singularity pull --force container.sif "docker://${CONTAINER_URL}"
    ${EXEC} singularity run --containall  -H "${PWD}:/example" container.sif  ${COMMAND} "${DATASET_VOLUME_PATH}"
fi;
```

### Containers ###

DaVE tries to be compatible with many different container images. Any Docker container can theoretically be used. Singularity/Apptainer is used to convert Docker images into Singularity images. Singularity/Apptainer is often used in HPC environments where users have less permissions.
Each example references a Docker image with which it can be executed. Additionally, it also provides the build recipe for the image - a dockerfile. 
This can be used to extend existing images for new examples, but is not needed for executing the example.

For easier maintainability and extensibility, the provided docker image uses [spack](https://spack.readthedocs.io/en/latest/) to manage required software and its dependencies. Spack is a package manager designed for HPC. To create your own container for an example, either build upon an existing docker container by using the one of the reference example as a base or change or add packages via spack in the original dockerfile.

Currently, most examples make heavy use of the [ParaView](https://www.paraview.org/) software, which is commonly used for the visualization of scientific datasets. ParaView and its dependencies were installed using spack.

## Creating Examples ##
Changing examples or creating your own in DaVE can be done at varying levels of complexity. Either way an example can be easely created using the [this](/resources/example_template.zip) template.

### Using Custom Data ###

If you find an example fitting your visualization needs but want to use your own data, you can simply change the path to the data in the execution script. Afterwards it might be necessary to change some things in the visualization. In the case of visualizations with ParaView, you can edit the accompanying trace file. Lines where changes are potentially needed are marked with a comment containing ```# OWN_DATA``` and a short description of what needs to be adapted.

For example, you download the volume rendering example but want to use on of the time steps of the viscous fingers data set from the SciVisContest 2016. You download the data set, place it in the data directory of the example and configured the correct file name in the template wizard or change it directly inside the execution script. The necessary changes to the trace file are exemplified below.

```python
# create a new 'XML Image Data Reader'
reader = pvs.XMLImageDataReader(registrationName='reader', FileName=[filepath])
# OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name
reader.PointArrayStatus = ['Scalars_']

[...]

# OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name
pvs.ColorBy(ctBonesvtiDisplay, ('POINTS', 'Scalars_'))
```

The two important changes are the field name of the data set. The viscous finger data set has a field called "concentration" instead of "Scalars_".

```diff
# create a new 'XML Image Data Reader'
reader = pvs.XMLImageDataReader(registrationName='reader', FileName=[filepath])
-reader.PointArrayStatus = ['Scalars_']
+reader.PointArrayStatus = ['concentration'] 

[...]

-pvs.ColorBy(ctBonesvtiDisplay, ('POINTS', 'Scalars_'))
+pvs.ColorBy(ctBonesvtiDisplay, ('POINTS', 'concentration'))
```

If you want to turn this visualization with your data into an entry for DaVE, you need to copy the example folder from which your example derives, do some renaming and change the data set to your own. You have to rename the following in the visualization.yaml:

  - name
  - date
  - potentially some tags
  - url for the dataset 

Although this example should work now, the description.md should also be adapted to describe your use case with a detailed description, limitations and references for the dataset.

With everything set, you can do a pull request for your example to [DaVE](https://github.com/VRGroupRWTH/DaVE).

### Changing Existing Visualizations ###

If you want to adapt the visualization itself, you can change the visualization trace itself, at least for the ParaView examples. Let us exemplify this by adding a filter that extracts a subset of your data to the pipeline. 

Using the example of the volume rendering pipeline again, we add a subset extraction filter to the pipeline.

```diff
# create a new 'XML Image Data Reader'
reader = pvs.XMLImageDataReader(registrationName='reader', FileName=[filepath])
# OWN_DATA: every field has a name in a .vti file. Replace 'Scalars_' by the corresponding name
reader.PointArrayStatus = ['Scalars_']                                          

+subset = pvs.ExtractSubset(registrationName='extractSubset', Input=reader)
+subset.VOI = [50, 100, 50, 100, 50, 100]

[...]

# show data in view
-display = pvs.Show(reader, renderView1)
+display = pvs.Show(subset, renderView1)
display.SetRepresentationType('Volume')

[...]
```

Alternatively, you can create a completely new trace with [ParaView](https://docs.paraview.org/en/latest/Tutorials/ClassroomTutorials/pythonAndBatchPvpythonAndPvbatch.html#python-batch-pvpython-and-pvbatch) and use it for your example.

Contributing a derived visualization to DaVE's repository is similarly to [using your own data](#Using_Custom_Data). When creating a completely new entry, either take a similar example and build from there or you consult the sections on the [database structure](#Database_Structure) and [visualization](#Visualizations) for creating all necessary files.

### Changing the Containerized Environment ###
If you find that you need an additional package not available in the provided container image, you can check whether this package is available in spack.
If so, you can add it to the build configuration in the Dockerfile provided with each example. Then build the docker container. For errors during the build process consult the [spack documentation](https://spack.readthedocs.io/en/latest/). In the example below, the ffmpeg package is added to the spack configuration.

```diff
[...]

# What we want to install and how we want to install it
# is specified in a manifest file (spack.yaml)
RUN mkdir /opt/spack-environment \
&&  (echo spack: \
&&   echo '  # add package specs to the `specs` list' \
-&&   echo '  specs: [paraview+mpi+osmesa+python~qt ^mesa+osmesa+llvm ^llvm~clang~lld~gold ^openmpi+legacylaunchers+pmi+thread_multiple fabrics=ucx schedulers=slurm]' \
+&&   echo '  specs: [ffmpeg, paraview+mpi+osmesa+python~qt ^mesa+osmesa+llvm ^llvm~clang~lld~gold ^openmpi+legacylaunchers+pmi+thread_multiple fabrics=ucx schedulers=slurm]' \
&&   echo '  view: /opt/views/view' \
&&   echo '  concretizer:' \
&&   echo '    unify: true' \
&&   echo '  config:' \
&&   echo '    install_tree: /opt/software') > /opt/spack-environment/spack.yaml

[...]
```

After the desired changes build the container with 

```
docker buildx build -t <your/container/name> -f Dockerfile --target build .
```

Changes to the container can be done in addition to changes in data and/or visualization. When using a new container only the uri in the visualization.yaml has to be changed and the new Dockerfile should be added as a resource in the respective directory. Ideally those changes are combined such that the newly added capabilities in your container are used by the visualization.

### Using a Custom Environment ###
If none of the above works for you or you already have a working docker container and just want to make your use case available, you can provide your own docker container in the visualization.yaml.

## Feature Requests ##
If you have an idea how to improve the DaVE website or any other aspect of DaVE, you are welcome to create a feature request in the DaVE repository on GitHub using this <a href="https://github.com/VRGroupRWTH/DaVE/issues/new?title=Feature Request&body=Please describe the feature that you are requesting as detailed as possible and change the name of the ticket accordingly. If you like, you can also assign labels to your feature request.">link</a>.
Make sure that you properly describe your idea.
We will then review your request, give feedback and if possible implement your feature as quickly as possible.