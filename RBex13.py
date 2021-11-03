from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
# Jouw python instructies zet je vanaf hier:
afstand = 1
while True:
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        for z in range(afstand):
            robotArm.moveRight()
        robotArm.drop()
        for c in range(afstand):
            robotArm.moveLeft()

        afstand += 1
    else:
        break



# for x in range(7):
#     robotArm.speed = 2
#     afstandrechts = 7
#     afstandlinks = 7
#     robotArm.grab()
#     for s in range(afstandrechts):
#         robotArm.moveRight()
#     robotArm.drop()
#     for d in range(afstandlinks):
#         robotArm.moveLeft()
#     afstandrechts -= 1
#     afstandlinks -= 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
