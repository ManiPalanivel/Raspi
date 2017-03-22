import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
#time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()

while GPIO.input(ECHO)==1:
  pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print "Distance:",distance,"cm"

'''

GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

current = GPIO.input(21)
previous = current
def printState(current):
    print '%s' % ('HIGH' if current else 'LOW')
printState(current)
while True:
    current = GPIO.input(21)
    if current != previous:
        printState(current)
    previous = current
    time.sleep(0.1)
    
GPIO.cleanup()
'''
