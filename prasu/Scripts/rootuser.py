#!/usr/bin/env python
import pexpect

def connection():
    msg_newkey = 'Enter new UNIX password:'
    p=pexpect.spawn('sudo passwd root')
    i=p.expect([msg_newkey,'Retype new UNIX password:',pexpect.EOF])
    if i==0:
        print "Accepting key."
        p.sendline('abc123')
        i=p.expect([msg_newkey,'Retype new UNIX password:',pexpect.EOF])
    if i==1:
        print "Supplying password"
        p.sendline("abc123")
    elif i==2:
        if "No route to host" in p.before:
            print p.before
        else:
            pass    # Add no functionality, just saying "move on"

connection()
