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
