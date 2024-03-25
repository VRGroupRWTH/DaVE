#!/bin/bash

set -e

# check for the existence of data and use default when none found
mkdir -p data
mkdir -p output
if ! test -f "${DENSITYFIELDHEADER_PATH}"; then
    echo "data set '${DENSITYFIELDHEADER_PATH}' not found - using default"
    DENSITYFIELDHEADER_PATH="./data/miranda.nhdr"
    DENSITYFIELD_PATH="./data/miranda_1024x1024x1024_float32.raw"
    if ! test -f "${DENSITYFIELDHEADER_PATH}"; then 
	    cd data
	    wget "${DENSITYFIELDHEADER_URL}"
        wget "${DENSITYFIELD_URL}"
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
    docker run --rm -v .:/example -w /example "${CONTAINER_URL}" ${EXEC} ${COMMAND} "${DENSITYFIELDHEADER_PATH}"
fi;

# assemble run command for singularity
if [[ "${CONTAINER_PLATFORM}" == "singularity" ]]; then
    ${EXEC} singularity run --containall  -H "${PWD}:/example" "docker://${CONTAINER_URL}" ${COMMAND} "${DENSITYFIELDHEADER_PATH}"
fi;
