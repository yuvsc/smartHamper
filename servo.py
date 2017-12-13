import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

def servo_init(freq1=50, freq2=50):
    GPIO.setup(03, GPIO.OUT)
    GPIO.setup(05, GPIO.OUT)

    # GPIO.PWM(<pin>,<freq>)
    pwm1=GPIO.PWM(03,freq1)
    pwm2=GPIO.PWM(05,freq2)

    pwm1.start(0)
    pwm2.start(0)

    setAngle(90,pwm2)
    setAngle(90,pwm1)

    return pwm1, pwm2

def moveLaundry(clss, pwm1, pwm2):
    if clss == 0:
        setAngle(120, pwm1)
    elif clss == 1:
        setAngle(110, pwm2)
    elif clss == 2:
        setAngle(40, pwm1)

    # Reset postion
    sleep(1)
    setAngle(90, pwm1)
    setAngle(80, pwm2)

def setAngle(angle,pwm):
    duty = angle / 18 + 2
    GPIO.output(03,True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)

def reset_servo():
    pwm1, pwm2 = servo_init()

    setAngle(90,pwm2)
    setAngle(90,pwm1)


if __name__ == '__main__':
    reset_servo()
