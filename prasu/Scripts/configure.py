import os

def main():
    path = r"/etc/ansible/hosts"
    with open(path, "a") as f:
        f.write("[myservers]" + "\n" + "172.19.77.161")
