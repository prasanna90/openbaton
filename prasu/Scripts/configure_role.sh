#!/bin/bash

file:'/etc/ansible/ansible.cfg'

sed -i '/^#.* roles_path /s/^#//' file

