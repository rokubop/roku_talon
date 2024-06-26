from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()

mod.tag("parrot_side_b", desc="Tag for side B version of default parrot mode")

ctx.matches = r"""
tag: user.parrot_side_b
"""

# @ctx.action_class("user")
# class ParrotCommands:
#     def parrot_cluck():
#         actions.user.parrot_side_b_disable()
#         actions.user.parrot_mode_disable()
#     def parrot_pop(): actions.user.parrot_mouse_click(0, 2)
#     def parrot_palate(): actions.core.repeat_phrase()
#     def parrot_ah():
#         actions.user.parrot_set_modifier("ctrl")
#         actions.user.parrot_mouse_drag(0)
#     def parrot_oh():
#         actions.user.parrot_set_modifier("shift")
#         actions.user.parrot_mouse_drag(2)
#     def parrot_t(): actions.user.kingfisher_parrot_trigger_virtual_key()
#     def parrot_nn(): actions.user.parrot_side_b_disable()
    # def parrot_eh(): actions.user.parrot_position_mode_enable()
    # def parrot_eh(): actions.user.parrot_teleport_mouse_soft()
    # def parrot_ee(): actions.user.parrot_mouse_and_scroll_stop()
    # def parrot_guh(): actions.user.parrot_run_flex_macro()
    # def parrot_tut(): actions.key("escape")
    # def parrot_er(): actions.user.parrot_rpg_mouse_mode_enable()
    # def parrot_hiss(): actions.user.parrot_scroll_down()
    # def parrot_hiss_stop(): actions.user.parrot_scroll_stop_soft()
    # def parrot_shush(): actions.user.parrot_scroll_up()
    # def parrot_shush_stop(): actions.user.parrot_scroll_stop_soft()

tags = []
tag_source = None

@mod.action_class
class Actions:
    def parrot_side_b_source_tag() -> str:
        """Return the source tag for side b"""
        global tag_source
        return tag_source

    def parrot_side_b_enable():
        """Enable parrot side B mode"""
        global tags, tag_source
        print("parrot side B mode enabled")
        tags = actions.user.parrot_mode_get_tags()
        tag_source = tags[0]
        for t in tags:
            if t != settings.get("user.parrot_default_tag"):
                actions.user.parrot_mode_remove_tag(t)
        actions.user.parrot_mode_append_tag("user.parrot_side_b")

        # actions.user.parrot_teleport_mouse_soft()
        actions.user.add_color_cursor("FF00FF")

    def parrot_side_b_disable():
        """Disable parrot side B mode"""
        print("parrot side B mode disable")
        actions.user.parrot_mode_remove_tag("user.parrot_side_b")
        if actions.user.parrot_mode_get_tags() == []:
            actions.user.clear_screen_regions()
            # actions.user.add_red_cursor()
            actions.user.parrot_mode_reset_tags()
        actions.user.parrot_set_cursor_color()