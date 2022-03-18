# -*- coding: iso-8859-1 -*-
# %%
from dataclasses import dataclass, field
from multiprocessing.sharedctypes import Value
from turtle import st
from typing import List


# %%


@dataclass
class Bingoplate:

    rawInput: list = field(repr=False)

    @dataclass
    class Bingonum:
        value: int
        picked: bool

    def __post_init__(self) -> None:
        self.number: dict = {}
        for i, row in enumerate(self.rawInput):
            for j, num in enumerate(row):
                self.number[(i, j, 'val')] = num
                self.number[(i, j, 'picked')] = False

    def __str__(self) -> str:
        plate = ""
        for i, row in enumerate(self.rawInput):
            for j, num in enumerate(row):
                if int(num) < 10:
                    strnum = '0'+num
                else:
                    strnum = num

                if self.number[(i, j, 'picked')] == True:
                    strnum = '('+strnum+')'
                else:
                    strnum = ' '+strnum+' '
                plate += strnum + " "
                # plate[(i,j)] = Bingonum(num,0)
            plate += '\n'
        return plate.strip('\n')

    def bingocheck(self) -> str:
        # Kode som checker om en plade har bingo et sted
        for i in range(5):
            bingolist = [self.number[i, j, 'picked'] for j in range(5)]
            # print('Bingolist  række ', i, 'er: ', bingolist)
            bingolist = [self.number[j, i, 'picked'] for j in range(5)]
            # print('Bingolist kolonne', i, 'er: ', bingolist)
            if all(bingolist):
                return True
        return False

    def pick(self, drawn_num: int) -> None:
        for key, item in self.number.items():
            if int(item) == drawn_num:
                self.number[key[:2]+('picked',)] = True             # key = (?,?,'val')   ||   key[:2]+('picked',) = (?,?,'picked')


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
        drawnNums = f.readline().strip().split(',')

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

    return drawnNums, bingoPlates


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

    bingoPlates.plates[0].number[0, 1, 'picked'] = True
    bingoPlates.plates[0].number[0, 2, 'picked'] = True
    bingoPlates.plates[0].number[0, 4, 'picked'] = True
    bingoPlates.plates[0].number[4, 0, 'picked'] = True
    bingoPlates.plates[0].number[1, 2, 'picked'] = True
    bingoPlates.plates[0].number[2, 2, 'picked'] = True
    bingoPlates.plates[0].number[3, 2, 'picked'] = True
    print()
    bingoPlates.plates[0].bingocheck()
    bingoPlates.plates[0].pick(96)
    print(bingoPlates.plates[0])
    bingoPlates.plates[0].bingocheck()

    # print("\n")
    # for j in range(5):
    #     bingolist = [bingoPlates.plates[0].number[i, j, 'picked'] for i in range(5)]
    #     print('Bingolist er: ', bingolist)
    #     if all(bingolist):
    #         print('BINGO!!')
