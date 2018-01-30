import os


def sample():
    cwddir = os.getcwd()
    #path = r"C:\Users\GURC4657\Desktop\ppp"
    path = r"Sampletest"
    if os.path.exists(path):
        print "the directory already exists"
    else:
        os.mkdir(path)
        print "the directory got created"
    os.chdir(path)
    with open("vmtest.txt", 'w') as f:
        f.write "hello world\n Welcome to VM test file"

sample()

