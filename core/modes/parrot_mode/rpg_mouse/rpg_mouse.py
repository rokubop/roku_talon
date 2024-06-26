from talon import Module, Context, actions, ctrl, cron, settings
import platform
os = platform.system().lower()

if os.startswith("windows"):
    import win32api, win32con

mod = Module()
ctx = Context()

mod.setting(
    "rpg_mouse_increment_x",
    desc="X increment for rpg mouse mode",
    type=int,
    default=26
)
mod.setting(
    "rpg_mouse_increment_y",
    desc="Y increment for rpg mouse mode",
    type=int,
    default=26
)
mod.setting(
    "rpg_mouse_interaction_axis_y_pos",
    desc="Y position of an interaction bar in the application",
    type=int,
    default=140
)

nav_job = None
direction = (0, 1)

speeds = {"slow": 1, "medium": 5, "fast": 15}
speed_default = "slow"
speed = speeds[speed_default]

def no_op():
    pass

def update_speed(new_speed):
    global speed
    speed = speeds.get(new_speed, speed_default)
    actions.user.on_rpg_mouse_speed_change(new_speed)

def mouse_move_windows(dx: int, dy: int):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(dx * 2), int(dy * 2))

def mouse_move_generic(dx: int, dy: int):
    (x, y) = ctrl.mouse_pos()
    ctrl.mouse_move(x + dx, y + dy)

mouse_move = mouse_move_windows if os.startswith("windows") else mouse_move_generic

def nav_tick():
    global direction
    if direction:
        dx, dy = direction
        mouse_move(dx * speed, dy * speed)

def start_moving(dx, dy):
    global nav_job, direction
    if nav_job:
        cron.cancel(nav_job)
    direction = (dx, dy)
    nav_job = cron.interval("16ms", nav_tick)

@mod.action_class
class RpgMouseActions:
    def rpg_mouse_move_left():
        """Start moving mouse to the left"""
        start_moving(-1, 0)

    def rpg_mouse_move_right():
        """Start moving mouse to the right"""
        start_moving(1, 0)

    def rpg_mouse_move_down():
        """Start moving mouse down"""
        start_moving(0, 1)

    def rpg_mouse_move_up():
        """Start moving mouse up"""
        start_moving(0, -1)

    def rpg_mouse_repeat_dir_by_increment():
        """Repeat previous direction by the increment defined by the settings"""
        increment_x = settings.get("user.rpg_mouse_increment_x")
        increment_y = settings.get("user.rpg_mouse_increment_y")

        dx = direction[0] * increment_x
        dy = direction[1] * increment_y

        if direction:
            mouse_move(dx, dy)

    def rpg_mouse_repeat_reverse_dir_by_increment():
        """Repeat previous direction by the increment defined by the settings"""
        increment_x = settings.get("user.rpg_mouse_increment_x")
        increment_y = settings.get("user.rpg_mouse_increment_y")
        dx = direction[0] * increment_x * -1
        dy = direction[1] * increment_y * -1

        if direction:
            mouse_move(dx, dy)

    def rpg_mouse_move_slow():
        """Move mouse slower"""
        global speed
        update_speed("slow")

    def rpg_mouse_move_fast():
        """Move mouse faster"""
        global speed
        if speed == speeds["slow"]:
            update_speed("medium")
        elif speed == speeds["medium"]:
            update_speed("fast")
        elif speed == speeds["fast"]:
            return

    def rpg_mouse_move_to_interaction_axis():
        """Mouse move to interaction axis"""
        pos = ctrl.mouse_pos()
        y = settings.get("user.rpg_mouse_interaction_axis_y_pos")
        ctrl.mouse_move(pos[0], y)
        actions.user.rpg_mouse_stop()

    def rpg_mouse_stop():
        """Stop moving mouse"""
        global nav_job, direction
        if nav_job:
            cron.cancel(nav_job)

    def rpg_mouse_reset_speed():
        """Reset speed"""
        update_speed(speed_default)

    def on_rpg_mouse_speed_change(speed: str):
        """Event called when speed changes"""
        no_op()


@mod.action_class
class ParrotRpgMouseActions:
    def parrot_rpg_mouse_mode_enable():
        """Enable parrot mouse rpg mode"""
        actions.user.parrot_freeze_mouse()
        actions.user.add_yellow_cursor()
        actions.user.rpg_mouse_stop()
        update_speed(speed_default)
        actions.user.parrot_mode_enable_tag("user.rpg_mouse")

    def parrot_rpg_mouse_mode_disable_full():
        """Disable parrot mouse rpg mode and exit parrot mode"""
        actions.user.rpg_mouse_stop()
        actions.user.clear_screen_regions()
        update_speed(speed_default)
        actions.user.parrot_mode_reset_tags()
        actions.user.parrot_mode_disable()

    def parrot_rpg_mouse_mode_disable():
        """Disable parrot mouse rpg mode"""
        actions.user.rpg_mouse_stop()
        actions.user.clear_screen_regions()
        update_speed(speed_default)
        actions.user.parrot_mode_reset_tags()
        actions.user.parrot_mode_enable()