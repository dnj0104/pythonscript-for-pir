from gpiozero import MotionSensor
from signal import pause
import time
from subprocess import run

pir = MotionSensor(7)
def motion_function():
    print("Motion Detected")
    run('vcgencmd display_power 1', shell=True)
    time.sleep(30)

def no_motion_function():
    print("Motion stopped")
    run('vcgencmd display_power 0', shell=True)
    time.sleep(1) 

pir.when_motion = motion_function
pir.when_no_motion = no_motion_function

pause()
