print("Hello World")

import machine

machine.reset()

from machine import Pin
pin=Pin(13)
pwm=machine.PWM(pin,freq=0, duty=0)
pwm
help(pwm)
pwm.duty(20)
