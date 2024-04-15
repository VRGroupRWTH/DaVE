<script>
    import { ref } from "vue";
    import GlobalHeader from "../components/global_header.vue";
    import GlobalFooter from "../components/global_footer.vue";
    import Outline from "../components/outline.vue";

    export default
    {
        components:
        {
            "shared-header": GlobalHeader,
            "shared-footer": GlobalFooter,
            "outline": Outline
        },
        setup()
        {
            let content = ref(null);

            return {
                content
            }
        }
    };
</script>

<template>
    <header class="sticky-top">
        <shared-header>
            <h5 class="pt-3 pb-1">On this page</h5>
            <outline :target="content"></outline>
        </shared-header>
    </header>
    <main>
        <div class="container d-flex">
            <div ref="content" class="guide-content me-lg-4">
                <h1 class="display-2 ps-2 py-5 mb-4" style="font-weight: 350;">Guide</h1>
                <div id="database" outline_label="Database" outline_indent="0">
                    <h3>Database</h3>
                    <p>
                        The database of DaVE contains selection of commonly used visualization techniques and provides documentation and addtional resources for them.
                        To find a visualization, either a search term can be used and or tags can be used to further narrow down the selection.
                    </p>
                </div>
                <div id="tags" outline_label="Tags" outline_indent="0">
                    <h3>Tags</h3>
                    <p>
                        Searching visualization techniques with a search query alone would be far too general, as there are often many techniques that would match the query but have totally different properties.
                        To make the search function of DaVE more specific, every technique in the database owns a set of tags that are used to further describe the properties of a visualization technique.
                    </p>
                    <div class="d-flex justify-content-center">
                        <figure class="figure">
                            <img class="figure-img img-flud" src="/images/dave_guide_tags.svg" style="width: 100%; max-width: 400px;">
                            <figcaption class="figure-caption">Tags used by DaVE to further describe visualizations.</figcaption>
                        </figure>
                    </div>
                    <p>
                        For example, a technique with the tag <span class="mx-1 badge text-primary-emphasis bg-primary-subtle border-primary-subtle px-2 py-1">Scalar</span> would be suitable for datasets consisting of real-valued samples, e.g. a dataset describing the temperature within a room.
                        The tags that are used throughout the database are divided into two groups.
                        Blue tags are used to identify technical properties such as the domain for which a visualization can be used or whether the technique can be used for time-dependent datasets.
                        On the other hand, green tags are used to identify the scientific domain for which a technique is particularly suitable.
                    </p>
                </div>
                <div id="visualizations" outline_label="Visualizations" outline_indent="0">
                    <h3>Visualizations</h3>
                    <p>
                        Besides of giving an overview over different vizualization techniuqes and providing addtional information, the goal of DaVE is also to make every technique accessible to users.
                        However, this can be quite challanging as different uesers may use different software environments meaning that the environment in which a vizualization technique should be executed is not always known.
                        DaVE therefore havily relies on the use of containers with which the software for the viszualization technique can be encapsulated.
                        The container as well as additonal resources of a vizualization technique can be downloaded separately.
                        However, there is also the option to create a template that combines al resources of a techniuqe and that is condifured for a specific use case.
                    </p>
                </div>
                <div id="templates" outline_label="Templates" outline_indent="0">
                    <h3>Templates</h3>
                    <p>
                        A template combines all neccessary resources for a visualization technique that are needed to render an image for a given dataset.
                        If required, the template also contains a preview dataset with which the technique can be tested.
                        The shell script that is always included in the template zip file of the template controlls and automates the execution of the vizualization technique.
                        When running the script, it loads a docker container, depending on the configuration of the template ether with docker or singularity.
                    </p>
                    <div class="d-flex justify-content-center">
                        <figure class="figure">
                            <img class="figure-img img-flud" src="/images/dave_guide_template.svg"style="width: 100%; max-width: 400px;">
                            <figcaption class="figure-caption">Tags used by DaVE to further describe visualizations.</figcaption>
                        </figure>
                    </div>
                    <p>
                        The container that is currently used for most of the visualization techniques, contains ParaView which is a software commonly used for scientific visualizations and data exploration.
                        The script calls the ParaView instance in the container and ParaView is instructed to load a trace file which describes the visualization technique itself and all the steps that ParaView has to take to apply the visualization on the given dataset.
                        ParaView then loads the dataset and renders it according to the trace File.
                        The resulting image is then stored in the same directory in which the script file is located.
                        Currently the script as well as the containers only run under linux based operating systems.
                    </p>
                </div>
                <div id="containers" outline_label="Containers" outline_indent="0">
                    <h3>Containers</h3>
                    <p>
                        DaVE tries to provide to different types of containers. Any Docker container can theoretically be used. Singularity is used to convert Docker images into Singularity images
                        that require less permissions. Singularity/Apptainer is often used in HPC environments where users have no root access.
                        Each example references a Docker image with which it can be executed. Additionally, it also provides the build recipe for the image - a dockerfile. 
                        This can be used to extend existing images for new examples, but is not needed for executing the example.

                        The main provided docker image uses spack to manage required software and its dependencies. Spack is a package manager designed with HPC in mind. 
                        To create your own container for an example, either build upon an existing docker container bz using the one of the reference example as a base or
                        change or add packages via spack in the original dockerfile.
                    </p>
                </div>
                <div id="paraview" outline_label="ParaView" outline_indent="0">
                    <h3>ParaView</h3>
                    <p>
                        <a href="https://www.paraview.org/">ParaView</a> is software commonly use for the visualization of scientific datasets.
                    </p>
                </div>
                <div id="faq" outline_label="Frequently ask Questions" outline_indent="0">
                    <h3>Frequently ask Questions</h3>
                    <p>
                        The container that is currently used for most of the visualization techniques, contains ParaView which is a software commonly used for sientify visualizations and data exploration.
                        When loading the container, ParaView is instructed to load a trace file which describes the visualization techniuqe it self and all the steps that ParaView has to take to apply the visualization on the given dataset.
                        ParaView then loads the Dataset and renders it according to the Trace File.
                        The resulting image is then stored in the same directory in which the script file is located.
                        Currently the script as well as the containers only run under linux based operating systems.
                    </p>
                </div>
                <div id="extending_dave" outline_label="Extending DaVE" outline_indent="0">
                    <h3>Extending DaVE</h3>
                    <p>
                        
                    </p>
                    <h5>Database Structure</h5>
                    <p>
                        hallo welt
                    </p>
<pre>
database/
├─ example/
│  ├─ images/
│  ├─ resources/
│  ├─ scene/
│  ├─ visualization.yaml
│  ├─ description.md
</pre>
                    <h5>Visualization Metadata</h5>
                    <p>
                        hallo welt
                    </p>
<pre>
name: "&lt;Name of the example&gt;"
date: 1900-01-01
</pre>
<pre>
tags:
- name: "Name of technique related tag"
type: "technique"
- name: "Name of domain related tag"
type: "domain"
abbreviation: "Abbreviation of tag name"
</pre>
<pre>
images:
- "images/name of image"
</pre>
<pre>
scene: "scene/index.json"
</pre>
<pre>
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
</pre>
<pre>
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
</pre>
<pre>
datasets:
- name: "Volume"
identifier: "DATASET_VOLUME"
description: "The volumetric dataset for which the image should be created"
url: "https://raw.githubusercontent.com/topology-tool-kit/ttk-data/dev/ctBones.vti"
</pre>

                </div>
            </div>
            <div class="flex-shrink-0 d-none d-lg-block" style="width: 250px;">
                <div class="sticky-top" style="top: 100px; z-index: 0;">
                    <h5 class="about-content pt-3 pb-1">On this page</h5>
                    <outline :target="content"></outline>
                </div>
            </div>
        </div>
    </main>
    <footer class="bg-body-tertiary">
        <shared-footer class="container"></shared-footer>
    </footer>
</template>