#!/bin/bash

set -e

# check for the existence of data and use default when none found
mkdir -p data
mkdir -p output
if ! test -f "${DATASET_POINTCLOUD_PATH}"; then
    echo "data set '${DATASET_POINTCLOUD_PATH}' not found - using default"
    DATASET_POINTCLOUD_PATH="./data/smoothinglength_0.30/run01/090.vtu"
    if ! test -f "${DATASET_POINTCLOUD_PATH}"; then 
	    cd data
	    wget "${DATASET_POINTCLOUD_URL}" -O pointcloud.tar.bz2
        tar jxvf pointcloud.tar.bz2
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
    docker run --rm -v .:/example -w /example "${CONTAINER_URL}" ${EXEC} ${COMMAND} "${DATASET_POINTCLOUD_PATH}"
fi;

# assemble run command for singularity
if [[ "${CONTAINER_PLATFORM}" == "singularity" ]]; then
    singularity pull --force container.sif "docker://${CONTAINER_URL}"
    ${EXEC} singularity run --containall  -H "${PWD}:/example" container.sif  ${COMMAND} "${DATASET_POINTCLOUD_PATH}"
fi;

if command -v ffmpeg &> /dev/null
then
    ffmpeg -hide_banner -loglevel error -y -framerate 10 -i output/pointcloud.%04d.png output/pointcloud.webp
else
    echo "ffmpeg not found - animation from images could not be generated"
fi