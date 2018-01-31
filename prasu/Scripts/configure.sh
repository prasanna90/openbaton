#!/bin/bash


FILE="/etc/ansible/hosts"

/bin/cat <<EOM >$FILE
[myservers]

172.19.77.161
EOM
