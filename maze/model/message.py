"""All messages."""


class Messages:
    """Class message."""

    def __init__(self):
        """Init."""
        self.messages = []

    def __iter__(self):
        for message in self.messages:
            yield message

    def add_message(self, message):
        """Add."""
        self.messages.append(message)

    def clear_message(self):
        """Clear."""
        self.messages = []


messages = Messages()
