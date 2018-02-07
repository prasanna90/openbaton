#!/usr/bin/env python
import os
import paramiko
import time

def playbook():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect("172.19.77.161", username="root", password="abc123", port=22)
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
        channel.send("ansible 172.19.77.161 -m ping -u root -k\n")
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

