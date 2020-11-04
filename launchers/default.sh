#!/bin/bash

source /environment.sh

# initialize launch file
dt-launchfile-init

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------


# NOTE: Use the variable DT_REPO_PATH to know the absolute path to your code
# NOTE: Use `dt-exec COMMAND` to run the main process (blocking process)

# launching app
#dt-exec echo "This is an empty launch script. Update it to launch your application."
dt-exec Xvfb :1 -screen 0 1024x768x24 -ac +extension GLX +render -noreset 
export DISPLAY=:1
dt-exec rosrun simulatorwrapper simulatorwrapper.py

# ----------------------------------------------------------------------------
# YOUR CODE ABOVE THIS LINE

# wait for app to end
dt-launchfile-join
