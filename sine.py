from microbit import *
import math

display.off()

x = [i/20 for i in range(0,126)]
sine_wave = [0]*len(x)
for index, value in enumerate(x):
    sine_wave[index] = int(127*(math.sin(value) + 1))
    
pins = [pin7, pin6, pin5, pin4, pin3, pin2, pin1, pin0]

while True:
    for point in sine_wave:
        start_point = point
        for pin in pins:
          pin.write_digital(point & 1)
          point >>= 1
        print(start_point, pin10.read_analog() >> 2)
         