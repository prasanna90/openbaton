#!/bin/bash

#yes Y | sudo apt-add-repository ppa:ansible/ansible
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y ansible
sudo apt-get update 

#yes Y | sudo apt-get install ansible 
sudo apt-get install expect
sudo apt-get install sshpass
sudo apt-get install python-pexpect

#expect rootuser.sh
#expect ssh.sh
