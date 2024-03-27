#!/bin/bash

set -e

# check for the existence of data and use default when none found
mkdir -p data
mkdir -p output
if ! test -f "${AMR_PATH}"; then
    echo "data set '${AMR_PATH}' not found - using default"
    AMR_PATH="./data/amr_mesh.vthb"
    if ! test -f "${AMR_PATH}"; then 
	    cd data
	    #wget "${AMR_URL}"
        unzip amr_mesh.zip
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
    docker run --rm -v .:/example -w /example "${CONTAINER_URL}" ${EXEC} ${COMMAND} "${AMR_PATH}"
fi;

# assemble run command for singularity
if [[ "${CONTAINER_PLATFORM}" == "singularity" ]]; then
    ${EXEC} singularity run --containall  -H "${PWD}:/example" "docker://${CONTAINER_URL}" ${COMMAND} "${AMR_PATH}"
fi;
