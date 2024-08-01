&nbsp;
<p align=center>
  <img src="/website/public/images/home_logo_small.svg" width="350">
</p>
&nbsp;

Welcome to DaVE - the Database of Visualization Examples.
The goal of DaVE is simple: empower users, especially working with High Performance Computing (HPC) infrastructure, with easy access to advanced and state-of-the-art visualization techniques.
We understand that many face a lack of time or resources to explore and integrate new techniques.
However, most also know about the benefits and seek to enhance their simulations with effective visualizations to explore, analyze, or present their data.

DaVE serves as a centralized repository where users can find and discover visualization examples tailored to their specific needs through a simple search.
Our database is designed to be user-friendly, offering seamless integration into existing workflows using adaptable containers.
Whether you're exploring cutting-edge visualizations for data or seeking practical solutions to enhance your simulations, DaVE seeks to find helpful resources for you.

And the best part: DaVE is designed to keep growing!
Everybody can join our mission and add more examples and resources.

## Contribution Process ##
If you would like to contribute, for example by adding an example to the database, you need a GitHub account and a basic understanding of `git`.
In case you haven't worked with `git` before or just need a refresher, watch one of the many beginner guides on the internet to get a rough understanding of how `git` works.

After logging into your GitHub account, navigate to the website of the DaVE repository on GitHub and create a fork of the repository by pressing the respective button in the upper right half of the website.
Give the fork a name of your choice, and make sure that the work includes only the `main` branch of the DaVE repository.
The fork that GitHub will then create for you is a repository that belongs only to you and contains the current state of the DaVE repository.
Every change that you want to make has to be applied first to your fork repository before it can be integrated into the original DaVE repository.

As with any other repository, create a local copy of the fork repository by cloning it, and then make changes to this local copy of the repository.
If you are finished and satisfied with your changes, create a commit and push your modifications to the `main` branch of your fork repository.
After that, you need to again navigate to the DaVE repository on GitHub where you then have to create a pull request for your changes.
Select the main branch of the original DaVE repository as well as your fork repository, and briefly describe the changes you made.
We will then review what you have done before we accept the pull request and make your changes official.

It is important to keep in mind that DaVE is a database for examples, descriptions and source code and **not** for datasets.
Therefore, please try to keep your examples as small as possible by, for example not directly including datasets in your examples.
Instead, use publicly available datasets, for example hosted on [Zenodo](https://zenodo.org/), and include them using an `url`.
Pull requests larger than 100 MB will be declined to limit the size of the repository.

## Development ##
After cloning or downloading the repository, open the cloned directory in Visual Studio Code with the Dev Containers extension installed.
Before using the Dev Container extension, it is necessary to install Docker.
More information on that can be found on the extension page in VS Code.
Following that, reopen the directory in the container by pressing `F1` and entering `reopen in container` in the command box that opens at the top of the editor.
When the container is fully loaded by Visual Studio Code, open a terminal and type the following command to download and initialize the dependencies of the website:
```
npm install
```

If you want a development version where you can easily make changes to the website, use the following command:
```
npm run dev
```
On the other hand, if you want a production version of the website, use the following command to build and pack the website:
```
npm run prod
```
In both cases, the message `Listening on port 8080` should appear in the terminal, and you should be able to access the website by visiting `http://localhost:8080/`.

## Deployment ##
DaVE can be deployed easily with the help of Docker and the provided Dockerfiles using the following command:
```
docker compose up
```
After building the Dockerfile and starting the web server, the message `Listening on port 8080` should appear in the terminal, and you should be able to access the website by visiting `http://localhost:8080/`.
