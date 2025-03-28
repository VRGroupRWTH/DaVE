#!/bin/bash

set -e

# check for the existence of data and use default when none found
mkdir -p data
mkdir -p output
if ! test -f "${FLOWFIELD_PATH}"; then
    echo "data set '${FLOWFIELD_PATH}' not found - using default"
    FLOWFIELD_PATH="./data/jet.vti"
    if ! test -f "${FLOWFIELD_PATH}"; then 
	    cd data
	    wget "${FLOWFIELD_URL}"
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
    docker run --rm -v .:/example -w /example "${CONTAINER_URL}" ${EXEC} ${COMMAND} "${FLOWFIELD_PATH}"
fi;

# assemble run command for singularity
if [[ "${CONTAINER_PLATFORM}" == "singularity" ]]; then
    singularity pull --force container.sif "docker://${CONTAINER_URL}"
    ${EXEC} singularity run --containall  -H "${PWD}:/example" container.sif  ${COMMAND} "${FLOWFIELD_PATH}"
fi;
