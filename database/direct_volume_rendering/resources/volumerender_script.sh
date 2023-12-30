#!/bin/bash

set -e

wget "https://raw.githubusercontent.com/topology-tool-kit/ttk-data/dev/ctBones.vti"

docker pull kitware/paraview:pv-v5.7.1-osmesa-py3

docker run --rm  -v .:/example -w /example kitware/paraview:pv-v5.7.1-osmesa-py3 /opt/paraview/bin/pvpython volumerender_trace.py
