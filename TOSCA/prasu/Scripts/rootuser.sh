#!/usr/bin/expect -f

spawn sudo passwd root
expect "Enter new UNIX password:"
send "abc123\r"
expect "Retype new UNIX password:"
send "abc123\r"
interact

