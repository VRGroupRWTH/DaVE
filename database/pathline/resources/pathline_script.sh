#!/bin/bash

set -e

# check for the existence of data and use default when none found
mkdir -p dataset
mkdir -p output
if ! test -d "${DATASET}"; then
    echo "data set '${DATASET}' not found - using default"
    if test -f 'dataset/jet4.zip'; then
        mkdir -p dataset/jet4/
        unzip -n -qq dataset/jet4.zip -d dataset/jet4/
        DATASET="./dataset/jet4/"
    else
        echo "default data set not found - aborting"
        exit 0
    fi
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
    docker run --rm -v .:/example -w /example "${CONTAINER_URL}" ${EXEC} ${COMMAND} "${DATASET}"
fi;

# assemble run command for singularity
if [[ "${CONTAINER_PLATFORM}" == "singularity" ]]; then
    ${EXEC} singularity run -H "${PWD}:/example" "docker://${CONTAINER_URL}" ${COMMAND} "${DATASET}"
fi;

if command -v ffmpeg &> /dev/null
then
    ffmpeg -hide_banner -loglevel error -y -framerate 10 -i output/pathline.%04d.png output/output.avi
    #ffmpeg -y -i output/output.avi -b:v 8500k -s 1920x1080 output/output.gif # uncomment  for generating gifs for website
else
    echo "ffmpeg not found - animation from images could not be generated"
fi