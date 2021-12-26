# %%


def parse(puzzle_input):
    """Parse input"""
    with open(puzzle_input) as fin:
        data = [i for i in fin.read().strip().split("\n")]

    return data


data = parse("input.txt")

# %%


def part1(input):
    posdict = {}
    for element in input:
        for i, char in enumerate(element):
            if i in posdict:
                posdict[i] += char
            else:
                posdict[i] = char

    for item in posdict.items():
        posdict[item[0]] = item[1].replace('0', '')

    for item in posdict.items():

        if len(item[1]) > len(input)/2:
            posdict[item[0]] = '1'
        else:
            posdict[item[0]] = '0'

    gamma = ""
    for item in posdict.items():
        gamma += item[1]

    # gamma = 101101011111

    epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])

    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)
    print(gamma)
    print(epsilon)

    return gamma*epsilon


# %%
part1(data)

# %%

# %%
