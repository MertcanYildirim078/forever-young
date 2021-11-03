from sys import _xoptions
from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
# Jouw python instructies zet je vanaf hier:
for x in range(10):
    robotArm.speed = 2
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        afstand = 10 - x
        for s in range(afstand + 1):
            robotArm.moveRight()
        robotArm.drop()
        for  c in range(afstand  - 1):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
