#!/usr/bin/env python
import os
import paramiko
import time
import subprocess

def playbook():
    proc = subprocess.Popen("hostname -i".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out1, err1 = proc.communicate()
    print out1
    out1 = host
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username="root", password="abc123", port=22)
        channel = ssh.invoke_shell()
        out = channel.recv(9999)
        channel.send("cd /etc/ansible\n")
        channel.send("ls\n")
        while not channel.recv_ready():
            time.sleep(3)
        out = channel.recv(9999)
        print(out.decode("ascii"))
        channel.send("mv /opt/openbaton/scripts/prasu/bugzilla /etc/ansible\n")
        while not channel.recv_ready():
            time.sleep(3)
        out = channel.recv(9999)
        print(out.decode("ascii"))
        channel.send("mv /opt/openbaton/scripts/prasu/Scripts/bugzilla_ans.yml /etc/ansible\n")
        while not channel.recv_ready():
            time.sleep(3)
        out = channel.recv(9999)
        print(out.decode("ascii"))
        channel.send("ansible" + " " + host + " " + "-m ping -u root -k\n")
        while not channel.recv_ready():
            time.sleep(3)
        out = channel.recv(9999)
        print(out.decode("ascii"))
        channel.send("abc123\n")
        while not channel.recv_ready():
            time.sleep(3)
        out = channel.recv(9999)
        print(out.decode("ascii"))
        channel.send("ansible-playbook bugzilla_ans.yml -k\n")
        while not channel.recv_ready():
            time.sleep(3)
        out = channel.recv(9999)
        print(out.decode("ascii"))
        channel.send("abc123\n")
        while not channel.recv_ready():
            time.sleep(10)
        out = channel.recv(99999999999999)
        print(out.decode("ascii"))
    except Exception as e:
       print "exception occured:", e
playbook()

