from talon import Context, actions, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
os: windows
"""

@mod.action_class
class Actions:
    def window_maximize():
        """Maximize window"""
        # actions.key("alt-space");
        # actions.sleep(300ms);
        # actions.key("x");
        actions.key("win-up")

    def window_minimize():
        """Minimize window"""
        actions.key("win-down")

    def window_restore():
        """Restore window"""
        # actions.key("alt-space");
        # actions.sleep(300ms);
        # actions.key("r");
        actions.key("win-down")

    def app_switch(index: int = 1):
        """Switch to the app at the given index"""
        actions.key("alt:down")
        actions.key(f"tab:{index}")
        actions.sleep("50ms")
        actions.key("alt:up")
        # actions.sleep("300ms")
