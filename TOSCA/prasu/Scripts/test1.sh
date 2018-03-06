#!/bin/bash

OUTPUT="$(hostname -i)"
echo "${OUTPUT}"
sudo expect -f ssh.sh ${OUTPUT}
