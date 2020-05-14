"""test parcours d'un fichier txt, récupération de la position du caractère."""
from pathlib import Path

BASE_DIR = Path(".").resolve()
MAZE_DIR = BASE_DIR / "maze"
DATA_DIR = MAZE_DIR / "data"

FILEM = DATA_DIR / "maze1.txt"
LISTF = []

with open(FILEM, "r") as file:
    content = file.read()

# charger la première ligne dans une liste
for line in content:
    LISTF.append(line)

print(len(LISTF))

LISTA = []
COUNTER = 0
print("  ", end="")
for x in range(0, 239):
    if COUNTER == 14:
        print("\n")
        print(" ", LISTF[x], " ", end="")
        COUNTER += 1
    else:
        print(LISTF[x], " ", end="")
print("\n")
