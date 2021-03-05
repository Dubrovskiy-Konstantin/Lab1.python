import os
import pwd
import datetime


def get_username():
    return pwd.getpwuid(os.getuid())[0]


if __name__ == "__main__":
    name = get_username()
    time = str(datetime.datetime.now())
    cmd = "{0} opened MyScript.py at {1}".format(name, time)
    f = open("Dialog.log", "a")
    f.write(cmd + "\n")
    f.close()
    cmd = "echo " + cmd
    os.system(cmd)
