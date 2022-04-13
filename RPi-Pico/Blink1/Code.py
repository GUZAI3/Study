#Blink the built-in LED (GP25)
import machine
import utime
led = machine.Pin(25, machine.Pin.OUT)
while True:
    led.value(1)    # LED ON
    utime.sleep(1)  # 1s stop
    led.value(0)    # LED OFF
    utime.sleep(1)  # 1s stop