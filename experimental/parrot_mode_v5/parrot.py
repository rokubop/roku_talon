
from talon import Module, actions, cron, Context
from datetime import datetime
import time
from ...plugin.debouncer import Debouncer

mod = Module()
ctx = Context()

two_way_opposites = [
    ("north", "south"),
    ("upper", "downer"),
    ("up", "down"),
    ("left", "right"),
    ("push", "tug"),
    ("drain", "step"),
    ("undo", "redo"),
    ("last", "next"),
    ("forward", "back"),
    ("out", "in"),
    # tab and shift tab
]

# ss_debounce_time = "20ms"
ss_debounce_time = "100ms"

state = {}
cron_jobs = {}
callbacks = {}
shush_start: float = 0
opposites = {}

for key, value in two_way_opposites:
    opposites[key] = value
    opposites[value] = key

last_tut = ""
last_palete = ""


class StateReverse:
    def __init__(self):
        self.is_reverse_active = False
        self.timer_handle = None

    def activate_reverse(self):
        self.is_reverse_active = True
        if self.timer_handle:
            cron.cancel(self.timer_handle)
        self.timer_handle = cron.after("2s", self.deactivate_reverse)

    def deactivate_reverse(self):
        self.is_reverse_active = False
        self.timer_handle = None

    def is_active(self):
        return self.is_reverse_active

stateReverse = StateReverse()

shush_debouncer = Debouncer(500, actions.user.noise_shush_start, actions.user.noise_shush_stop)
hiss_debouncer = Debouncer(300, actions.user.noise_hiss_start, actions.user.noise_hiss_stop)
ee_debouncer = Debouncer(200, actions.user.noise_ee_start, actions.user.noise_ee_stop)
oo_debouncer = Debouncer(200, actions.user.noise_oo_start, actions.user.noise_oo_stop)
# shush_debouncer.start()

palate_mode = "repeater"

@mod.action_class
class Actions:
    def palate_mode_toggle():
        """Toggle palate mode"""
        global palate_mode
        if palate_mode == "repeater":
            palate_mode = "ax"
        else:
            palate_mode = "repeater"

    def toggleScrollSpeed():
        """Toggle scroll speed"""
        global ss_debounce_time
        if ss_debounce_time == "40ms":
            print("setting speed to 120ms")
            actions.user.hud_publish_mouse_particle('float_up', '0000FF')
            ss_debounce_time = "120ms"
        else:
            print("setting speed to 40ms")
            actions.user.hud_publish_mouse_particle('float_up', 'FF0000')
            ss_debounce_time = "40ms"

    def on_palate():
        """Repeat or wake up."""
        global last_palete, last_tut, palate_mode

        if (actions.speech.enabled()):
            if palate_mode != "repeater":
                actions.user.fluent_search_show_labels_window()
                return

            if (stateReverse.is_active() and last_tut):
                last_command = actions.user.history_get(0)
                for word in opposites:
                    if word in last_command:
                        if last_palete and last_palete in last_command:
                            actions.mimic(last_command)
                            last_tut = ""
                        else:
                            oppositePhrase = last_command.replace(word, opposites[word])
                            last_palete = oppositePhrase
                            actions.mimic(oppositePhrase)
                            last_tut = ""
                        return
                last_palete = ""
            else:
                actions.core.repeat_command()

            stateReverse.activate_reverse()


    def on_tut():
        """Reverse the last command"""
        global last_tut, last_palete

        actions.user.cancel_repeat_repeatedly()

        if (actions.speech.enabled() and stateReverse.is_active()):
            last_command = actions.user.history_get(0)
            stateReverse.activate_reverse()
            for word in opposites:
                if word in last_command:
                    if last_tut and last_tut in last_command:
                        actions.mimic(last_command)
                        last_palete = ""
                    else:
                        oppositePhrase = last_command.replace(word, opposites[word])
                        last_tut = oppositePhrase
                        actions.mimic(oppositePhrase)
                        last_palete = ""
                    return
            last_tut = ""

    def on_pop():
        """Do pop"""
        if actions.user.parrot_mode_is_disabled_permanent():
            return

        actions.user.mouse_scroll_stop()
        if actions.user.mouse_is_dragging():
            actions.user.mouse_drag_end()
        else:
            actions.user.click()

    def on_shush_start():
        """Do shush start"""
        shush_debouncer.start()

    def on_shush_stop():
        """Do shush stop"""
        shush_debouncer.stop()

    def on_hiss_start():
        """Do hiss start"""
        hiss_debouncer.start()

    def on_hiss_stop():
        """Do hiss stop"""
        hiss_debouncer.stop()

    def on_oo_start():
        """Do oo start"""
        oo_debouncer.start()

    def on_oo_stop():
        """Do oo stop"""
        oo_debouncer.stop()

    def on_force_scroll_stop():
        """Do force scroll stop"""
        hiss_debouncer.force_stop()
        shush_debouncer.force_stop()

    def on_ee_start():
        """Do ee start"""
        ee_debouncer.start()
        # actions.user.noise_debounce("ee", True)

    def on_ee_stop():
        """Do ee stop"""
        ee_debouncer.stop()
        # actions.user.noise_debounce("ee", False)

    def on_cluck():
        """Do cluck"""
        actions.skip()

    def on_aa():
        """Do aa"""
        actions.skip()

    def on_ah():
        """Do ah"""
        actions.skip()

    def on_ch():
        """Do ch"""
        actions.skip()

    def on_eh():
        """Do eh"""
        actions.skip()

    def on_oh():
        """Do oh"""
        actions.skip()

    def on_short_oo():
        """Do short_oo"""
        actions.skip()

    def on_uh():
        """Do uh"""
        actions.skip()

    def on_jj():
        """Do jj"""
        actions.skip()

    def on_er():
        """Do er"""
        actions.skip()

    def on_guh():
        """Do guh"""
        actions.skip()

    def on_nn():
        """Do nn"""
        actions.skip()

    def noise_debounce(name: str, active: bool):
        """Start or stop continuous noise using debounce"""
        global ss_debounce_time
        if name not in state:
            state[name] = active
            cron_jobs[name] = cron.after(ss_debounce_time, lambda: callback(name))
        elif state[name] != active:
            cron.cancel(cron_jobs[name])
            state.pop(name)

    def noise_shush_start():
        """Noise shush started"""
        print("shush:start")

    def noise_shush_stop():
        """Noise shush stopped"""
        print("shush:stop")

    def noise_hiss_start():
        """Noise hiss started"""
        print("hiss:start")

    def noise_hiss_stop():
        """Noise hiss stopped"""
        print("hiss:stop")

    def noise_ee_start():
        """Noise ee started"""
        print("ee:start")

    def noise_ee_stop():
        """Noise ee stopped"""
        print("ee:stop")

    def noise_oo_start():
        """Noise oo started"""
        print("oo:start")

    def noise_oo_stop():
        """Noise oo stopped"""
        print("oo:stop")

def callback(name: str):
    active = state.pop(name)
    callbacks[name](active)

def on_shush(active: bool):
    if active:
        actions.user.noise_shush_start()
    else:
        actions.user.noise_shush_stop()

def on_hiss(active: bool):
    if active:
        actions.user.noise_hiss_start()
    else:
        actions.user.noise_hiss_stop()

def on_ee(active: bool):
    if active:
        actions.user.noise_ee_start()
    else:
        actions.user.noise_ee_stop()

def on_oo(active: bool):
    if active:
        actions.user.noise_oo_start()
    else:
        actions.user.noise_oo_stop()

callbacks["ch"] = on_shush
callbacks["shush"] = on_shush
callbacks["hiss"] = on_hiss
callbacks["ee"] = on_ee
callbacks["oo"] = on_oo