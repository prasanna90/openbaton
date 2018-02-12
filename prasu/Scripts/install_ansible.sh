#!/bin/bash

#yes Y | sudo apt-add-repository ppa:ansible/ansible
#sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6494C6D6997C215E
sudo rm -rf /var/lib/apt/lists/*
sudo apt-get update 

yes Y | sudo apt-get install ansible 
sudo apt-get install expect
sudo apt-get install sshpass
sudo apt-get install python-pexpect

#expect rootuser.sh
#expect ssh.sh
