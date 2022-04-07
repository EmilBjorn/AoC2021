#%%
from statistics import median


def parse(file):
    with open(file) as f:
        text = f.readline()
    int_list = []
    for i in text.split(','):
        int_list.append(int(i))
    return int_list


def part1(input):
    med = int(median(input))

    cost = 0
    for i in input:
        cost += abs(i - med)
    print(cost)


def part2(input):

    def cost(n, target):
        diff = abs(target - n)
        return (diff * (diff + 1)) // 2

    best_cost = 1 << 100
    for target in range(min(input), max(input)):
        sum_cost = 0
        for i in input:
            sum_cost += cost(i, target)
        if sum_cost < best_cost:
            best_cost = sum_cost
    print(best_cost)


if __name__ == '__main__':
    input = parse('input.txt')
    part2(input)
# %%
