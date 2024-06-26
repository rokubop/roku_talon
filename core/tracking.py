from talon import Module, actions

mod = Module()

gaze = False
head = False
last_gaze = False
last_head = False

@mod.action_class
class Actions:
    def tracking_control_gaze_toggle(value: bool):
        """Toggle gaze tracking"""
        global gaze, last_gaze
        last_gaze = gaze
        if (value == True and not actions.tracking.control_enabled()):
            actions.tracking.control_toggle(True)
        actions.tracking.control_gaze_toggle(value)
        gaze = value

    def tracking_control_head_toggle(value: bool):
        """Toggle head tracking"""
        global head, last_head
        last_head = head
        if (value == True and not actions.tracking.control_enabled()):
            actions.tracking.control_toggle(True)
        actions.tracking.control_head_toggle(value)
        head = value

    def tracking_control_pause():
        """Pause tracking"""
        actions.user.tracking_control_head_toggle(False)
        actions.user.tracking_control_gaze_toggle(False)

    def tracking_control_resume():
        """Resume tracking"""
        actions.user.tracking_control_head_toggle(last_head)
        actions.user.tracking_control_gaze_toggle(last_gaze)

    def tracking_control_gaze_enabled():
        """Return gaze value"""
        return gaze

    def tracking_control_head_enabled():
        """Return head value"""
        return head

    def tracking_control_is_moving():
        """Return is_moving value"""
        return gaze or head

    def tracking_control_was_moving():
        """Return is_moving value"""
        return last_gaze or last_head


