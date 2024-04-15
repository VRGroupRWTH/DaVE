<div id="whatisdave" outline_label="What is DaVE?" outline_indent="0"  markdown="1">

## What is DaVE? ##

DaVE is an explorable visualization database providing detailed visualization examples with containerized environments for easy execution and extensibility on HPC platforms for non-visualization experts.

<!-- Besides of giving an overview over different vizualization techniques and providing addtional information, the goal of DaVE is also to make every technique accessible to users.
However, this can be quite challenging as different users may use different software environments meaning that the environment in which a visualization technique should be executed is not always known.
DaVE therefore heavily relies on the use of containers with which the software for the visualization technique can be encapsulated.
The container as well as additonal resources of a vizualization technique can be downloaded separately.
However, there is also the option to create a template that combines all resources of a techniuqe and that is condifured for a specific use case. -->

</div>
<div id="howtouseDave" outline_label="How to Use DaVE?" outline_indent="0"  markdown="1">

## How to Use DaVE? ##

<div id="preliminaries" outline_label="Preliminaries" outline_indent="1" markdown="1">

#### Preliminaries ####

If you plan to execute any of the examples provided in DaVE, you either need a recent Docker or Singularity/Apptainer version installed on the machine you plan to run on. Further, you need to be able to execute shell scripts.
- Information on Docker can be found here [https://docs.docker.com/get-started/overview/](https://docs.docker.com/get-started/overview/)
- Information on Apptainer can be found here [https://apptainer.org/docs/user/latest/](https://apptainer.org/docs/user/latest/) and its compatability with singularity is described here [https://apptainer.org/docs/user/main/singularity_compatibility.html](https://apptainer.org/docs/user/main/singularity_compatibility.html)

</div>
<div id="browsing" outline_label="Finding Examples" outline_indent="1" markdown="1">

#### Finding Examples ####

The browser offers a gallery view of all the examples available in DaVE. Each thumbnail was produced by the underlying example. You can filter the examples by entering search terms in the search mask or specifying [tags](#tags). Tags can also be selected by clicking the tag annotation below the title of each example. Additionally, you can filter by the date when the example was added.

When clicking on one of the examples in the gallery view, you are redirected to a page containing more information on that example. If available, additional images can be cycled through at the top and an interactive preview of the visualizaiton can be explored.
Below are descriptions of the visualization methods and its application with references for further reading.

</div>
<div id="browsing" outline_label="Executing Examples" outline_indent="1" markdown="1">

#### Executing Examples ####

In order to execute each of the examples yourself, DaVE provides instructions for this purpose with example specific descriptions of optional changes if you wish to customize it.

To download an example ready for execution click on the download button in the top left corner. In order to prepare the example for your purpose you need to select the data, the environment and container technology to use. If in doubt, leave the default values and select the locally installed container platform. After selecting the options the [template](#templates) .zip file will be prepared. Everything you need to do afterwards is described in the instructions of that example. Generally, this boils down to extracting the .zip and executing the shell script inside.

</div>
<div id="architecture" outline_label="DaVE's Architecture" outline_indent="0" markdown="1">

## DaVE's Architecture ##

<div id="database" outline_label="Database" outline_indent="1" markdown="1">

#### Database ####

The database of DaVE contains a selection of commonly used visualization techniques and provides documentation and addtional resources for them. Each entry comes with an easy-to-use, easy-to-extend example that can be downloaded and executed on your local hardware or on HPC clusters with slurm and MPI, provided slurm and singularity/apptainer (or docker) are available.

##### Database Structure #####

DaVE's database is a simple file hierarchy, where each entry is represented by a directory. Each example contains further subdirectories. The _images_ folder stores all images to show in the gallery view and the example page. The _scene_ folder contains information for the interactive preview that some examples provide. The _resources_ directory contains all necessary files for executing this example. In general, this entails a shell script for execution and in the case of [ParaView](https://www.paraview.org/) visualizations, a Python trace file. The description markdown file contains all the text describing the visualization, its appllication, providing additional references and instructions for executing and adapting the example. The [visualization.yaml](#visualization-metadata) contains all the information about the tags, which container image to use, which images to show etc..

```
database/
├─ example/
│  ├─ images/
│  ├─ resources/
│  ├─ scene/
│  ├─ description.md
│  ├─ visualization.yaml
```

</div>
<div id="visualizations" outline_label="Visualizations" outline_indent="1" markdown="1">

#### Visualizations ####

DaVE tries to cover a wide range of visualization methods from different applications.
Additionally, the provided examples should be executable on a diverse set of computing resources. In order to categorize and organize each of the example visualizations the meta data for each example is stored in a yaml file.

##### Visualization Metadata #####

```
name: "<Name of the example>"
date: 1900-01-01
```
```
tags:
- name: "Name of technique related tag"
  type: "technique"
- name: "Name of domain related tag"
  type: "domain"
  abbreviation: "Abbreviation of tag name"
```
```
images:
- "images/name of image"
```
```
scene: "scene/index.json"
```
```
resources:
- name: "isocontour_trace.py"
  type: "Script"
  date: 2024-01-09
  path: "resources/isocontour_trace.py"
- name: "ParaView 5.11.1"
  type: "Container"
  date: 2024-01-09
  url: "ghcr.io/scivislab/paraview:5.11.1"
- name: "ctBones.vti"
  type: "Dataset"
  date: 2024-01-09
  url: "https://raw.githubusercontent.com/topology-tool-kit/ttk-data/dev/ctBones.vti"
```
```
templates:
- techniques:
    - "docker"
    - "singularity"
commands:
    - type: "local"
      run: "pvbatch isocontour_trace.py"
    - type: "mpi"
      run: "pvbatch isocontour_trace.py"
    - type: "slurm"
      run: "pvbatch isocontour_trace.py"
trace: "resources/isocontour_trace.py"
script: "resources/isocontour_script.sh"
container:
    url: "ghcr.io/scivislab/paraview:5.11.1"
```
```
datasets:
- name: "Volume"
  identifier: "DATASET_VOLUME"
  description: "The volumetric dataset for which the image should be created"
  url: "https://raw.githubusercontent.com/topology-tool-kit/ttk-data/dev/ctBones.vti"
```

</div>
<div id="tags" outline_label="Tags" outline_indent="1" markdown="1">

#### Tags ####

Searching visualization techniques with a search query alone would be far too general, as there are often many techniques that would match the query but have totally different properties.
To make the search function of DaVE more specific, every technique in the database owns a set of tags that are used to further describe the properties of a visualization technique.

<div class="d-flex justify-content-center">
    <figure class="figure">
        <img class="figure-img img-flud" src="/images/dave_guide_tags.svg" style="width: 100%; max-width: 400px;">
        <figcaption class="figure-caption">Tags used by DaVE to further describe visualizations.</figcaption>
    </figure>
</div>

For example, a technique with the tag <span class="mx-1 badge text-primary-emphasis bg-primary-subtle border-primary-subtle px-2 py-1">Scalar</span> would be suitable for datasets consisting of real-valued samples, e.g. a dataset describing the temperature within a room.
The tags that are used throughout the database are divided into two groups.
Blue tags are used to identify **technical properties** such as the domain for which a visualization can be used or whether the technique can be used for time-dependent datasets.
On the other hand, green tags are used to identify the **scientific domain** for which a technique is particularly suitable or where the data of the example visualization came from.
</div>
<div id="templates" outline_label="Templates" outline_indent="1" markdown="1">

#### Templates ####

A template combines all neccessary resources for a visualization technique that are needed to render an image for a given dataset.
If required, the template also contains or downloads a preview dataset with which the technique can be tested.
The shell script that is always included in the template zip file of the template controlls and automates the execution of the vizualization technique.
When running the script, it loads a docker container, depending on the configuration of the template ether with docker or singularity.

<div class="d-flex justify-content-center">
    <figure class="figure">
        <img class="figure-img img-flud" src="/images/dave_guide_template.svg"style="width: 100%; max-width: 400px;">
        <figcaption class="figure-caption">Tags used by DaVE to further describe visualizations.</figcaption>
    </figure>
</div>

The container that is currently used for most of the visualization techniques, contains ParaView which is a software commonly used for scientific visualizations and data exploration.
The script calls the ParaView instance in the container and ParaView is instructed to load a trace file which describes the visualization technique itself and all the steps that ParaView has to take to apply the visualization on the given dataset.
ParaView then loads the dataset and renders it according to the trace File.
The resulting image is then stored in the same directory in which the script file is located.
Currently the script as well as the containers only run under linux based operating systems.
</div>
<div id="containers" outline_label="Containers" outline_indent="1" markdown="1">

#### Containers ####

DaVE tries to be compatbile with many different container images. Any Docker container can theoretically be used. Singularity/Apptainer is used to convert Docker images into Singularity images
that require less permissions. Singularity/Apptainer is often used in HPC environments where users have no root access.
Each example references a Docker image with which it can be executed. Additionally, it also provides the build recipe for the image - a dockerfile. 
This can be used to extend existing images for new examples, but is not needed for executing the example.

For easier maintainability and extensibility, the provided docker image uses [spack](https://spack.readthedocs.io/en/latest/) to manage required software and its dependencies. Spack is a package manager designed for HPC. To create your own container for an example, either build upon an existing docker container by using the one of the reference example as a base or change or add packages via spack in the original dockerfile.

Currently, most examples make heavy use of the [ParaView](https://www.paraview.org/) software, which is commonly used for the visualization of scientific datasets. ParaView and its dependencies were installed using spack.
</div>
<div id="extenddave" outline_label="Extending DaVE" outline_indent="0" markdown="1">

## Extending DaVE ##

Changing examples or creating your own in DaVE can be done at varying levels of complexity.

<div id="customdata" outline_label="Using Custom Data" outline_indent="1" markdown="1">

#### Using Custom Data ####

If you find an example fitting your visualization needs but want to use your own data. You can simply copy the example folder, do some renaming and change the data set to your own. Renaming has to be done in the 
	visualization.yaml
		- name
		- date
		- potentially some tags (tags need a type)
		- rename the script and potentially trace file
		- change their names in the .yaml
		- change the url(s) in dataset and the description
	Although this example should work now, the dscription.md should be adapted to decribe your use case with the correct name for the script.
	Additional changes to the visualization trace for ParaView examples might be necessary. Lines where changes are potentially needed are marked with a comment containing ```# OWN_DATA``` and a short description of what needs to be adapted.
	
TODO add files with changes highlighted

</div>
<div id="changingvis" outline_label="Changing Existing Visualizations" outline_indent="1" markdown="1">

#### Changing Existing Visualizations ####

If you want to adapt the visualization itself, you can change the visualization trace itself, at least for the ParaView examples. For example you can add a filter extracting a subset of your data to the pipeline. 

TODO: add example in code

Alternatively, you can create a completely new trace with ParaView [TODO link] and use it for the exmaple.

</div>
<div id="changingenv" outline_label="Changing Containerized Environment" outline_indent="1" markdown="1">

#### Changing the Containerized Environment ####

If you find that you need an additional package not available in the provided container image, you can check whether this package is available in spack.
If so, you can add it to the build configuration in the Dockerfile provided with each example. Then build the docker container. For errors during the build process consult the spack documentation [TODO link].

TODO: add example of new Dockerfile

TODO: add build command

</div>
<div id="customenv" outline_label="Using Custom Environment" outline_indent="1" markdown="1">

#### Using a Custom Environment ####

If none of the above works for you or you already have a working docker container and just want to make your use case available, you can provide your own docker container in the .yaml.

</div>
<div id="faq" outline_label="Frequently ask Questions" outline_indent="0" markdown="1">

## Frequently ask Questions ##

The container that is currently used for most of the visualization techniques, contains ParaView which is a software commonly used for sientify visualizations and data exploration.
When loading the container, ParaView is instructed to load a trace file which describes the visualization techniuqe it self and all the steps that ParaView has to take to apply the visualization on the given dataset.
ParaView then loads the Dataset and renders it according to the Trace File.
The resulting image is then stored in the same directory in which the script file is located.
Currently the script as well as the containers only run under linux based operating systems.
</div>