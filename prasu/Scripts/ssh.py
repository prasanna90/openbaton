#!/usr/bin/env python
import pexpect

def connection():
    msg_newkey = "Are you sure you want to continue connecting (yes/no)?"
    p=pexpect.spawn("ssh root@172.19.77.143")
    i=p.expect([msg_newkey,"root@172.19.77.143's password:",pexpect.EOF])
    if i==0:
        print "Accepting key."
        p.sendline('yes')
        i=p.expect([msg_newkey,'password:',pexpect.EOF])
    if i==1:
        print "Supplying password"
        p.sendline("abc123")
    elif i==2:
        if "No route to host" in p.before:
            print p.before
        else:
            pass    # Add no functionality, just saying "move on"

connection()

