#!/bin/bash

set -eo pipefail

CONTAINER=${1}
EXEC=${2}

# check if execution type is a valid option
case $EXEC in
    "local");;
    "mpi");;
    "slurm");;
    *)
	exit;;
esac

# define example urls
PREFIX="http://localhost:8080/api/create_script?visualization="
SUFFIXES=('Adaptive Mesh Refinement'
	  'Direct Volume Rendering'
	  'Glyphs'
	  'Heatmap'
	  'Isocontours'
	  'Line-Integral Convolution (LIC)'
	  'Line-Integral Convolution (LIC) of a Jet Flow'
	  'Muliple Slices'
	  'Parallel Coordinates'
	  'Pathline'
	  'Point Cloud Multifield'
	  'Scatterplots'
	  'Streamlines'
	  'Velocity Gradient Tensor'
	  'Volume Statistics'
	 )

# create test directory and clean up old scripts
mkdir -p test
rm test/* || true

# get scripts and unzip
for SUFFIX in "${SUFFIXES[@]}";
do
    wget -P test "${PREFIX}${SUFFIX}&technique=${CONTAINER}&command=${EXEC}" -O tmp.zip
    unzip -n -q tmp.zip -d test
done
rm tmp.zip
