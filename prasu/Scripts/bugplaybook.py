import os
import subprocess

def main():
    os.chdir("/opt/openbaton/scripts/prasu")
    os.system("mv bugzilla /etc/ansible")
    os.system("mv bugzilla_ans.yml /etc/ansible")
    os.chdir("/etc/ansible")
    print os.system("ansible 172.19.77.161 -m ping -u root")
    print os. system("ansible-playbook bugzilla_ans.yml")
main()


