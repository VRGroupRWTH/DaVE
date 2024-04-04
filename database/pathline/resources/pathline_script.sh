#!/bin/bash

set -e

# check for the existence of data and use default when none found
mkdir -p data
mkdir -p output
if ! test -d "${DATASET_VOLUME_PATH}"; then
    echo "data set '${DATASET_VOLUME_PATH}' not found - using default"
    DATASET_VOLUME_PATH="./data/jet4/"
    if ! test -d "${DATASET_VOLUME_PATH}"; then
        # TODO download default data set
        cd data
        wget "${DATASET_VOLUME_URL}"
        cd ..
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
    docker run --rm -v .:/example -w /example "${CONTAINER_URL}" ${EXEC} ${COMMAND} "${DATASET_VOLUME_PATH}"
fi;

# assemble run command for singularity
if [[ "${CONTAINER_PLATFORM}" == "singularity" ]]; then
    ${EXEC} singularity run --containall -H "${PWD}:/example" "docker://${CONTAINER_URL}" ${COMMAND} "${DATASET_VOLUME_PATH}"
fi;

if command -v ffmpeg &> /dev/null
then
    ffmpeg -hide_banner -loglevel error -y -framerate 10 -i output/pathline.%04d.png output/pathline.avi
    #ffmpeg -y -i output/output.avi -b:v 8500k -s 1920x1080 output/output.gif # uncomment  for generating gifs for website
else
    echo "ffmpeg not found - animation from images could not be generated"
fi