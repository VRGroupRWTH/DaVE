
<p align=center>
  <img src="/website/public/images/logo.svg" width="60%">
</p>

Welcome to DaVE - the Database of Visualization Examples.
The goal of DaVE is simple: empower users, especially working with High Performance Computing (HPC) infrastructure, with easy access to advanced and state-of-the-art visualization techniques.
We understand that many face a lack of time or resources to explore and integrate new techniques.
However, most also know about the benefits and seek to enhance their simulations with effective visualizations to explore, analyze, or present their data.

DaVE serves as a centralized repository where users can find and discover visualization examples tailored to their specific needs through a simple search.
Our database is designed to be user-friendly, offering seamless integration into existing workflows using adaptable containers.
Whether you're exploring cutting-edge visualizations for data or seeking practical solutions to enhance your simulations, DaVE seeks to find helpful resources for you.

And the best part: DaVE is designed to keep growing!
Everybody can join our mission and add more examples and resources.

## Development ###
After cloning or downloading the repository, open the cloned directory in Visual Studio Code with the Dev Containers extension installed.
Before using the Dev Container extension, it is neccessary to install Docker.
More information on that can be found on the extension page in VS Code.
Following that, reopen the directory in the container by pressing `F1` and entering `reopen in container` in the command box that opens at the top of the editor.
When the container was fully loaded by Visual Studio Code, open a terminal and type the following command to download and initalize the dependencies of the website
```
npm install
```

If you want a development version where you can easily make changes to the website, use the following command.
```
npm run dev
```
On the other hand, if you want a production version of the website use the following command to build and pack the website.
```
npm run prod
```
In both cases, there should appear the text `Listening on port 8080` in the terminal and you should be able to access the website by visiting `http://localhost:8080/`.

## Deployment ##
The DaVE website can be deployed easily with the help of Docker and the provided Dockerfile.
First, a Docker image has to be created by running the following command in the terminal
```
docker build . -t dave
```
After that the Docker image and the website in it can be started using the following terminal command
```
docker run -p 127.0.0.1:8080:8080 -v .:/dave -w /dave dave bin/bash -c "npm install && npm run prod"
```
Finally, there should appear a text saying `Listening on port 8080` and you should be able to access the website by visiting `http://localhost:8080/`.