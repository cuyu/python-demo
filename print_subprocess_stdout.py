import subprocess

if __name__ == '__main__':
    proc = subprocess.Popen('ls /tmp -a', shell=True, stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if line != '':
            print "test:", line.rstrip()
        else:
            break
