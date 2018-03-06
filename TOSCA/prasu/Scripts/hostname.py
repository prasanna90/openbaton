#!/usr/bin/env python
import os
import subprocess

def main():
    proc = subprocess.Popen("hostname".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out1, err1 = proc.communicate()
    print out1
    cwddir = os.getcwd()
    path = r"/etc/hosts"
    try:
        with open(path, "a") as f:
            f.write("127.0.0.1"+"\t"+ out1.strip())
    except Exception as e:
        print "error occured:", e
main()
