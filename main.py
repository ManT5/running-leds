def _2():
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P12, 1)
    basic.pause(140)
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.digital_write_pin(DigitalPin.P11, 1)
    basic.pause(140)
    pins.digital_write_pin(DigitalPin.P11, 0)
    pins.digital_write_pin(DigitalPin.P10, 1)
    basic.pause(140)
    pins.digital_write_pin(DigitalPin.P10, 0)
    pins.digital_write_pin(DigitalPin.P9, 1)
    basic.pause(140)
    pins.digital_write_pin(DigitalPin.P9, 0)
    pins.digital_write_pin(DigitalPin.P8, 1)
    basic.pause(140)

def on_button_pressed_a():
    global stanje
    stanje = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def _3():
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P9, 0)
    pins.digital_write_pin(DigitalPin.P10, 0)
    pins.digital_write_pin(DigitalPin.P11, 0)
    pins.digital_write_pin(DigitalPin.P12, 0)
    basic.pause(100)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P9, 1)
    pins.digital_write_pin(DigitalPin.P10, 1)
    pins.digital_write_pin(DigitalPin.P11, 1)
    pins.digital_write_pin(DigitalPin.P12, 1)
    basic.pause(100)

def on_button_pressed_ab():
    global stanje
    stanje = 3
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global stanje
    stanje = 2
input.on_button_pressed(Button.B, on_button_pressed_b)

def start():
    global stanje
    led.enable(False)
    stanje = 0
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P9, 1)
    pins.digital_write_pin(DigitalPin.P10, 1)
    pins.digital_write_pin(DigitalPin.P11, 1)
    pins.digital_write_pin(DigitalPin.P12, 1)
    basic.pause(1000)
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P9, 0)
    pins.digital_write_pin(DigitalPin.P10, 0)
    pins.digital_write_pin(DigitalPin.P11, 0)
    pins.digital_write_pin(DigitalPin.P12, 0)
def _1():
    pins.digital_write_pin(DigitalPin.P12, 0)
    pins.digital_write_pin(DigitalPin.P8, 1)
    basic.pause(140)
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P9, 1)
    basic.pause(140)
    pins.digital_write_pin(DigitalPin.P9, 0)
    pins.digital_write_pin(DigitalPin.P10, 1)
    basic.pause(140)
    pins.digital_write_pin(DigitalPin.P10, 0)
    pins.digital_write_pin(DigitalPin.P11, 1)
    basic.pause(140)
    pins.digital_write_pin(DigitalPin.P11, 0)
    pins.digital_write_pin(DigitalPin.P12, 1)
    basic.pause(140)
stanje = 0
start()

def on_forever():
    if stanje == 1:
        _1()
    if stanje == 2:
        _2()
    if stanje == 3:
        _3()
basic.forever(on_forever)
