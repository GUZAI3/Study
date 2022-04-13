#Turn on the three LEDs in order
import machine
import utime
led1 = machine.Pin(3, machine.Pin.OUT)
led2 = machine.Pin(4, machine.Pin.OUT)
led3 = machine.Pin(5, machine.Pin.OUT)
while True:
    led1.value(1)   # LED1 ON
    led2.value(0)   # LED2 OFF
    led3.value(0)   # LED3 OFF
    utime.sleep(1)  # 1s stop

    led1.value(0)   # LED1 OFF
    led2.value(1)   # LED2 ON
    led3.value(0)   # LED3 OFF
    utime.sleep(1)  # 1s stop
    
    led1.value(0)   # LED1 OFF
    led2.value(0)   # LED2 OFF
    led3.value(1)   # LED3 ON
    utime.sleep(1)  # 1s stop
