#!/usr/bin/expect

cd /opt/openbaton/scripts/prasu/Scripts
sudo mv bugzilla /etc/ansible
sudo mv bugzilla_ans.yml /etc/ansible
cd /etc/ansible

spawn ansible 172.19.77.161 -m ping -u root -k
expect "SSH password:"
send "abc123\r"
interact
cd /etc/ansible
spawn ansible-playbook bugzilla_ans.yml -k
expect "SSH password:"
send "abc123\r"
interact

