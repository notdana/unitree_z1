import sys
sys.path.append("../lib")
import unitree_arm_interface
import time
import numpy as np
np.set_printoptions(precision=3, suppress=True)


arm =  unitree_arm_interface.ArmInterface(hasGripper=True)
armState = unitree_arm_interface.ArmFSMState
arm.loopOn()

#This goes to a saved position of "0.0, 1.5, -1.0, -0.54, 0.0, 0.0"
arm.labelRun("forward")
arm.startTrack(armState.JOINTCTRL)

#jointCtrlCmd sends joint velocity commands to the robot arm.
#It is used when the arm is in joint velocity control mode (JOINTCTRL).
#You must call it repeatedly (in a loop) to keep the arm moving

jnt_speed = 1.0
for i in range(0, 1000):
    # dp = directions * speed; include 7 joints
    arm.jointCtrlCmd([1,0,0,0,0,0,0], jnt_speed)
    time.sleep(arm._ctrlComp.dt)


arm.backToStart()
arm.loopOff()
