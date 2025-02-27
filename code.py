"""
blinking LED, but the delayed time between each blink increases

created on: Feb 19
by: Sophie Nguyen
"""
import time
import board
import digitalio

#variables
led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT
blink_time = 1

# loop
while True:
    #turns on LED
    led.value = True
    #wait 
    time.sleep(blink_time)
    #turns LED off
    led.value = False
    time.sleep(blink_time)

    #blink time increases by 1 second
    blink_time += 1