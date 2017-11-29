import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(03, GPIO.OUT)
GPIO.setup(05, GPIO.OUT)

pwm1=GPIO.PWM(03,50)
pwm2=GPIO.PWM(05,50)

pwm1.start(0)
pwm2.start(0)

def SetAngle(angle,pwm):
    duty = angle / 18 + 2
    GPIO.output(03,True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)

SetAngle(0,pwm1)
SetAngle(0,pwm2)

SetAngle(100,pwm1)

SetAngle(100,pwm2)

SetAngle(0,pwm1)
SetAngle(0,pwm2)

pwm1.stop()
pwm2.stop()

GPIO.cleanup()
