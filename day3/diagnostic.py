
# %%
from scipy import stats
import numpy as np'


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


def statmode(data):
    mode_dict = stats.mode(data)._asdict()
    mode = mode_dict['mode'][0]
    count = mode_dict['count'][0]

    for index, item in enumerate(count):
        if item == len(data)/2:
            mode[index] = 1

    return mode


def life_rating(data, opposite_mode=False):
    print(len(data))
    for numpos in range(12):
        new_data = []

        mode = statmode(data)  # Generate new filter based on the new dataset

        for data_item in data:
            if opposite_mode:
                if data_item[numpos] != mode[numpos]:
                    new_data.append(data_item)
            else:
                if data_item[numpos] == mode[numpos]:
                    new_data.append(data_item)

        data = new_data
        print(len(data))
        if len(data) == 1:
            output_string = ""
            for bit in data[0]:
                output_string += bit

            print(output_string, int(output_string, base=2))
            break

    output_string = ""
    for bit in data[0]:
        output_string += bit
    # print(output_string)

    return output_string


def part2(data):
    oxygen_binary = life_rating(data)
    co2_binary = life_rating(data, opposite_mode=True)

    return int(oxygen_binary, base=2) * int(co2_binary, base=2)


# %%
part1(data)
# %%
part2(data)
# %%

# %%

# %%

# %%
