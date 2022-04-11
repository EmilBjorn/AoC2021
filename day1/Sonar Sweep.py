# %%
# %%


def parse(puzzle_input):
    """Parse input"""
    with open(puzzle_input) as fin:
        data = [int(i) for i in fin.read().strip().split("\n")]

    return data

# %%


test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def part1(input):
    result = [first < second for first, second in zip(input, input[1:])]
    return sum(result)


def part2(input):
    """create sliding sum list, then apply part 1 to that"""
    ssums = [sum(input[i:i+3]) for i in range(len(input))]

    return ssums[:-2]


input = parse("input.txt")

if __name__ == "__main__":

    print(part2(input))
    print(part1(part2(input)))
    print(len(part2(input)))
# %%
