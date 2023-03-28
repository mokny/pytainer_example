import time
import sys
import pathlib

# For custom import paths, use this:
#   sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()) + '/mylibdir')
#   import mylib

active = True

# This is an example loop, that will run with or without pyTainer.
def mainLoop():
    print(config['greeting'])  # 'greeting' was defined at the pytainer.toml file
    counter = 0
    while active:
        counter += 1
        print("Output of some loop from a non blocking thread - Loop: " + str(counter) + " - Now waiting for " + str(config['sleeptime']) + " seconds")
        time.sleep(config['sleeptime'])

# This function gets called when the app was started as NON-Standalone
def pytainer_init(app):
    # 'pyTainerThread' references the underlying thread. See the docs how to use.
    print("I am running as a pyTainer Module.")
    print("Init function called.")
    global config
    config = app.config
    
    mainLoop()

# This function gets called when the app was stopped as NON-Standalone
def pytainer_stop(app):
    print("Stop function called.")
    global active
    active = False

# This detects if the app is running inside pyTainer.
if not 'pytainerserver' in sys.modules:
    print("Not running as pyTainer Module, initializing manually.")
    sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()) + '/../../ipc')
    import pytaineripc

    # Standalone Apps get the config via the IPC Interface
    config = pytaineripc.getConfig('unique_ident') # 'unique_ident' is the ident defined at the pytainer.toml file
    
    mainLoop()






