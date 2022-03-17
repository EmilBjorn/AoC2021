# %%
from dataclasses import dataclass, field
from typing import List


# %%


def parse(input):
    with open(input) as f:
        bingonum = f.readline().strip().split(',')

        bingoPlates = Deck()
        plateList = []
        for i, line in enumerate(f):
            if i >= 2 and i <= 20:
                if line.strip() == "":
                    plate = Bingoplate(plateList)
                    bingoPlates.add(plate)
                    plateList = []
                else:
                    row = line.split()
                    plateList.append(row)

    return bingonum, bingoPlates

# %%


@dataclass
class Bingoplate:

    rawInput: list = field(repr=False)

    @dataclass
    class Bingonum:
        value: int
        picked: bool

    def __post_init__(self):

        pass
        # self.values = {}
        # self.picked = {}

    def __str__(self) -> str:
        plate = ""
        for i, row in enumerate(self.rawInput):
            for j, num in enumerate(row):
                plate += num + " "
                # plate[(i,j)] = Bingonum(num,0)
            plate += '\n'
        return plate


@dataclass
class Deck:
    plates: List[Bingoplate] = field(init=False)

    def __post_init__(self):
        self.plates = []

    def add(self, plate):
        self.plates.append(plate)


if __name__ == "__main__":
    nums, bingoPlates = parse("day4/input.txt")
    # print(nums)
    for i in range(3):
        print(bingoPlates.plates[i])
