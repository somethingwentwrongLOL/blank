from gpiozero import MotionSensor
import os
import time
pir = MotionSensor(4)
time.sleep(3)
if pir.motion_detected:
    print("motion detected")
    
    os.system("fswebcam -F 3 --fps 20 -r 1200*800 /home/pi/Desktop/csea2.jpg")
    print("intruder alert")
else:
    print("nothing new")

