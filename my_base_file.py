import time
import sys

# For custom import paths, use this:
#   import pathlib
#   abspath = str(pathlib.Path(__file__).parent.resolve())
#   sys.path.insert(0, abspath + '/mylibdir')
#   import mylib

print("Outside a function")

active = True


def myLoop():
    global active
    while active:
        print("Output of some loop from a non blocking thread")
        time.sleep(1)

def pytainer_init(pyTainerThread):
    # 'pyTainerThread' references the underlying thread. See the docs how to use.
    print("Init function called")
    myLoop()

def pytainer_stop(pyTainerThread):
    print("Stop function called")
    global active
    active = False

# This way you can detect if your app is running inside pyTainer. If not, call the loop 'manually'
if not 'pytainerserver' in sys.modules:
    myLoop()
