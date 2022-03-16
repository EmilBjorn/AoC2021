# %%
from dataclasses import dataclass

# %%


def parse(input):
    with open(input) as f:
        bingonum = f.readline().split(',')
        # How to parse Bingo Plates?

# %%
# How to store bingo plate?


@dataclass
class Bingoplate():

    row = []
    col = []
    pass
