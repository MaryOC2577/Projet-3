"""Accéder à une liste dans une liste."""

LISTE = [
    ["t", "y", "j"],
    ["u", "i", "o"],
    ["s", "i", "p"],
]

for i in range(0, 3):
    for x in range(0, 3):
        print(LISTE[i][x], "est en position :", i, ":", x)
