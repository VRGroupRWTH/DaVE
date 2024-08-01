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
<a class="mx-auto mx-md-5 my-5 float-md-end d-block" style="width: 250px" href="https://ieeevis.org/year/2024/welcome">
    <img class="w-100 shadow" src="/images/about_paper.png">
</a>

The short paper that was published along with the release of DaVE gives further insight into the motivation that led to the development of DaVE and the development process itself.
The paper also presents the results of a user study that was conducted to evaluate the usability of DaVE.

Prior to the development of DaVE, a survey was conducted within the NHR community which revealed that many researchers are either unfamiliar with the latest visualisation techniques or lack the needed resources and time to apply these techniques, particularly when using HPC infrastructure.
This lack of resources was the impetus for the development of DaVE.
Three aspects in particular were taken into account during the development: DaVE should be tailored to users who are not experts in the field of visualisation, the resources provided by DaVE should allow for an easy deployment of visualisation techniques on existing HPC infrastructure, and DaVE should be easily extensible by the scientific community.

Easy access to resources for non-experts was achieved by implementing DaVE as a website, where not only a database of visualisation examples can be intuitively explored, but also resources tailored to a specific use case can be quickly found through the use of tags.
For each example listed in DaVE, a template is provided that includes all the necessary resources to run the visualisation example not only locally but also on a cluster.
Finally, the extensibility of DaVE has been ensured by organising the source code and database in a GitHub repository, which allows users to contribute via pull requests.

During the user study conducted at the end of development, five simulation scientists were asked to test the website by exploring the examples and resources available.
Comments made by the participants during the exploration were noted and each participant was asked to complete a questionnaire at the end of the session.
Overall, DaVE received positive feedback from the participants.

#### BibTeX ####
``` tex
@inproceedings{DaVE2024,
  author       = {Koenen, Jens and Petersen, Marvin and Garth, Christoph and Gerrits, Tim},
  booktitle    = {2024 IEEE Visualization and Visual Analytics (VIS)},
  publisher    = {IEEE Computer Society},
  title        = {{DaVE - A Curated Database of Visualization Examples}},
  year         = {2024}
}
```

## DaVE Team ##
In case you have a general question about DaVE and **don't** just want to report a bug or request a feature, please contact one of the following members of the DaVE team: