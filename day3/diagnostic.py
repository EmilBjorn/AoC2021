
# %%
from scipy import stats
import numpy as np

# %%


# def parse(puzzle_input):
#     """Parse input"""
#     with open(puzzle_input) as fin:
#         data = [i for i in fin.read().strip().split("\n")]

#     return data


# %%

def parse(puzzle_input):
    with open(puzzle_input) as fin:
        data = [i for i in fin.read().strip().split("\n")]

        for index, item in enumerate(data):
            data[index] = [i for i in data[index]]
    return data


data = np.array(parse("input.txt"))

# %%


def part1(data):
    mode = stats.mode(data).mode[0]

    gamma = ''
    for i in mode:
        gamma += i

    epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])

    gamma_int = int(gamma, base=2)
    epsilon_int = int(epsilon, base=2)

    return gamma_int*epsilon_int


def part2(data):
    mode = stats.mode(data).mode[0]
    print(len(data))
    for mode_index, mode_item in enumerate(mode):
        new_data = []
        for data_index, data_item in enumerate(data):
            if data_item[mode_index] == mode_item:
                new_data.append(data_item)
        data = new_data
        mode = stats.mode(data).mode[0]
        print(len(data))

    print(mode, data)

# %%


# %%
part1(data)
# %%
part2(data)
# %%

# %%
