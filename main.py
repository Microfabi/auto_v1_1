def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.HEART)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    if input.pin_is_pressed(TouchPin.P1):
        servos.P0.run(70)
        servos.P1.run(30)
    elif input.pin_is_pressed(TouchPin.P2):
        servos.P0.run(-70)
        servos.P1.run(-30)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    servos.P0.run(100)
    servos.P1.run(100)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    if input.pin_is_pressed(TouchPin.P1):
        servos.P1.run(30)
        servos.P0.run(70)
    elif input.pin_is_pressed(TouchPin.P2):
        servos.P1.run(-30)
        servos.P0.run(-70)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    servos.P0.run(-100)
    servos.P1.run(-100)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

bluetooth.start_accelerometer_service()
bluetooth.start_button_service()
bluetooth.start_io_pin_service()
bluetooth.start_temperature_service()