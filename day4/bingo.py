# -*- coding: iso-8859-1 -*-
# %%
from dataclasses import dataclass, field
from typing import List

# %%


#TODO (Maybe): Test cases.
@dataclass
class Bingoplate:

    rawInput: list = field(repr=False)
    lastDrawn: int = field(repr=False, default=-1)

    def __post_init__(self) -> None:
        self.new_numbers: dict = {}
        for i, row in enumerate(self.rawInput):
            # print(row)
            for j, num in enumerate(row):
                self.new_numbers[(i, j)] = {'val': int(num), 'picked': False}

    def __str__(self) -> str:
        plate = ''
        for i in range(5):
            for key, item in self.new_numbers.items():
                number = (str(item['val']) if item['val'] > 9 else ' ' +
                          str(item['val']))

                if key[0] == i:
                    if item['picked'] == True:
                        plate += '(' + number + ')'
                    elif item['picked'] == False:
                        plate += ' ' + number + ' '
                    else:
                        test = str(item)
                        plate += '?' + test + '?'
            plate += '\n'
        return plate.strip('\n')

    def bingocheck(self) -> str:
        # Kode som checker om en plade har bingo et sted
        for i in range(5):
            bingolist = [self.new_numbers[(i, j)]['picked'] for j in range(5)]
            bingolist = [self.new_numbers[(j, i)]['picked'] for j in range(5)]

            #TODO: Er det smart at den både kan returnere bool & int?
            if all(bingolist):
                print('Bingocheck() says BINGO!!')
                return self.score()
        return False

    def pick(self, drawn_num: int) -> None:
        self.lastDrawn = drawn_num
        for key, item in self.new_numbers.items():
            if item['val'] == drawn_num:
                self.new_numbers[key]['picked'] = True

    def score(self):
        score = 0
        #TODO: Gør disse ranges dynamiske ifht størrelsen på bingo-pladen
        for i in range(5):
            for j in range(5):
                if not self.new_numbers[(i, j)]['picked']:
                    score += self.new_numbers[(i, j)]['val']

        score *= self.lastDrawn
        return score


@dataclass
class Deck:
    plates: List[Bingoplate] = field(init=False)

    def __post_init__(self):
        self.plates = []

    def add(self, plate):
        self.plates.append(plate)

    def draw(self, drawn_number: int):
        # Kode som looper over alle trukkede numre og checker om der er bingo
        for plate in self.plates:
            plate.pick(drawn_number)
            bingo = plate.bingocheck()
            if bool(bingo):
                print(plate)
                break
        return bingo


# %%


def parse(input):
    with open(input) as f:
        drawnNums = f.readline().strip().split(',')
        drawnNums = [int(i) for i in drawnNums]

        bingoPlates = Deck()
        plateList = []
        for i, line in enumerate(f):
            if i > 0:
                if line.strip() == '':
                    plate = Bingoplate(plateList)
                    bingoPlates.add(plate)
                    plateList = []
                else:
                    row = line.split()
                    plateList.append(row)

    return drawnNums, bingoPlates


def part1():
    nums, bingoPlates = parse('day4/input.txt')

    bingoPlates.plates = bingoPlates.plates
    print(bingoPlates.plates)

    for i in nums:
        print('Drawing: ', i)
        bingo = bingoPlates.draw(i)
        if bingo:
            break
    print(bingo)


# %%
if __name__ == '__main__':
    part1()
