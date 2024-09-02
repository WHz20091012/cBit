def on_gesture_tilt_left():
    basic.show_leds("""
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        # # # . .
        """)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_logo_touched():
    basic.show_string("All Off")
    I2C_LCD1602.clear()
    I2C_LCD1602.backlight_off()
    I2C_LCD1602.off()
    basic.show_icon(IconNames.YES)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_gesture_logo_down():
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        . . . . .
        . . . . .
        """)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_button_pressed_a():
    basic.show_string("On")
    I2C_LCD1602.clear()
    I2C_LCD1602.on()
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # # #
        # # # # #
        # # # # #
        """)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_ab():
    basic.show_string("All ON")
    I2C_LCD1602.clear()
    I2C_LCD1602.backlight_on()
    I2C_LCD1602.on()
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def TH():
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P1, True, False, True)
    I2C_LCD1602.show_string("Temp:" + ("" + str(dht11_dht22.read_data(dataType.TEMPERATURE)) + "/00"),
        0,
        0)
    I2C_LCD1602.show_string("Hum:" + ("" + str(dht11_dht22.read_data(dataType.HUMIDITY))) + "/00",
        2,
        1)

def on_button_pressed_b():
    basic.show_string("On")
    I2C_LCD1602.clear()
    I2C_LCD1602.backlight_on()
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_tilt_right():
    basic.show_leds("""
        . . # # #
        . . # # #
        . . # # #
        . . # # #
        . . # # #
        """)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

basic.show_icon(IconNames.HOUSE)
I2C_LCD1602.lcd_init(0)

def on_forever():
    if dht11_dht22.read_data_successful():
        basic.pause(10000)
        TH()
    else:
        TH()
basic.forever(on_forever)
