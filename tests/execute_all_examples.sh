#!/bin/bash

set -eo pipefail

# indent funciton for more readable output
indent() { sed 's/^/  /'; }

# execute all examples
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
echo "Successfully completed ${c}/${count} examples"
