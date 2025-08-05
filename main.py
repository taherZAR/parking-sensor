import machine
from machine import Pin
from time import sleep, ticks_us, ticks_diff


ECHO = Pin(2, Pin.IN)   
TRIG = Pin(5, Pin.OUT)    
Buzzer = Pin(15, Pin.OUT) 
Pbutton = Pin(32, Pin.IN, Pin.PULL_UP)  
led = Pin(21, Pin.OUT)      

DISTANCE_THRESHOLD = 20 
alarm_active = False

def time_pulse_us(pin, pulse_level, timeout_us=30000):
    t0 = ticks_us()
    while pin.value() != pulse_level:
        if ticks_diff(ticks_us(), t0) > timeout_us:
            return -1
    
    t0 = ticks_us()
    while pin.value() == pulse_level:
        if ticks_diff(ticks_us(), t0) > timeout_us:
            return -1
    
    return ticks_diff(ticks_us(), t0)

def measure_distance():
    TRIG.value(0)
    sleep(0.01)
    TRIG.value(1)
    sleep(0.00001)
    TRIG.value(0)
    
    pulse_duration = time_pulse_us(ECHO, 1, 30000)
    if pulse_duration < 0:
        return float('inf')
    return (pulse_duration / 2) / 29.1

while True:
    distance = measure_distance()
    print("Distance:", distance, "cm")

    if distance < DISTANCE_THRESHOLD and not alarm_active:
        Buzzer.on()
        led.on()
        alarm_active = True

    if alarm_active and Pbutton.value() == 0:
        Buzzer.off()
        led.off()
        alarm_active = False
        print("Alarm stopped")

    sleep(0.2)