#!/bin/bash

#set -e

CONTAINER=${1}
EXEC=${2}

case $EXEC in
    "local");;
    "mpi");;
    "slurm");;
    *)
	exit;;
esac

PREFIX="http://localhost:8080/api/create_script?visualization="
SUFFIXES=('Direct Volume Rendering'
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

mkdir -p test
rm test/*

set -e

for SUFFIX in "${SUFFIXES[@]}";
do
    wget -P test "${PREFIX}${SUFFIX}&technique=${CONTAINER}&command=${EXEC}" -O tmp.zip
    unzip -n -q tmp.zip -d test
done

rm tmp.zip

# execute examples
cd test

for entry in *.sh
do
    echo "execute ${entry} ..."
    chmod +x ${entry}
    ./${entry}
done
