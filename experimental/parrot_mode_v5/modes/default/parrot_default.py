from talon import Module, Context, actions, settings, ctrl

mod = Module()

ctx = Context()
ctx.matches = """
mode: user.parrot_v5
and mode: user.parrot_v5_default
"""

is_tracking = False

def teleport_and_track_head():
    global is_tracking
    actions.user.parrot_v5_ui_cursor_green()
    if not actions.tracking.control_enabled():
        actions.tracking.control_toggle(True)
    actions.tracking.control_head_toggle(False)
    actions.tracking.control_gaze_toggle(True)
    actions.sleep("50ms")
    actions.tracking.control_gaze_toggle(False)
    actions.tracking.control_head_toggle(True)
    is_tracking = True

def freeze_tracking():
    global is_tracking
    if is_tracking:
        actions.tracking.control_head_toggle(False)
        actions.tracking.control_gaze_toggle(False)
        is_tracking = False
    actions.user.parrot_v5_ui_cursor_red()

@ctx.action_class("user")
class Actions:
    def on_parrot_v5_mode_enable():
        actions.user.parrot_v5_ui_cursor_red()

    def on_parrot_v5_mode_disable():
        actions.user.event_mouse_drag_stop()
        actions.user.parrot_v5_stopper()
        actions.user.event_key_modifier_disable_all()
        actions.user.parrot_v5_ui_clear()

    def on_parrot_v5_mode_disable_soft():
        actions.user.parrot_v5_stopper()

    def on_event_mouse_scroll_start():
        freeze_tracking()

    def on_event_mouse_drag_stop():
        actions.user.parrot_v5_ui_cursor_red()

    def on_event_key_modifier_enabled(key: str):
        print(f"key modifier enabled {key}")
        actions.user.parrot_v5_ui_cursor_mod_enable(key)

    def on_event_key_modifier_disabled(key: str):
        print(f"key modifier disabled {key}")
        actions.user.parrot_v5_ui_cursor_mod_disable(key)


@mod.action_class
class Actions:
    def parrot_v5_click_primary():
        """Click the primary mouse button"""
        if ctrl.mouse_buttons_down():
            actions.user.event_mouse_drag_stop()
        else:
            actions.user.event_mouse_click(0)
        freeze_tracking()

    def parrot_v5_click_alternate():
        """Click the alternate mouse button"""
        if ctrl.mouse_buttons_down():
            actions.user.event_mouse_drag_stop()
        else:
            actions.user.event_mouse_click(1)
        freeze_tracking()

    def parrot_v5_drag_primary():
        """Drag primary mouse"""
        actions.user.parrot_v5_ui_cursor_blue()
        actions.user.event_mouse_drag(0)

    def parrot_v5_scroller_down():
        """Start scrolling down"""
        actions.user.event_mouse_scroll_start("down")

    def parrot_v5_scroller_up():
        """Start scrolling up"""
        actions.user.event_mouse_scroll_start("up")

    def parrot_v5_scroller_stop():
        """Stop scrolling"""
        actions.user.event_mouse_scroll_stop_soft()

    def parrot_v5_stopper():
        """Generic all purpose stopper"""
        global is_tracking
        is_dragging = ctrl.mouse_buttons_down()
        is_scrolling = actions.user.event_mouse_is_scrolling()
        if not is_tracking and not is_dragging and not is_scrolling:
            actions.user.event_key_modifier_disable_all()

        actions.user.event_mouse_scroll_stop_hard()
        freeze_tracking()

    def parrot_v5_positioner():
        """Use cursor/tracking positioning"""
        teleport_and_track_head()

    def parrot_v5_mode_b_enable():
        """Enable secondary mode for example rpg mouse"""
        actions.user.parrot_v5_mode_switch("user.parrot_v5_rpg_mouse")

    def parrot_v5_set_modifier(key: str):
        """Set modifier"""
        actions.user.event_key_modifier_toggle(key)