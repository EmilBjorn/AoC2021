# -*- coding: iso-8859-1 -*-


def parse(input):
    with open(input) as file:
        coords = file.readlines()


# parse lines (done).
# then parse each line into dict {x1 = ..., y1 = ..., x2 = ..., y2 = ...}
