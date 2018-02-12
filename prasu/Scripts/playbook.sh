#!/usr/bin/expect -f


set IP   [lindex $argv 0];
spawn ansible $IP -m ping -u root -k
expect "SSH password:"
send "abc123\r"
interact

spawn ansible-playbook bugzilla_ans.yml -k
expect "SSH password:"
send "abc123\r"
interact
