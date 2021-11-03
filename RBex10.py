from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
# Jouw python instructies zet je vanaf hier:
afstand = 9
afstandTerug = 8
robotArm.speed = 2
for x in range(5):
    robotArm.grab() 
    for s in range(afstand):
        robotArm.moveRight()
    robotArm.drop()
    for r in range(afstandTerug):
        robotArm.moveLeft()
    afstandTerug -= 2
    afstand -= 2
# for x in range(9):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(8):
#     robotArm.moveLeft()
# robotArm.grab()
# for x in range(7):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(6):
#     robotArm.moveLeft()
# robotArm.grab()
# for x in range(5):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(4):
#     robotArm.moveLeft()
# robotArm.grab()
# for x in range(3):
#     robotArm.moveRight()
# robotArm.drop()
# for x in range(2):
#     robotArm.moveLeft()
# robotArm.grab()
# for x in range(1):
#     robotArm.moveRight()
# robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

