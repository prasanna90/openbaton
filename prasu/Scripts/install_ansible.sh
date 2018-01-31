#!/bin/bash

sudo apt-add-repository ppa:ansible/ansible

expect "Press [ENTER] to continue or ctrl-c to cancel adding it"
send "yes"

sudo apt-get update && sudo apt-get install ansible
