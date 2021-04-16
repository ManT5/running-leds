function _2 () {
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P12, 1)
    basic.pause(140)
    pins.digitalWritePin(DigitalPin.P12, 0)
    pins.digitalWritePin(DigitalPin.P11, 1)
    basic.pause(140)
    pins.digitalWritePin(DigitalPin.P11, 0)
    pins.digitalWritePin(DigitalPin.P10, 1)
    basic.pause(140)
    pins.digitalWritePin(DigitalPin.P10, 0)
    pins.digitalWritePin(DigitalPin.P9, 1)
    basic.pause(140)
    pins.digitalWritePin(DigitalPin.P9, 0)
    pins.digitalWritePin(DigitalPin.P8, 1)
    basic.pause(140)
}
input.onButtonPressed(Button.A, function () {
    stanje = 1
})
function _3 () {
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P9, 0)
    pins.digitalWritePin(DigitalPin.P10, 0)
    pins.digitalWritePin(DigitalPin.P11, 0)
    pins.digitalWritePin(DigitalPin.P12, 0)
    basic.pause(100)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P9, 1)
    pins.digitalWritePin(DigitalPin.P10, 1)
    pins.digitalWritePin(DigitalPin.P11, 1)
    pins.digitalWritePin(DigitalPin.P12, 1)
    basic.pause(100)
}
input.onButtonPressed(Button.AB, function () {
    stanje = 3
})
input.onButtonPressed(Button.B, function () {
    stanje = 2
})
function start () {
    led.enable(false)
    stanje = 0
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P9, 1)
    pins.digitalWritePin(DigitalPin.P10, 1)
    pins.digitalWritePin(DigitalPin.P11, 1)
    pins.digitalWritePin(DigitalPin.P12, 1)
    basic.pause(1000)
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P9, 0)
    pins.digitalWritePin(DigitalPin.P10, 0)
    pins.digitalWritePin(DigitalPin.P11, 0)
    pins.digitalWritePin(DigitalPin.P12, 0)
}
function _1 () {
    pins.digitalWritePin(DigitalPin.P12, 0)
    pins.digitalWritePin(DigitalPin.P8, 1)
    basic.pause(140)
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P9, 1)
    basic.pause(140)
    pins.digitalWritePin(DigitalPin.P9, 0)
    pins.digitalWritePin(DigitalPin.P10, 1)
    basic.pause(140)
    pins.digitalWritePin(DigitalPin.P10, 0)
    pins.digitalWritePin(DigitalPin.P11, 1)
    basic.pause(140)
    pins.digitalWritePin(DigitalPin.P11, 0)
    pins.digitalWritePin(DigitalPin.P12, 1)
    basic.pause(140)
}
let stanje = 0
start()
basic.forever(function () {
    if (stanje == 1) {
        _1()
    }
    if (stanje == 2) {
        _2()
    }
    if (stanje == 3) {
        _3()
    }
})
