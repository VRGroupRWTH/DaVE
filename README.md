Welcome to DaVE - the Database of Visualization Examples.
The goal of DaVE is simple: empower users, especially working with High Performance Computing (HPC) infrastructure, with easy access to advanced and state-of-the-art visualization techniques.
We understand that many face a lack of time or resources to explore and integrate new techniques.
However, most also know about the benefits and seek to enhance their simulations with effective visualizations to explore, analyze, or present their data.

DaVE serves as a centralized repository where users can find and discover visualization examples tailored to their specific needs through a simple search.
Our database is designed to be user-friendly, offering seamless integration into existing workflows using adaptable containers.
Whether you're exploring cutting-edge visualizations for data or seeking practical solutions to enhance your simulations, DaVE seeks to find helpful resources for you.

And the best part: DaVE is designed to keep growing!
Everybody can join our mission and add more examples and resources.



```
docker build . -t dave
```

```
docker run -p 127.0.0.1:8080:8080 dave npm run prod
```

```
npm install
npm run dev #For development
npm run prod #For production
```

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
