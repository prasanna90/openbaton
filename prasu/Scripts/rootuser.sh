#!/bin/bash

sudo su
#sudo passwd root 
pass=abc123
echo $pass | sudo passwd root
#abc123
#abc123
sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
sudo service ssh restart
echo $pass | ssh -o StrictHostKeyChecking=no -l root 172.19.77.161





#echo $efi | sudo -S firmwarepasswd -verify

