settings():
    user.mouse_move_calibrate_360_x = 617
move right:                 user.mouse_move_delta_ease_out(100, 0)
move left:                  user.mouse_move_delta_ease_out(-100, 0)
move down:                  user.mouse_move_delta_ease_out(0, 100)
move up:                    user.mouse_move_delta_ease_out(0, -100)
move right <number>:        user.mouse_move_delta_ease_out(number * 100, 0)
move left <number>:         user.mouse_move_delta_ease_out(number * -100, 0)
move down <number>:         user.mouse_move_delta_ease_out(0, number * 100)
move up <number>:           user.mouse_move_delta_ease_out(0, number * -100)
move calibrate x <number>:  user.mouse_move_calibrate_360_x(number)
move stop:                  user.mouse_move_stop()
move left ninety:           user.mousem_move_delta_degrees_ease_out(-90, 0)
move left one eighty:       user.mouse_move_delta_degrees_ease_out(-180, 0)
move right ninety:          user.mouse_move_delta_degrees_ease_out(90, 0)
move right one eighty:      user.mouse_move_delta_degrees_ease_out(180, 0)

drag left:                  user.mouse_drag_delta_ease_out(0, -200, 0)
drag right:                 user.mouse_drag_delta_ease_out(0, 200, 0)
drag up:                    user.mouse_drag_delta_ease_out(0, 0, -200)
drag down:                  user.mouse_drag_delta_ease_out(0, 0, 200)
drag stop:                  user.mouse_drag_stop()

middle left:                user.mouse_drag_delta_ease_out(2, -200, 0)
middle right:               user.mouse_drag_delta_ease_out(2, 200, 0)
middle up:                  user.mouse_drag_delta_ease_out(2, 0, -200)
middle down:                user.mouse_drag_delta_ease_out(2, 0, 200)
middle calibrate x <number>: user.mouse_drag_calibrate_360_x(2, number)
middle left ninety:         user.mouse_drag_delta_degrees_ease_out(2, -90, 0)
middle right ninety:        user.mouse_drag_delta_degrees_ease_out(2, 90, 0)
middle right three sixty:   user.mouse_drag_delta_degrees_ease_out(2, 360, 0)
middle right seven twenty:  user.mouse_drag_delta_degrees_ease_out(2, 720, 0)
middle right one eighty:    user.mouse_drag_delta_degrees_ease_out(2, 180, 0)
middle stop:                user.mouse_drag_stop()

start right:                user.mouse_move_constant(2, 0)
start left:                 user.mouse_move_constant(-2, 0)
start up:                   user.mouse_move_constant(0, -2)
start down:                 user.mouse_move_constant(0, 2)
start stop:                 user.mouse_move_stop()

start middle right:         user.mouse_drag_constant(2, 2, 0)
start middle left:          user.mouse_drag_constant(2, -2, 0)
start middle up:            user.mouse_drag_constant(2, 0, -2)
start middle down:          user.mouse_drag_constant(2, 0, -2)

step up:                    user.mouse_move_delta_instant(0, -16)
step down:                  user.mouse_move_delta_instant(0, 16)
step right:                 user.mouse_move_delta_instant(16, 0)
step left:                  user.mouse_move_delta_instant(-16, 0)
