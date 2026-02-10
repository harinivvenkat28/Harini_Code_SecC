from machine import Pin
import time

bob = Pin(15, Pin.IN)     
led1 = Pin(12, Pin.OUT)
led2 = Pin(26, Pin.OUT)

while True:
    bob_val = bob.value()   

    if bob_val == 0:      
        led1.on()
        time.sleep(0.3)
        led1.off()
        time.sleep(0.3)

        led2.on()
        time.sleep(0.3)
        led2.off()

    else:                 
        led1.on()
        time.sleep(0.3)
        led1.off()
        time.sleep(0.3)
        led1.on()
        time.sleep(0.3)
        led1.off()
        time.sleep(0.3)

        led2.on()
        time.sleep(0.3)
        led2.off()
        time.sleep(0.3)
        led2.on()
        time.sleep(0.3)
        led2.off()


    time.sleep(0.05)      
