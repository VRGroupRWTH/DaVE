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
    echo "${c}/${count} execute ${entry} ..."
    chmod +x ${entry}
    ./${entry} | indent
    RC=${PIPESTATUS[0]}
    if [ "${RC}" = "0" ] ; then
	s=$((s+1))
    else
	echo "${entry} failed"
    fi
done
echo "Successfully completed ${s}/${count} examples"
