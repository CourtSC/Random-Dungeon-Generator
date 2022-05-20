#! python 3 - dunGen.py - a program to generate random dungeons according to the rules for D&D 5e in the Dungeon Master's Guide

from random import randint

# horzBorder = ' ------ '
# vertBorder = '|      |'

# def tile(area):
#     # Define the area
#     rows, cols = area
#     # Print the first row of tiles
#     print(horzBorder * rows)
#     print(vertBorder * rows)
#     print(vertBorder * rows)
#     print(horzBorder * rows)
#     for col in range(cols-1):
#         # The top line of each tile in the row will share the bottom line of the previous row
#         print(vertBorder * rows)
#         print(vertBorder * rows)
#         print(horzBorder * rows)

startingAreaDict = {
    1: {'Shape': 'Square', 'Size': '20x20 ft.', 'Doors': 0, 'Passages': 4}, 
    2: {'Shape': 'Square', 'Size': '20x20 ft.', 'Doors': 2, 'Passages': 3}, 
    3: {'Shape': 'Square', 'Size': '40x40 ft.', 'Doors': 3, 'Passages': 0}, 
    4: {'Shape': 'Rectangle', 'Size': '80x20 ft.', 'Doors': 2, 'Passages': 2},
    5: {'Shape': 'Rectangle', 'Size': '20x40 ft.', 'Doors': 0, 'Passages': 4},
    6: {'Shape': 'Circle', 'Size': '40 ft. diameter', 'Doors': 0, 'Passages': 4},
    7: {'Shape': 'Circle', 'Size': '40 ft. diameter', 'Doors': 0, 'Passages': 4},
    8: {'Shape': 'Square', 'Size': '20x20 ft.', 'Doors': 2, 'Passages': 1, 'Secret': 1},
    9: {'Shape': 'Passage', 'Size': '10 ft. wide', 'Intersection': 'T-shaped'},
    10: {'Shape': 'Passage', 'Size': '10 ft. wide', 'Intersection': '4-way'}
}
startingArea = startingAreaDict[randint(1,len(startingAreaDict))]
for key, value in startingArea.items():
    if value != 0:
        print(f'{key}: {value}')