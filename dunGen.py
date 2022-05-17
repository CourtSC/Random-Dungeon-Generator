#! python 3 - dunGen.py - a program to generate random dungeons according to the rules for D&D 5e in the Dungeon Master's Guide

from random import randint

horzBorder = ' ------ '
vertBorder = '|      |'

def tile(rows, cols):
    print(horzBorder * rows)
    print(vertBorder * rows)
    print(vertBorder * rows)
    print(horzBorder * rows)
    for col in range(cols-1):
        # print(horzBorder * rows)
        print(vertBorder * rows)
        print(vertBorder * rows)
        print(horzBorder * rows)

tile(randint(1,5),randint(1,5))