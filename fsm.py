import sys
sys.path.append("../lib")
import unitree_arm_interface
import time
import numpy as np
np.set_printoptions(precision=3, suppress=True)


arm =  unitree_arm_interface.ArmInterface(hasGripper=True)
armState = unitree_arm_interface.ArmFSMState
arm.loopOn()


#arm.startTrack(armState.JOINTCTRL)

#This goes to a saved position of "0.0, 1.5, -1.0, -0.54, 0.0, 0.0"
arm.labelRun("forward")



gripper_pos = 0.0
jnt_speed = 2.0

# arm.MoveJ(joint_positions, gripper_position, speed)
arm.MoveJ([0.0, 1.5, -1.0, -0.54, 0.0, 0.0], gripper_pos, jnt_speed)

# gripper_pos = -1.0
# cartesian_speed = 0.5
# arm.MoveL([0,0,0,0.45,-0.2,0.2], gripper_pos, cartesian_speed)
# gripper_pos = 0.0
# arm.MoveC([0,0,0,0.45,0,0.4], [0,0,0,0.45,0.2,0.2], gripper_pos, cartesian_speed)

time.sleep(30)

arm.backToStart()
arm.loopOff()

