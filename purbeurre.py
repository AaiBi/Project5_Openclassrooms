#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
MacGyver, maze game
MacGyver must move through a labyrinth to collect items that will allow him to kill the guardian and
finish the game.

files : maze.py, classes_maze.py, constants_maze.py. README.md
folder : ressource, .idea
"""
import json

import requests

from my_classes import Database


def main():
    """main function"""

    menu = input(
        "1 - Quel aliment souhaitez - vous remplacer ?"'\n'
        "2 - Retrouver mes aliments substitués."'\n'
    )

    if menu == "1":
        print("Sélectionnez la catégorie. "'\n')

    elif menu == "2":
        print("deux")


if __name__ == "__main__":
    main()
