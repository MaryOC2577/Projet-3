
class Moves:
    """Control the Hero's movements.
    move up : "Z"
    move down : "S"
    move left : "Q"
    move right : "D"
    """

    def hero_move(self):
        """Moves of the hero."""
        hero_move = input()
        if hero_move == "Z":
            print("Hero goes up.")
        elif hero_move == "S":
            print("Hero goes down.")
        elif hero_move == "Q":
            print("Hero goes left.")
        elif hero_move == "D":
            print("Hero goes right.")
