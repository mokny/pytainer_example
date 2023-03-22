import time
import logger

logger.out("This is a pyTainer Example Program. This line executes because it's outside a function / class")

active = True

# A pyTainer program should contain an init() function. Even if it's not required. pyTainer may pass useful
# information as a parameter.
def init():
    logger.info("Initialization Routine called")  
    global active
    while active:
        logger.info("This message comes from a pyTainer program. It's running inside a non blocking thread.")
        time.sleep(1)

# The stop() function will be called before the pyTainer thread ends. You can do your cleanup here.
def stop():
    global active
    logger.info("Stopping the loop")
    active = False

