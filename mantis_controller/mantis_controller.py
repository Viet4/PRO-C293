from controller import Robot

robot = Robot()

timestep = 320
flag = 0

leg_left_front = robot.getDevice("LAC")
leg_left_middle = robot.getDevice("LMC")
leg_left_back = robot.getDevice("LPC")

leg_right_front = robot.getDevice("RAC")
leg_right_middle = robot.getDevice("RMC")
leg_right_back = robot.getDevice("RPC")

while robot.step(timestep) != -1:
    if flag % 4 == 0:
        leg_left_front.setPosition(-0.3)
        leg_right_front.setPosition(0.3)
    elif flag % 4 == 1:
        leg_left_middle.setPosition(-0.3)
        leg_right_middle.setPosition(0.3)
    elif flag % 4 == 2:
        leg_left_back.setPosition(-0.3)
        leg_right_back.setPosition(0.3)
    elif flag % 4 == 3:
        leg_left_front.setPosition(0.2)
        leg_left_middle.setPosition(0.2)
        leg_left_back.setPosition(0.2)
        leg_right_front.setPosition(-0.2)
        leg_right_middle.setPosition(-0.2)
        leg_right_back.setPosition(-0.2)
    flag += 1