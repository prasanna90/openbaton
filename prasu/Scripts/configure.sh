#!/bin/bash


FILE="/etc/ansible/hosts"

/bin/cat <<EOT >> $FILE
[myservers]

172.19.77.161
EOT
