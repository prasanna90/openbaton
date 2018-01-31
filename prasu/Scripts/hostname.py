#!/usr/bin/env python
import os
import subprocess

def main():
    proc = subprocess.Popen("hostname".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out1, err1 = proc.communicate()
    print out1
    cwddir = os.getcwd()
    path = r"/etc/hosts"
    with open(path, "w") as f:
        f.write("172.19.77.161", out1)
main()
