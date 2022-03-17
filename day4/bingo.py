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
            if i >= 2:
                if not line.strip():
                    plate = Bingoplate(plateList)
                    bingoPlates.add(plate)
                row = line.split()
                plateList.append(row)

    return bingonum, bingoPlates
    # How to parse Bingo Plates?

# %%
# How to store bingo plate?


@dataclass
class Bingoplate:

    rawInput: list

    def __post_init__(self):
        self.values = {}
        self.picked = {}


@dataclass
class Deck:
    plates: List[Bingoplate] = field(init=False)

    def __post_init__(self):
        self.plates = []

    def add(self, plate):
        self.plates.append(plate)


if __name__ == "__main__":
    nums, bingoPlates = parse("day4/input.txt")
    print(nums)
    print(bingoPlates)
