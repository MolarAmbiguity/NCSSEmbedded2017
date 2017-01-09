from microbit import *
import math

display.off()
wave = []
strings = [
    '00000000000000000000',
    '00000000000000000000',
    '10000000000000000000',
    '01000000000000000000',
    '00100000000000000000',
    '00010000000000000000',
    '00001000000010000000',
    '00000100000100000000',
    '00000010001000000000',
    '00000001110000000000',
    ]
    
for row in strings:
  for count, col in enumerate(row):
    if col == '1':
       #print(col)
       wave.append(255 // (count + 1))

pins = [pin7, pin6, pin5, pin4, pin3, pin2, pin1, pin0]

while True:
    for point in wave:
        print(point)
        for pin in pins:
          pin.write_digital(point & 1)
          point >>= 1
         