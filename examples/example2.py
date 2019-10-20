from hx711_gpiozero import HX711
from statistics import mean, median
from time import sleep

spi = HX711()


def get_values(times):
    values = []
    for _ in range(times):
        values.append(spi.value)
        sleep(0.1)  # wait for data ready
    return values


values = get_values(10)
print("data: ", values)
print("mean: ", mean(values))
print("median: ", median(values))
