def on_button_pressed_a():
    DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, 40)
    basic.pause(2500)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    basic.pause(500)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, 40)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, 40)
    basic.pause(2500)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)

DFRobotMaqueenPlus.i2c_init()

def on_forever():
    pass
basic.forever(on_forever)
