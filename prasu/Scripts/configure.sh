#!/bin/bash


OUTPUT="$(hostname -i)"
echo "${OUTPUT}"
FILE="/etc/ansible/hosts"

/bin/cat <<EOT >> $FILE
[myservers]

${OUTPUT}
EOT
