# %%


def parse(puzzle_input):
    """Parse input"""
    with open(puzzle_input) as fin:
        data = [i.split() for i in fin.read().strip().split("\n")]

    return data


data = parse("input.txt")
# %%


def part1(input):
    horizontal = 0
    depth = 0
    for item in input:
        match item[0]:
            case 'forward':
                horizontal += int(item[1])
            case 'down':
                depth += int(item[1])
            case 'up':
                depth -= int(item[1])

    # print(horizontal, depth)
    return horizontal * depth


def part2(input):
    horizontal = 0
    depth = 0
    aim = 0
    for item in input:
        val = int(item[1])
        match item[0]:
            case 'forward':
                horizontal += val
                depth += aim*val
            case 'down':
                aim += val
            case 'up':
                aim -= val

    # print(horizontal, depth)
    return horizontal * depth


# %%
part1(data)

# %%
part2(data)
# %%
