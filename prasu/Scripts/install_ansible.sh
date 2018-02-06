#!/bin/bash

#yes Y | sudo apt-add-repository ppa:ansible/ansible

sudo apt-get update 

yes Y | sudo apt-get install ansible 
sudo apt-get install expect
sudo apt-get install sshpass


expect rootuser.sh
expect ssh.sh
