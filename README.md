# HX711 driver library [Depreciated]

## Description

This library allows to drive a HX711 load cess amplifier with a Raspberry Pi by using `gpiozero` library.

- to set channel and gain
- to read raw value

*This package requires `gpiozero` to be installed in Python 3.*

## Example

```py
  
from hx711_gpiozero import HX711
from time import sleep

spi = HX711()
print("Initiating ...")
init_reading = spi.value

sleep(1)
input("Put a known mass on the scale, then press `enter`.")

try:
    rel_weight = float(input("What is the weight of the known mass?\n"))
except ValueError as err:
    print(err)
    print("(The input of weight can only be numbers)")
    exit(1)
rel_reading = spi.value
scale_ratio = rel_weight / (rel_reading - init_reading)

sleep(1)
while True:
    weight = (spi.value - init_reading) * scale_ratio
    print(weight)
    sleep(1)
```
