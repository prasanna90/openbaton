#!/bin/bash

OUTPUT="$(hostname -i)"
echo "${OUTPUT}"
expect -f ssh.sh ${OUTPUT}
