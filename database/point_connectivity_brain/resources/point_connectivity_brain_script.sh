#!/bin/bash

set -e

# check for the existence of data and use default when none found
mkdir -p data
mkdir -p output
if ! test -f "${DATASET_BRAIN_PATH}"; then
    echo "data set '${DATASET_BRAIN_PATH}' not found - using default"
    DATASET_BRAIN_PATH="./data/brainData_all.vtk"
    if ! test -f "${DATASET_BRAIN_PATH}"; then 
	    cd data
	    wget "${DATASET_BRAIN_URL}"
	    cd ..
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
    docker run --rm -v .:/example -w /example "${CONTAINER_URL}" ${EXEC} ${COMMAND} "${DATASET_BRAIN_PATH}"
fi;

# assemble run command for singularity
if [[ "${CONTAINER_PLATFORM}" == "singularity" ]]; then
    singularity pull --force container.sif "docker://${CONTAINER_URL}"
    ${EXEC} singularity run --containall  -H "${PWD}:/example" container.sif  ${COMMAND} "${DATASET_BRAIN_PATH}"
fi;