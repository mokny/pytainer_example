import time
import sys

# For custom import paths, use this:
#   import pathlib
#   abspath = str(pathlib.Path(__file__).parent.resolve())
#   sys.path.insert(0, abspath + '/mylibdir')
#   import mylib

# Communicating with pyTainer if this is a standalone APP
#import pathlib
#sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()) + '/../../ipc')
#import pytaineripc
#pytaineripc.do("METHOD")

print("Outside a function")

active = True
counter = 0

def myLoop():
    global active
    global counter
    while active:
        counter += 1
        print("Output of some loop from a non blocking thread - Loop: " + str(counter))
        time.sleep(1)

def pytainer_init(pyTainerThread):
    # 'pyTainerThread' references the underlying thread. See the docs how to use.
    print("I am running as a pyTainer Module.")
    print("Init function called.")
    myLoop()

def pytainer_stop(pyTainerThread):
    print("Stop function called.")
    global active
    active = False

# This way you can detect if your app is running inside pyTainer. If not, call the loop 'manually'
if not 'pytainerserver' in sys.modules:
    print("Not running as pyTainer Module, initializing manually.")
    myLoop()
