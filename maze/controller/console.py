"""Controller."""


class InputKeys:
    """Check input keys."""

    def __init__(self):
        """Init keys."""
        self.pressed_key = ""

    def check_keys(self):
        """Check press keys."""
        key = input()
        if key.lower() == "e":
            self.pressed_key = "exit"
        if key.lower() == "q":
            self.pressed_key = "left"
        if key.lower() == "s":
            self.pressed_key = "down"
        if key.lower() == "d":
            self.pressed_key = "right"
        if key.lower() == "z":
            self.pressed_key = "up"
