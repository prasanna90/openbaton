#!/usr/bin/env python
import os
import subprocess

def main():
    proc = subprocess.Popen("hostname".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out1, err1 = proc.communicate()
    print out1
    proc = subprocess.Popen("hostname -i".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out2, err2 = proc.communicate()
    print out2
    cwddir = os.getcwd()
    path = r"/etc/hosts"
    try:
        with open(path, "a") as f:
            f.write(out2 + "\t" + out1)
    except Exception as e:
        print "error occured:", e
main()
