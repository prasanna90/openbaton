#!/usr/bin/env python
import pexpect


def test():
   # password = "abc123"
    p=pexpect.spawn("sudo passwd root")
    p.expect("Enter new UNIX password:")
    p.sendline("abc123\n")
    print p.after + "abc123\n"
    p.expect("Retype new UNIX password:")
    p.sendline("abc123\n")
    print p.after + "abc123\n"
    i=p.expect("passwd: password updated successfully")
    print i
    if i==0:
        print "password is changed successfully"
    else:
        print "failed to change password"
    
    
 
def connection():
    msg_newkey = 'Enter new UNIX password:'
    p=pexpect.spawn('sudo passwd root')
    i=p.expect([msg_newkey,'Retype new UNIX password:',pexpect.EOF])
    print p.after
    print i
    if i==0:
        print "Accepting key."
        p.sendline('abc123')
        print p.before
        i=p.expect([msg_newkey,'Retype new UNIX password:',pexpect.EOF])
        print p.after
        print i
    if i==1:
        print "Supplying password"
        p.sendline("abc123")
        print p.after
    elif i==2:
        if "No route to host" in p.before:
            print p.before
        else:
            pass    # Add no functionality, just saying "move on"

test()
