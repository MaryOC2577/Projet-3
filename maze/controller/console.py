"""Controller."""

from maze.model.position import Position
from maze.model.mymaze import MyMaze


class Moves:
    """Control the Hero's movements.
    move up : "Z"
    move down : "S"
    move left : "Q"
    move right : "D"
    """

    def hero_move(self):
        """Moves of the hero."""
        hero_move = input().lower()
        if hero_move == "z":
            print("Hero goes up.")
        elif hero_move == "s":
            print("Hero goes down.")
        elif hero_move == "q":
            print("Hero goes left.")
        elif hero_move == "d":
            print("Hero goes right.")
            self.hero_right()

    def hero_right(self):
        """Hero moves up."""
        # vérifier la position du héro
        position = Position()
        # vérifier la case adjacente
        right_case = (position.hero_position()[0], position.hero_position()[1] + 1)
        # si mur le héro ne bouge pas
        print("Hero can't move")
        # si chemin le héro se déplace sur la case
        # si objet (T, N ,E) objet ajouté dans inventaire + héro se déplace sur la case
