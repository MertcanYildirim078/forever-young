from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
for x in range(9):
    robotArm.speed = 2
    robotArm.grab()
    color = robotArm.scan()
    if color == 'white':
        afstand = 9 - x
        for c in range(afstand):
            robotArm.moveRight()
        robotArm.drop()
        for r in range(afstand - 1):
            robotArm.moveLeft()
    else:   
        robotArm.drop()
        robotArm.moveRight()
# 0 word 9
# 6 word 3 en 7 word 2
# colorw = color == 'white'
# while colorw == False:
#         color = robotArm.scan()
#         print(color)
#         robotArm.drop()
#         robotArm.moveRight()
#         robotArm.grab()
#         if colorw == True:
#             for x in range(10):
#                 robotArm.moveRight()
#             robotArm.drop()
#             for x in range(8):
#                 robotArm.moveLeft()

#if colorw == True:
    #for x in range(10):
        #robotArm.moveRight()
    #robotArm.drop()
    #for x in range(8):
        #robotArm.moveLeft()
#else:
    #while colorw == False:
        #color = robotArm.scan()
       # print(color)
       # robotArm.drop()
       ## robotArm.moveRight()
       # robotArm.grab()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
