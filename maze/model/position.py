"""Class position."""


class Position:
    """Calculate position."""

    def __init__(self):
        """Constructor."""

    def items_position(self, item, listmaze):
        """Items position."""
        for line in range(0, 15):
            for char in range(0, 15):
                if listmaze[line][char] == item:
                    item_position = (line, char)
                    return item_position
