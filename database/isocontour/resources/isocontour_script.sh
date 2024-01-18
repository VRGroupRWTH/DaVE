#!/bin/bash

set -e

# check for the existence of data and use default when none found
mkdir -p dataset
mkdir -p output
if ! test -f "${DATASET_VOLUME}"; then
    echo "data set '${DATASET_VOLUME}' not found - using default"
    DATASET_VOLUME="./dataset/ctBones.vti"
    if ! test -f "${DATASET_VOLUME}"; then
        echo "Error! No data found!" 1>$2
        exit 0
    fi;
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
    docker run --rm -v .:/example -w /example "${CONTAINER_URL}" ${EXEC} ${COMMAND} "${DATASET_VOLUME}"
fi;

# assemble run command for singularity
if [[ "${CONTAINER_PLATFORM}" == "singularity" ]]; then
    ${EXEC} singularity run --containall  -H "${PWD}:/example" "docker://${CONTAINER_URL}" ${COMMAND} "${DATASET_VOLUME}"
fi;