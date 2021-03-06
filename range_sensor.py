import RPi.GPIO as GPIO
import time

TRIG = 16 #23 
ECHO = 18 #24
GPIO.setmode(GPIO.BOARD)

def range_init():
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, False)

def get_dist():
    time.sleep(2)

    # Send pulse
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

if __name__ == "__main__":
    range_init()
    while 1:
        print(get_dist())



