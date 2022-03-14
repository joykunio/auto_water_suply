import machine
import utime
sensor_moisto = machine.ADC(0)
conversion_factor = 3 /(65535)
cutoff = 0.9
sensor_pin = machine.Pin(15, machine.Pin.OUT)

while True:
    reading = sensor_moisto.read_u16()
    voltage = reading * conversion_factor
    print(voltage)
    if voltage > cutoff:
        sensor_pin(1)
    else:
        sensor_pin(0)
    
    utime.sleep(1)
