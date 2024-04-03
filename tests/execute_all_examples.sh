#!/bin/bash

set -eo pipefail

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
rm test/* || true

for SUFFIX in "${SUFFIXES[@]}";
do
    wget -P test "${PREFIX}${SUFFIX}&technique=${CONTAINER}&command=${EXEC}" -O tmp.zip
    unzip -n -q tmp.zip -d test
done

rm tmp.zip

# execute examples
indent() { sed 's/^/  /'; }

cd test
count=$(ls -1q *.sh | wc -l)
s=0
c=0

for entry in *.sh
do
    c=$((c+1))
    echo "${s}/${count} execute ${entry} ..."
    chmod +x ${entry}
    if ./${entry} | indent ; test ${PIPESTATUS[0]} -eq 0 ; then
	s=$((s+1))
    fi
done
echo "Completed ${c}/${count} examples"
