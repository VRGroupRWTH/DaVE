## What is DaVE? ##
DaVE is a Database of Visualization Examples.
The goal of DaVE is simple: empower users, especially working with High Performance Computing (HPC) infrastructure, with easy access to advanced and state-of-the-art visualization techniques.
We understand that many face a lack of time or resources to explore and integrate new techniques.
However, most also know about the benefits and seek to enhance their simulations with effective visualizations to explore, analyze, or present their data.

DaVE serves as a centralized repository where users can find and discover visualization examples tailored to their specific needs through a simple search.
Our database is designed to be user-friendly, offering seamless integration into existing workflows using adaptable containers.
Whether you're exploring cutting-edge visualizations for data or seeking practical solutions to enhance your simulations, DaVE seeks to find helpful resources for you.

And the best part: DaVE is designed to keep growing!
Everybody can join our mission and [add](/guide_extend_dave) more examples and resources.

## DaVE Paper ##
<a class="mx-auto mx-md-5 my-5 float-md-end d-block" style="width: 250px" href="http://arxiv.org/abs/2408.03188">
    <img class="w-100 shadow" src="/images/about_paper.png">
</a>

We describe our motivation and realization of DaVE within a short paper that was accepted for presentation at the [2024 IEEE VIS conference](https://ieeevis.org). 
It also presents the results of an expert user study that was conducted to evaluate the usability of DaVE.

[NHR](https://www.nhr-verein.de) is a large national research project in Germany that aims to improve research infrastructure using high performance computing. Within NHR, a [survey](https://zenodo.org/records/7715663) was conducted which revealed that many researchers are either unfamiliar with the latest visualization techniques or lack the needed resources and time to apply these techniques, particularly when using HPC infrastructure.
This lack of resources was the impetus for the development of DaVE.
Three aspects in particular were taken into account during the development: DaVE should be tailored to users who are not experts in the field of visualization, the resources provided by DaVE should allow for an easy deployment of visualization techniques on existing HPC infrastructure, and DaVE should be easily extensible by the scientific community.

Easy access to resources for non-experts was achieved by implementing DaVE as a website, where not only a database of visualization examples can be intuitively explored, but also resources tailored to a specific use case can be quickly found through the use of tags.
For each example listed in DaVE, a template is provided that includes all the necessary resources to run the visualization example not only locally but also on a cluster.
Finally, the extensibility of DaVE has been ensured by organising the source code and database in a GitHub repository, which allows users to contribute via pull requests.

During the user study conducted at the end of development, five simulation scientists were asked to test the website by exploring the examples and resources available.
Comments made by the participants during the exploration were noted and each participant was asked to complete a questionnaire at the end of the session.
Overall, DaVE received positive feedback from the participants.

#### Preliminary BibTeX ####
``` tex
@inproceedings{dave2024,
  author={Koenen, Jens and Petersen, Marvin and Garth, Christoph and Gerrits, Tim},
  booktitle={2024 IEEE Visualization and Visual Analytics (VIS)}, 
  title={DaVE - A Curated Database of Visualization Examples}, 
  year={2024},
  month={Oct},
  volume={},
  number={},
  pages={11-15},
  keywords={Codes;Visual analytics;High performance computing;Data visualization;Containers;Visual databases;Visualization;Curated Database;High-Performance Computing},
  doi={10.1109/VIS55277.2024.00010},
  ISSN={2771-9553}
}
```

## DaVE Team ##
In case you have a general question about DaVE and **don't** just want to report a bug or request a feature, please contact one of the following members of the DaVE team: