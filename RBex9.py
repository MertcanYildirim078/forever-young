from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for x in range(4):
    for x in range(4):
        robotArm.speed = 2
        for x in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(4):
            robotArm.moveLeft()
        robotArm.grab()
    for x in range(6):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
