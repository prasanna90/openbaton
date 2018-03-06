#!/usr/bin/expect -f


set IP   [lindex $argv 0];
spawn ssh root@$IP
expect "Are you sure you want to continue connecting (yes/no)?"
send "yes\r"
expect "root@$IP's password:"
send "abc123\r"
interact
