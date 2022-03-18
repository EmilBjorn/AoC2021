# -*- coding: iso-8859-1 -*-
# %%
from dataclasses import dataclass, field
from multiprocessing.sharedctypes import Value
from typing import Dict, List


# %%


@dataclass
class Bingoplate:

    rawInput: list = field(repr=False)

    @dataclass
    class Bingonum:
        value: int
        picked: bool

    def __post_init__(self):
        self.number: dict = {}
        for i, row in enumerate(self.rawInput):
            for j, num in enumerate(row):
                self.number[(i, j, 'val')] = num
                self.number[(i, j, 'picked')] = False

    def __str__(self) -> str:
        plate = ""
        for i, row in enumerate(self.rawInput):
            for j, num in enumerate(row):
                plate += num + " "
                # plate[(i,j)] = Bingonum(num,0)
            plate += '\n'
        return plate

    def bingocheck(self):
        # Kode som checker om en plade har bingo et sted
        for i in range(5):
            bingolist = [self.number[i, j, 'picked'] for j in range(5)]
            # print('Bingolist  række ', i, 'er: ', bingolist)
            bingolist = [self.number[j, i, 'picked'] for j in range(5)]
            # print('Bingolist kolonne', i, 'er: ', bingolist)
            if all(bingolist):
                return 'BINGO!!'
        pass


@dataclass
class Deck:
    plates: List[Bingoplate] = field(init=False)

    def __post_init__(self):
        self.plates = []

    def add(self, plate):
        self.plates.append(plate)

# %%


def parse(input):
    with open(input) as f:
        bingonum = f.readline().strip().split(',')

        bingoPlates = Deck()
        plateList = []
        for i, line in enumerate(f):
            if i > 0:
                if line.strip() == "":
                    plate = Bingoplate(plateList)
                    bingoPlates.add(plate)
                    plateList = []
                else:
                    row = line.split()
                    plateList.append(row)

    return bingonum, bingoPlates


def play_bingo(drawn_numbers: list):
    # Kode som gennemgår alle trukkede numre og checker om der er bingo
    #   Skal måske være en metode i Deck klassen.
    pass


# %%
if __name__ == "__main__":
    nums, bingoPlates = parse("day4/input.txt")
    # print(nums)
    # for i in range(3):
    print(bingoPlates.plates[0])
    print(bingoPlates.plates[0].number[0, 1, 'val'])
    print(bingoPlates.plates[0].number[0, 1, 'picked'])
    bingoPlates.plates[0].number[0, 1, 'picked'] = True
    bingoPlates.plates[0].number[0, 2, 'picked'] = True
    bingoPlates.plates[0].number[0, 4, 'picked'] = True
    bingoPlates.plates[0].number[4, 0, 'picked'] = True
    bingoPlates.plates[0].number[1, 2, 'picked'] = True
    bingoPlates.plates[0].number[2, 2, 'picked'] = True
    bingoPlates.plates[0].number[3, 2, 'picked'] = True
    bingoPlates.plates[0].number[4, 2, 'picked'] = True
    print(bingoPlates.plates[0].number[0, 1, 'picked'])
    print(bingoPlates.plates[0].bingocheck())

    # print("\n")
    # for j in range(5):
    #     bingolist = [bingoPlates.plates[0].number[i, j, 'picked'] for i in range(5)]
    #     print('Bingolist er: ', bingolist)
    #     if all(bingolist):
    #         print('BINGO!!')
