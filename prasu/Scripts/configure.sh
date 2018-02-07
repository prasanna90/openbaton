#!/bin/bash


FILE="/etc/ansible/hosts"

/bin/cat <<EOT >> $FILE
[myservers]

172.19.77.161
172.19.77.162
EOT

sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
sudo service ssh restart

