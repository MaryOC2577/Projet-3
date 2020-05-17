"""Test parcours d'un fichier txt, récupération de la position du caractère."""

from pathlib import Path

BASE_DIR = Path(".").resolve()
MAZE_DIR = BASE_DIR / "maze"
DATA_DIR = MAZE_DIR / "data"

FILEM = DATA_DIR / "maze1.txt"

LISTTEST = []
with open(FILEM, "r") as file:
    LISTTEST = file.read().splitlines()

for X in range(0, 15):
    for Y in range(0, 15):
        # print(LISTTEST[X][Y], "est en position :", X, ":", Y)
        if LISTTEST[X][Y] == "S":
            print("Le départ est en position : ", X, ":", Y)
        if LISTTEST[X][Y] == "F":
            print("L'arrivée est en position : ", X, ":", Y)
