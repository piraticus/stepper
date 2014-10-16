import Adafruit_BBIO.GPIO as GPIO
import time

class Stepper:
    def __init__(self, name, a, aPrime, b, bPrime):
        self.name = name
        self.pinsF = [a, b, aPrime, bPrime]
        self.pinsR = [b, a, bPrime, aPrime]
        for pin in self.pinsF:
            GPIO.setup(pin, GPIO.OUT)

    def allOff(self):
        for i in self.pinsF:
            GPIO.output(i, GPIO.LOW)
    
    def lastPin(self, list):
        for i in range(len(list)-1):
            GPIO.output(list[i], GPIO.LOW)
    
    def oneStep(self, pins):
            for i in range(len(pins)):
                if i >= 2:
                    GPIO.output(pins[i-2], GPIO.LOW)
                GPIO.output(pins[i], GPIO.HIGH)
                if i == 1:
                    GPIO.output(pins[3], GPIO.LOW)
                time.sleep(.001)
    
    def step(self, steps):
        allOff()
        for i in range(abs(steps)):
            if steps >= 0:
                oneStep(self.pinsF)
                lastPin(self.pinsF)
            elif steps < 0:
                oneStep(self.pinsR)
                lastPin(self.pinsR)
            time.sleep(.01)
    
        allOff()
