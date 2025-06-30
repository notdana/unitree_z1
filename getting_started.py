import sys
sys.path.append("../lib")
import unitree_arm_interface
import time
import numpy as np
np.set_printoptions(precision=3, suppress=True)


arm =  unitree_arm_interface.ArmInterface(hasGripper=True)

arm.loopOn()

#This goes to a saved position of "0.0, 1.5, -1.0, -0.54, 0.0, 0.0"
arm.labelRun("forward")

arm.backToStart()
arm.loopOff()

