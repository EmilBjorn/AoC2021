#%%
def parse(file):
    with open(file) as f:
        text = f.readline()
    int_list = []
    for i in text.split(','):
        int_list.append(int(i))
    return int_list


def age(list):
    new_list = list
    for i, val in enumerate(list):
        new_list[i] = val - 1
        if new_list[i] == -1:
            new_list[i] = 6
            new_list.append(8)
    return new_list


def day1(input, days):
    for i in range(days):
        input = age(input)
        print(i, input[10:], len(input))
    print(len(input))


# %%
if __name__ == "__main__":
    input = parse('input.txt')
    print(len(input))
    day1(input, 80)

# %%
