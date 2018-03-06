import os
#import subprocess
from subprocess import Popen, PIPE
#mport pexpect
import sys
STDERR = sys.stderr
def excepthook(*args):
    print >> STDERR, 'caught'
    print >> STDERR, args

sys.excepthook = excepthook

def main():
    #os.chdir("/opt/openbaton/scripts/prasu")
    #os.system("mv bugzilla /etc/ansible")
    #os.system("mv bugzilla_ans.yml /etc/ansible")
    os.chdir("/etc/ansible")
    
    #proc = subprocess.Popen("ansible 172.19.77.161 -m ping -u root -k".split(),stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    proc=Popen('ansible 172.19.77.161 -m ping -u root -k'.split(), stdin=PIPE, stdout=PIPE)
    sys.stdout.readline()
    sys.stdin.write("abc123\n")
    sys.stdin.flush()
    #proc.communicate("abc123")    
    #outQueue = Queue()
    #errQueue = Queue()
    #proc.stdin.write("abc123\n")
    #proc.stdin.flush()
    #proc.stdin.close()
    #proc = subprocess.Popen("hostname".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #errors = getOutput(errQueue)
    #output = getOutput(outQueue)
    #out1, err1 = proc.communicate()
    #print out1
    #proc.stdin.write("abc123\n")

    #child = pexpect.spawn("ansible 172.19.77.161 -m ping -u root -k")
    #child.expect(pexpect.EOF)
    #child.expect("SSH Password:")
    #child.sendline("abc123")
    #output = child.before
    #print output
    
    #print os.system("ansible 172.19.77.161 -m ping -u root")
    #print os. system("ansible-playbook bugzilla_ans.yml")
main()


