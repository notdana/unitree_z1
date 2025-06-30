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



# arm.MoveJ(joint_positions, gripper_position, speed)
gripper_pos = 0.0
jnt_speed = 2.0

arm.MoveJ([0.0, 1.5, -1.0, -0.54, 0.0, 0.0], gripper_pos, jnt_speed)
time.sleep(10)
arm.MoveJ([1.0, 1.5, -1.0, -0.54, 0.0, 0.0], gripper_pos, jnt_speed)


arm.backToStart()
arm.loopOff()

