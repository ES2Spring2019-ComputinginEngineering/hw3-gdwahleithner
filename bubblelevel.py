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
        anglexradians = math.atan2(x, math.sqrt(y ** 2 + z ** 2))           #find angle between x and z axis
        return anglexradians

    def angley_radians(x, y, z):
        angleyradians = math.atan2(y, math.sqrt(x ** 2 + z ** 2))           #find angle between y and z axis
        return angleyradians

    def anglez_radians(x, y, z):
        anglezradians = math.atan2(z, math.sqrt(x ** 2 + y ** 2))           #find angle between x and y axis
        return anglezradians

    while True:
        ax = acceleration_x()           #run function to find acceleration of three axes
        ay = acceleration_y()
        az = acceleration_z()

        anglexradians = anglex_radians(ax, ay, az)          #run function to find three angles of axes
        angleyradians = angley_radians(ay, ay, az)
        anglezradians = anglez_radians(ax, ay, az)

        anglexdegrees = anglexradians * (180 / math.pi)         #angle x, angle y, angle z from radians into degrees
        angleydegrees = angleyradians * (180 / math.pi)
        anglezdegrees = anglezradians * (180 / math.pi)

        sleep(500)
        print((anglexdegrees, angleydegrees, anglezdegrees))    #print angle x, angle y, and angle z for plotting in microbit every 500 ms

        dimARROW_N = Image("00300:03330:30303:00300:00300")     #create dimARROW_N image to display dim arrow on microbit pointing North
        medARROW_N = Image("00600:06660:60606:00600:00600")     #create medARROW_N image to display medium brightness arrow on microbit pointing North

        dimARROW_S = Image("00300:00300:30303:03330:00300")     #create dimARROW_S image to display dim arrow on microbit pointing South
        medARROW_S = Image("00600:00600:60606:06660:00600")     #create dimARROW_S image to display medium brightness arrow on microbit pointing South

        dimARROW_E = Image("00300:00030:33333:00030:00300")     #create dimARROW_E image to display dim arrow on microbit pointing East
        medARROW_E = Image("00600:00060:66666:00060:00600")     #create dimARROW_E image to display medium brightness arrow on microbit pointing East

        dimARROW_W = Image("00300:03000:33333:03000:00300")     #create dimARROW_W image to display dim arrow on microbit pointing West
        medARROW_W = Image("00600:06000:66666:06000:00600")     #create dimARROW_W image to display medium brightness arrow on microbit pointing West


        if (anglexdegrees >= -5 and anglexdegrees <= 5) and (angleydegrees >= -5 and angleydegrees <= 5):
            display.show(Image.HAPPY)   #displays smiley face image if microbit is flat (the tilt of the x axis is greater than or equal to -5
                                        #or less than or equal to 5 degrees and the tilt of the y axis is between -5 and 5 degrees
        elif (angleydegrees > 5 and angleydegrees <= 15) and (angleydegrees > anglexdegrees):
            display.show(Image.ARROW_N) #displays bright arrow pointing north if the y axis tilt is greater than 5 and less than or equal to 5 degrees
                                        #and the y axis tilt is greater than the x axis tilt
        elif (angleydegrees > 15 and angleydegrees <= 30) and (angleydegrees > anglexdegrees):
            display.show(medARROW_N)    #displays medium bright arrow pointing north if the y axis tilt is greater than 15 degrees and less than or equal to 30 degrees
                                        #and the y axis tilt is greater than the x axis tilt
        elif (angleydegrees > 30) and (angleydegrees > anglexdegrees):
            display.show(dimARROW_N)    #displays dim arrow pointing north if the y axis tilt is greater than 30 degrees
                                        #and the y axis tilt is greater than the x axis tilt

        elif (angleydegrees < -5 and angleydegrees >= -15) and (angleydegrees < anglexdegrees):
            display.show(Image.ARROW_S) #displays bright arrow pointing south if the y axis tilt is less than -5 degrees and greater than or equal to -15 degrees
                                        #and the y axis tilt is greater than the x axis tilt
        elif (angleydegrees < -15 and angleydegrees >= -30) and (angleydegrees < anglexdegrees):
            display.show(medARROW_S)    #displays medium bright arrow pointing south if the y axis tilt is less than -15 degrees and greater than or equal to -30 degrees
                                        #and the y axis tilt is greater than the x axis tilt
        elif (angleydegrees < -30) and (angleydegrees < anglexdegrees):
            display.show(dimARROW_S)    #displays dim arrow pointing south if the y axis tilt is less than -30 degrees
                                        #and the y axis tilt is greater than the x axis tilt

        elif (anglexdegrees > 5 and anglexdegrees <= 15) and (anglexdegrees > angleydegrees):
            display.show(Image.ARROW_W) #displays bright arrow pointing west if the x axis tilt is greater than 5 degrees and less than or equal to 15 degrees
                                        #and the x axis tilt is greater than the y axis tilt
        elif (anglexdegrees > 15 and anglexdegrees <= 30) and (anglexdegrees > angleydegrees):
            display.show(medARROW_W)    #displays medium bright arrow pointing west if the x axis tilt is greater than 15 degrees and less than or equal to 30 degrees
                                        #and the x axis tilt is greater than the y axis tilt
        elif (anglexdegrees > 30) and (anglexdegrees > angleydegrees):
            display.show(dimARROW_W)    #displays bright arrow pointing west if the x axis tilt is greater than 30 degrees
                                        #and the x axis tilt is greater than the y axis tilt
        elif (anglexdegrees < -5 and anglexdegrees >= -15) and (anglexdegrees < angleydegrees):
            display.show(Image.ARROW_E) #displays bright arrow pointing east if the x axis tilt is less than -5 degrees and greater than or equal to -15 degrees
                                        #and the x axis tilt is greater than the y axis tilt
        elif (anglexdegrees < -15 and anglexdegrees >= -30) and (anglexdegrees < angleydegrees):
            display.show(medARROW_E)    #displays medium bright arrow pointing east if the x axis tilt is less than -15 degrees and greater than or equal to -30 degrees
                                        #and the x axis tilt is greater than the y axis tilt
        elif (anglexdegrees < -30) and (anglexdegrees < angleydegrees):
            display.show(dimARROW_E)    #displays dim arrow pointing south if the x axis tilt is less than -30 degrees
                                        #and the x axis tilt is greater than the y axis tilt
        else:
            pass