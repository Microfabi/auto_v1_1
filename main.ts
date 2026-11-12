bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.Yes)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.No)
})
input.onButtonPressed(Button.A, function () {
    if (input.pinIsPressed(TouchPin.P1)) {
        servos.P0.run(70)
        servos.P1.run(30)
    } else if (input.pinIsPressed(TouchPin.P2)) {
        servos.P0.run(-70)
        servos.P1.run(-30)
    }
})
input.onPinPressed(TouchPin.P2, function () {
    servos.P1.run(100)
    servos.P0.run(100)
})
input.onButtonPressed(Button.B, function () {
    if (input.pinIsPressed(TouchPin.P1)) {
        servos.P1.run(30)
        servos.P0.run(70)
    } else if (input.pinIsPressed(TouchPin.P2)) {
        servos.P1.run(-30)
        servos.P0.run(-70)
    }
})
input.onPinPressed(TouchPin.P1, function () {
    servos.P0.run(-100)
    servos.P1.run(-100)
})
bluetooth.startAccelerometerService()
bluetooth.startButtonService()
bluetooth.startIOPinService()
bluetooth.startTemperatureService()
