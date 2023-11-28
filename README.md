# DaVE
DaVE is a curated database of visualization examples. This repository contains the website where examples can be integrated.

## Setup
To run the website locally for development purposes, follow these steps:

### VS Code + Docker
1. Clone or download the repository
2. Open the cloned directory in Visual Studio Code with the Dev Containers extension installed (this requires Docker, you can find more information on how to install Docker on the extension page in VS Code)
3. Reopen the directory in the container (press F1, then enter "reopen in container")
4. Open a terminal in VS Code and enter ``./setup.sh``
5. Start the application by entering ``node index.js``
6. There should appear a text saying "Listening on port 8080" and you should be able to see the webpage by visiting ``http://localhost:8080/``
