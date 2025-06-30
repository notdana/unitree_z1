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


# arm.MoveJ(joint_positions, gripper_position, speed)

# Gripper Positions (-1.5 > 0.0) (Opened > Closed)
gripper_pos = 0.0
jnt_speed = 1.0


#Actual Joint Positions [J6, ]


print("position1")
arm.MoveJ([0.5,0.1,0.1,0.5,-0.2,0.5], gripper_pos, jnt_speed)
print("position2")
arm.MoveJ([0.4,0.2,0.1,0.5,-0.2,0.5], gripper_pos, jnt_speed)
print("position3")
arm.MoveJ([0.3,-0.1,0.1,0.5,-0.2,0.5], gripper_pos, jnt_speed)
print("position4")
arm.MoveJ([0.2,-0.2,0.1,0.5,-0.2,0.5], gripper_pos, jnt_speed)
print("position5")
arm.MoveJ([0.1,0.0,0.1,0.5,-0.2,0.5], gripper_pos, jnt_speed)



arm.backToStart()
arm.loopOff()

