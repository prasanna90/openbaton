#!/bin/bash

sudo mv /opt/openbaton/scripts/prasu/bugzilla /etc/ansible
sudo mv /opt/openbaton/scripts/prasu/bugzilla_ans.yml /etc/ansible
OUTPUT="$(hostname -i)"
echo "${OUTPUT}"
expect -f playbook.sh ${OUTPUT}
