# Bubble Scale
# Grant Smith and Emma Whalen
# Instead of arrows we used pixels, this gives a more accurate reading of exactly where you need to move
# the MicroBit to level the scale. If you act as though the dot is a bubble it works the same as a bubble would.


import math
import time
import microbit

while True:
    microbit.display.clear()
    #assign accelerometer values
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    z = microbit.accelerometer.get_z()

    #get squares
    xx = x**2
    yy = y**2
    zz = z**2

    #X Axis
    result_x1 = math.sqrt(yy+zz)
    result_x = x/result_x1
    accel_angle_x = math.atan(result_x)

    #Y Axis
    result_y1 = math.sqrt(xx+zz)
    result_y = y/result_y1
    accel_angle_y = math.atan(result_y)

    x_deg = math.degrees(accel_angle_x)
    y_deg = math.degrees(accel_angle_y)

    #print to REPL
    print((x_deg, y_deg))


    if abs(x_deg) <= 5 and abs(y_deg) <= 5 :
        microbit.display.set_pixel(2, 2, 9)
    elif 5 < x_deg <= 25 and 5 < y_deg <= 25 :
        microbit.display.set_pixel(1, 1, 9)
    elif 25 < x_deg <= 90 and 25 < y_deg <= 90 :
        microbit.display.set_pixel(0, 0, 9)
    elif -5 > x_deg >= -25 and -5 > y_deg >= -25 :
        microbit.display.set_pixel(3, 3, 9)
    elif -25 > x_deg >= -90 and -25 > y_deg >= -90 :
        microbit.display.set_pixel(4, 4, 9)
    elif 5 < x_deg <= 25 and -5 > y_deg >= -25 :
        microbit.display.set_pixel(1, 3, 9)
    elif 25 < x_deg <= 90 and -25 > y_deg >= -90 :
        microbit.display.set_pixel(0, 4, 9)
    elif -5 > x_deg >= -25 and 5 < y_deg <= 25 :
        microbit.display.set_pixel(3, 1, 9)
    elif -25 > x_deg >= -90 and 25 < y_deg <= 90 :
        microbit.display.set_pixel(4, 0, 9)
    elif 5 < x_deg < 25:
        microbit.display.set_pixel(1,2,9)
    elif 25 < x_deg < 90:
        microbit.display.set_pixel(0,2,9)
    elif -5 > x_deg > -25:
        microbit.display.set_pixel(3,2,9)
    elif -25 > x_deg > -90:
        microbit.display.set_pixel(4,2,9)
    elif 5 < y_deg < 25:
        microbit.display.set_pixel(2,1,9)
    elif 25 < y_deg < 90:
        microbit.display.set_pixel(2,0,9)
    elif -5 > y_deg > -25:
        microbit.display.set_pixel(2,3,9)
    elif -25 > y_deg > -90:
        microbit.display.set_pixel(2,4,9)

    microbit.sleep(100)