input.onGesture(Gesture.TiltLeft, function () {
    basic.showLeds(`
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        `)
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    basic.showString("All Off")
    I2C_LCD1602.clear()
    I2C_LCD1602.BacklightOff()
    I2C_LCD1602.off()
    basic.showIcon(IconNames.Yes)
})
input.onGesture(Gesture.LogoDown, function () {
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        . . . . .
        . . . . .
        `)
})
input.onButtonPressed(Button.A, function () {
    basic.showString("On")
    I2C_LCD1602.clear()
    I2C_LCD1602.on()
    basic.showIcon(IconNames.Yes)
})
input.onGesture(Gesture.LogoUp, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # # #
        # # # # #
        # # # # #
        `)
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("All ON")
    I2C_LCD1602.clear()
    I2C_LCD1602.BacklightOn()
    I2C_LCD1602.on()
    basic.showIcon(IconNames.Yes)
})
function TH () {
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P1,
    true,
    false,
    true
    )
    I2C_LCD1602.ShowString("Temp:" + ("" + dht11_dht22.readData(dataType.temperature) + "/00"), 0, 0)
    I2C_LCD1602.ShowString("Hum:" + ("" + dht11_dht22.readData(dataType.humidity)) + "/00", 2, 1)
}
input.onButtonPressed(Button.B, function () {
    basic.showString("On")
    I2C_LCD1602.clear()
    I2C_LCD1602.BacklightOn()
    basic.showIcon(IconNames.Yes)
})
input.onGesture(Gesture.TiltRight, function () {
    basic.showLeds(`
        . . # # #
        . . # # #
        . . # # #
        . . # # #
        . . # # #
        `)
})
let red = 0
basic.showIcon(IconNames.House)
I2C_LCD1602.LcdInit(0)
basic.forever(function () {
    if (dht11_dht22.readDataSuccessful()) {
        basic.pause(10000)
        TH()
    } else {
        TH()
    }
})
basic.forever(function () {
    red = 0
    for (let index = 0; index < 60; index++) {
    	
    }
})
