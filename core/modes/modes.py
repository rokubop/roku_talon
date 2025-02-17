from talon import Context, Module, actions, app, speech_system

mod = Module()
ctx_sleep = Context()
ctx_awake = Context()

modes = {
    "presentation": "a more strict form of sleep where only a more strict wake up command works",
}

for key, value in modes.items():
    mod.mode(key, value)

global hard_sleep
hard_sleep = False

@mod.action_class
class Actions:
    def wake_if_not_hard_sleep():
        """Wakes up if hard sleep is not active."""
        if not hard_sleep:
            actions.speech.enable()
            actions.user.hud_publish_mouse_particle('float_up', '36d96a')

    def set_hard_sleep():
        """Sets hard sleep mode."""
        global hard_sleep
        hard_sleep = True

    def unset_hard_sleep():
        """Unsets hard sleep mode."""
        global hard_sleep
        hard_sleep = False

    def toggle_hard_sleep():
        """Toggles hard sleep mode."""
        global hard_sleep
        hard_sleep = not hard_sleep

    def is_hard_sleep():
        """Returns true if hard sleep mode is active."""
        return hard_sleep

    def talon_mode():
        """For windows and Mac with Dragon, enables Talon commands and Dragon's command mode."""
        actions.speech.enable()

        engine = speech_system.engine.name
        # app.notify(engine)
        if "dragon" in engine:
            if app.platform == "mac":
                actions.user.dragon_engine_sleep()
            elif app.platform == "windows":
                actions.user.dragon_engine_wake()
                # note: this may not do anything for all versions of Dragon. Requires Pro.
                actions.user.dragon_engine_command_mode()

    def dragon_mode():
        """For windows and Mac with Dragon, disables Talon commands and exits Dragon's command mode"""
        engine = speech_system.engine.name
        # app.notify(engine)

        if "dragon" in engine:
            # app.notify("dragon mode")
            actions.speech.disable()
            if app.platform == "mac":
                actions.user.dragon_engine_wake()
            elif app.platform == "windows":
                actions.user.dragon_engine_wake()
                # note: this may not do anything for all versions of Dragon. Requires Pro.
                actions.user.dragon_engine_normal_mode()
