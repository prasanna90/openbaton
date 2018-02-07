#!/bin/bash

sed -i 's/#roles_path/roles_path/g' /etc/ansible/ansible.cfg

expect bugplaybook.sh
