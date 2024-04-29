### Preliminaries ###
If you plan to execute any of the examples provided in DaVE, you either need a recent Docker or Singularity/Apptainer version installed on the machine you plan to run on. Further, you need to be able to execute shell scripts.
- Information on Docker can be found [here](https://docs.docker.com/get-started/overview/)
- Information on Apptainer can be found [here](https://apptainer.org/docs/user/latest/) and its compatibility with singularity is described [here](https://apptainer.org/docs/user/main/singularity_compatibility.html)

### Finding Examples ###
The browser offers a gallery view of all the examples available in DaVE. Each thumbnail was produced by the underlying example. You can filter the examples by entering search terms in the search mask or by specifying [tags](#Tags). Tags can also be selected by clicking the tag annotation below the title of each example. Additionally, you can filter by the date when the example was added.

When clicking on one of the examples in the gallery view, you are redirected to a page containing more information on that example. If available, additional images can be cycled through at the top and an interactive preview of the visualization can be explored.
Below are descriptions of the visualization methods and its application with references for further reading.

### Tags ###
Searching visualization techniques with a search query alone would be far too general, as there are often many techniques that would match the query but have totally different properties.
To make the search function of DaVE more specific, every technique in the database owns a set of tags that are used to further describe the properties of a visualization technique.

<div class="d-flex justify-content-center">
    <figure class="figure">
        <img class="figure-img img-flud" src="/images/dave_guide_tags.svg" style="width: 100%; max-width: 800px;">
        <figcaption class="figure-caption text-center">Tags used by DaVE to further describe visualizations.</figcaption>
    </figure>
</div>

For example, a technique with the tag *Scalar* would be suitable for datasets consisting of real-valued samples, e.g. a dataset describing the temperature within a room.
The tags that are used throughout the database are divided into three groups.
Blue tags are used to identify **dataset properties** such as if the visualization is commonly used with three-dimensional dataset, scalar dataset or if the technique can be used for time-dependent datasets.
Red tags are used to identify **technique properies** such as if the technique uses lines or glyphs to illustrate the dataset.
Green tags are used to identify the **scientific domain** for which a technique is particularly suitable or where the data of the example visualization came from.

### Executing Examples ###
In order to execute each of the examples yourself, DaVE provides instructions for this purpose with example specific descriptions of optional changes if you wish to customize it.

To download an example ready for execution click on the download button in the top left corner. In order to prepare the example for your purpose you need to select the data, the environment and container technology to use. If in doubt, leave the default values and select the locally installed container platform. After selecting the options the [template](#Templates) .zip file will be prepared. Everything you need to do afterwards is described in the instructions of that example. Generally, this boils down to extracting the .zip and executing the shell script inside.

### Templates ###
A template combines all necessary resources for a visualization technique that are needed to render an image for a given dataset.
If required, the template also contains or downloads a preview dataset with which the technique can be tested.
The shell script that is always included in the template zip file of the template controls and automates the execution of the visualization technique.
When running the script, it loads a docker container, depending on the configuration of the template ether with docker or singularity.

<div class="d-flex justify-content-center">
    <figure class="figure">
        <img class="figure-img img-flud" src="/images/dave_guide_template.svg" style="width: 100%; max-width: 400px;">
        <figcaption class="figure-caption text-center">Pipeline used by a template.</figcaption>
    </figure>
</div>

The container that is currently used for most of the visualization techniques, contains ParaView which is a software commonly used for scientific visualizations and data exploration.
The script calls the ParaView instance in the container and ParaView is instructed to load a trace file which describes the visualization technique itself and all the steps that ParaView has to take to apply the visualization on the given dataset.
ParaView then loads the dataset and renders it according to the trace File.
The resulting image is then stored in the same directory in which the script file is located.
Currently the script as well as the containers only run under linux based operating systems.