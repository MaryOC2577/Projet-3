"""All messages."""


class Messages:
    """Class message."""

    def __init__(self):
        """Init."""
        self.message = ""

    def set_message(self, message):
        """Add."""
        self.message = message

    def get_message(self):
        """Get and clear the messages."""
        msg = self.message
        self.message = ""
        return msg

    def exists(self):
        """Return true if there is a message."""
        return bool(self.message)


messages = Messages()
