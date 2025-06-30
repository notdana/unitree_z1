import sys
sys.path.append("../lib")
import unitree_arm_interface
import time
import numpy as np
np.set_printoptions(precision=3, suppress=True)


arm =  unitree_arm_interface.ArmInterface(hasGripper=True)
armState = unitree_arm_interface.ArmFSMState
arm.loopOn()

arm.labelRun("forward")
arm.startTrack(armState.JOINTCTRL)

jnt_speed = 1.0
for i in range(0, 1000):
    # dp = directions * speed; include 7 joints
    arm.jointCtrlCmd([0,0,0,-1,0,0,-1], jnt_speed)
    time.sleep(arm._ctrlComp.dt)

arm.backToStart()
arm.loopOff()
