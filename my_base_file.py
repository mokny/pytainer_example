import time
import sys
import pathlib

# For custom import paths, use this:
#   sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()) + '/mylibdir')
#   import mylib

# Communicating with pyTainer if this is a standalone APP
sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()) + '/../../ipc')
import pytaineripc

# Standalone Apps get the config via the IPC Interface
config = pytaineripc.getConfig('unique_ident') # 'unique_ident' is the ident defined at the pytainer.toml file

print(config['greeting'])       # 'greeting' was defined at the pytainer.toml file

active = True
counter = 0

def myLoop():
    global active
    global counter
    while active:
        counter += 1
        print("Output of some loop from a non blocking thread - Loop: " + str(counter) + " - Now waiting for " + str(config['sleeptime']) + " seconds")
        time.sleep(config['sleeptime'])

def pytainer_init(app):
    # 'pyTainerThread' references the underlying thread. See the docs how to use.
    print("I am running as a pyTainer Module.")
    print("Init function called.")
    myLoop()

def pytainer_stop(app):
    print("Stop function called.")
    global active
    active = False

# This way you can detect if your app is running inside pyTainer. If not, call the loop 'manually'
if not 'pytainerserver' in sys.modules:
    print("Not running as pyTainer Module, initializing manually.")
    myLoop()
