#!/usr/bin/env python


import RPi.GPIO as GPIO
import time
import random


VERDE=17
ROJO=22
AMARILLO=11

colores = [VERDE, ROJO, AMARILLO]

GPIO.setmode(GPIO.BCM)
GPIO.setup(VERDE,GPIO.OUT)
GPIO.setup(ROJO,GPIO.OUT)
GPIO.setup(AMARILLO,GPIO.OUT)

GPIO.output(ROJO, GPIO.HIGH)
GPIO.output(VERDE, GPIO.HIGH)
GPIO.output(AMARILLO, GPIO.HIGH)

time.sleep(0.5)

try:
    while True:
        rnd_color = colores[random.randint(0,2)]
        status = GPIO.input(rnd_color)
        GPIO.output(rnd_color, not status)
        time.sleep(0.05)
except:
    GPIO.output(ROJO, GPIO.HIGH)
    GPIO.output(VERDE, GPIO.HIGH)
    GPIO.output(AMARILLO, GPIO.HIGH)

    time.sleep(0.5)

    GPIO.output(ROJO, GPIO.LOW)
    GPIO.output(VERDE, GPIO.LOW)
    GPIO.output(AMARILLO, GPIO.LOW)








