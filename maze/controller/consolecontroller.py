"""Controller."""

from maze.model.message import messages


class InputKeysCli:
    """Check input keys."""

    def __init__(self):
        """Init keys."""
        self.pressed_key = ""

    def check_keys(self):
        """Check press keys."""
        possible_keys = {
            "e": "exit",
            "q": "left",
            "s": "down",
            "d": "right",
            "z": "up",
        }
        key = input().lower()
        if key not in possible_keys:
            messages.set_message("Invalid key !")
            self.pressed_key = ""
            return
        self.pressed_key = possible_keys[key]
