from talon import actions, ctrl, Module, Context

mod = Module()
mod.tag("pedal_click_mute", desc="click or mute")
ctx = Context()
ctx.matches = "tag: user.pedal_click_mute"

speech_toggle_flag = False

@ctx.action_class("user")
class Actions:
    def pedal_on_tag_enable():
        actions.user.hud_add_log('event', '<*Pedal: Click/Mute />')

    def pedal_left_down():
        ctrl.mouse_click(button=0, down=True)

    def pedal_left_up():
        ctrl.mouse_click(button=0, up=True)

    def pedal_center_down():
        global speech_toggle_flag
        if speech_toggle_flag:
            actions.user.hud_publish_mouse_particle('float_up', '30F343')
            # actions.speech.toggle(True)
            # actions.user.talon_wake()
            actions.sound.set_microphone("Microphone (Yeti X)")
            actions.user.hud_add_log('event', '<*Voice: on/>')
        else:
            # actions.speech.toggle(False)
            actions.user.hud_publish_mouse_particle('float_up', 'ff0000')
            actions.sleep("1s")
            actions.sound.set_microphone("None")
            actions.user.hud_add_log('error', '<*Voice: off />')
            # actions.user.talon_sleep()
        speech_toggle_flag = not speech_toggle_flag

    def pedal_center_up():
        actions.skip()
