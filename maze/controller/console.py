"""Controller."""


class InputKeys:
    """Check input keys."""

    def __init__(self):
        """Init keys."""
        self.key_press = ""

    def check_keys(self):
        """Check press keys."""
        key = input()
        if key.lower() == "e":
            self.key_press = "exit"
        if key.lower() == "q":
            self.key_press = "left"
        if key.lower() == "s":
            self.key_press = "down"
        if key.lower() == "d":
            self.key_press = "right"
        if key.lower() == "z":
            self.key_press = "up"
