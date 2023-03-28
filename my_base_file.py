import time
import sys
import pathlib

# For custom import paths, use this:
#   sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()) + '/mylibdir')
#   import mylib

active = True

# This is an example loop, that will run with or without pyTainer.
def main():
    print(config['greeting'])  # 'greeting' was defined at the pytainer.toml file
    counter = 0
    while active:
        counter += 1
        print("Output of some loop from a non blocking thread - Loop: " + str(counter) + " - Now waiting for " + str(config['sleeptime']) + " seconds")
        time.sleep(config['sleeptime'])

# This function gets called when the app was started as NON-Standalone
# pyTainer passes the configuration as parameter - Here app.config
def pytainer_init(app):
    print("I am running as a pyTainer Module.")
    print("Init function called.")
    global config
    config = app.config
    main() # Start our main function from here

# This function gets called when the app was stopped as NON-Standalone
def pytainer_stop(app):
    print("Stop function called.")
    global active
    active = False

# This detects if the app is running inside pyTainer.
if not 'pytainerserver' in sys.modules:
    print("I am running as Standalone")
    
    # Import the IPC interface to communicate with pyTainer
    sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve()) + '/../../ipc')
    import pytaineripc

    # Fetch the configuration from pyTainer
    config = pytaineripc.getConfig('unique_ident') # 'unique_ident' is the ident defined at the pytainer.toml file
    
    main() # Start our main function from here
    
else:
    print("I am running as NON-Standalone")
    
    import pytaineripc






