#!/usr/bin/expect

spawn ssh root@172.19.77.162
expect "Are you sure you want to continue connecting (yes/no)?"
send "yes\r"
expect "root@172.19.77.162's password:"
send "abc123\r"
interact

