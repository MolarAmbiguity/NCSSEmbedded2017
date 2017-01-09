from microbit import *
import radio

radio.on()
radio.config(channel = 52)

while True:
    x_axis = accelerometer.get_x()
    y_axis = accelerometer.get_y()
    if x_axis < -500:
        radio.send('left')
        display.show(Image.ARROW_W)
    elif x_axis > 500:
        radio.send('right')
        display.show(Image.ARROW_E)
    elif y_axis > 500:
        radio.send('reverse')
        display.show(Image.ARROW_S)
    elif y_axis < -500:
        radio.send('forward')
        display.show(Image.ARROW_N)
    else:
        radio.send('stop')
        display.clear()
    sleep(6)
    