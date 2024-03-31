#!/bin/bash

set -e

# check for the existence of data and use default when none found
mkdir -p data
mkdir -p output
if ! test -f "${DATA_PATH}"; then
    echo "data set '${DATA_PATH}' not found - using default"
    DATA_PATH="./data/spherical001.nc"
    if ! test -f "${DATA_PATH}"; then 
	    cd data
	    wget "${DATA_URL}" -O mantle.tgz
        tar -zxvf mantle.tgz
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
    docker run --rm -v .:/example -w /example "${CONTAINER_URL}" ${EXEC} ${COMMAND} "${DATA_PATH}"
fi;

# assemble run command for singularity
if [[ "${CONTAINER_PLATFORM}" == "singularity" ]]; then
    ${EXEC} singularity run --containall  -H "${PWD}:/example" "docker://${CONTAINER_URL}" ${COMMAND} "${DATA_PATH}"
fi;
