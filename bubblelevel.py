# ***********
# Bubble Level
# ES2 Homework Assignment HW3
# ************************************************************
# FILL THESE COMMENTS IN
#*****************************************
# YOUR NAME: Gillian Wahleithner
# NUMBER OF HOURS TO COMPLETE: 5
# YOUR COLLABORATION STATEMENT(s): I worked on this assignment with Zosia and Hector.
#
#
#*****************************************
import math

from microbit import *

while True:

    #find acceleration of x, y, and z axis
    def acceleration_x():
        ax = accelerometer.get_x()
        return ax

    def acceleration_y():
        ay = accelerometer.get_y()
        return ay

    def acceleration_z():
        az = accelerometer.get_z()
        return az

    def anglex_radians(x, y, z):
        #find angle between x and z axis
        anglexradians = math.atan2(x, math.sqrt(y ** 2 + z ** 2))
        return anglexradians

    def angley_radians(x, y, z):
        #find angle between y and z axis
        angleyradians = math.atan2(y, math.sqrt(x ** 2 + z ** 2))
        return angleyradians

    def anglez_radians(x, y, z):
        #find angle between x and y axis
        anglezradians = math.atan2(z, math.sqrt(x ** 2 + y ** 2))
        return anglezradians

    while True:

        #run function to find acceleration of three axes
        ax = acceleration_x()
        ay = acceleration_y()
        az = acceleration_z()

        #run function to find three angles of axes
        anglexradians = anglex_radians(ax, ay, az)
        angleyradians = angley_radians(ay, ay, az)
        anglezradians = anglez_radians(ax, ay, az)

        #angle x, angle y, angle z from radians into degrees
        anglexdegrees = anglexradians * (180 / math.pi)
        angleydegrees = angleyradians * (180 / math.pi)
        anglezdegrees = anglezradians * (180 / math.pi)

        sleep(500)

        print((anglexdegrees, angleydegrees, anglezdegrees))

        dimARROW_N = Image("00300:03330:30303:00300:00300")
        medARROW_N = Image("00600:06660:60606:00600:00600")

        dimARROW_S = Image("00300:00300:30303:03330:00300")
        medARROW_S = Image("00600:00600:60606:06660:00600")

        dimARROW_E = Image("00300:00030:33333:00030:00300")
        medARROW_E = Image("00600:00060:66666:00060:00600")

        dimARROW_W = Image("00300:03000:33333:03000:00300")
        medARROW_W = Image("00600:06000:66666:06000:00600")





        if (anglexdegrees >= -5 and anglexdegrees <= 5) and (angleydegrees >= -5 and angleydegrees <= 5):
            display.show(Image.HAPPY)

        elif (angleydegrees > 5 and angleydegrees <= 15) and (angleydegrees > anglexdegrees):
            display.show(Image.ARROW_N)
        elif (angleydegrees > 15 and angleydegrees <= 30) and (angleydegrees > anglexdegrees):
            display.show(medARROW_N)
        elif (angleydegrees > 30) and (angleydegrees > anglexdegrees):
            display.show(dimARROW_N)

        elif (angleydegrees < -5 and angleydegrees >= -15) and (angleydegrees < anglexdegrees):
            display.show(Image.ARROW_S)
        elif (angleydegrees < -15 and angleydegrees >= -30) and (angleydegrees < anglexdegrees):
            display.show(medARROW_S)
        elif (angleydegrees < -30) and (angleydegrees < anglexdegrees):
            display.show(dimARROW_S)

        elif (anglexdegrees > 5 and anglexdegrees <= 15) and (anglexdegrees > angleydegrees):
            display.show(Image.ARROW_W)
        elif (anglexdegrees > 15 and anglexdegrees <= 30) and (anglexdegrees > angleydegrees):
            display.show(medARROW_W)
        elif (anglexdegrees > 30) and (anglexdegrees > angleydegrees):
            display.show(dimARROW_W)

        elif (anglexdegrees < -5 and anglexdegrees >= -15) and (anglexdegrees < angleydegrees):
            display.show(Image.ARROW_E)
        elif (anglexdegrees < -15 and anglexdegrees >= -30) and (anglexdegrees < angleydegrees):
            display.show(medARROW_E)
        elif (anglexdegrees < -30) and (anglexdegrees < angleydegrees):
            display.show(dimARROW_E)
        else:
            pass

        #(0,0,-90) --> level