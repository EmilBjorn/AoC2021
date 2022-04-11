#%%
def parse(input):
    with open(input) as f:
        lines = [i.strip() for i in f.readlines()]
        rawlist = [i.split(' ') for i in lines]
        setlist = [[{j for j in k} for k in i] for i in rawlist]
        dictlist = [{'key': i[:10], 'signal': i[-4:]} for i in setlist]

        return dictlist


def part1():
    count = 0
    for i in data:
        for j in i['signal']:
            if len(j) in [2, 3, 4, 7]:
                count += 1
    print('part1:', count)


def part2(input):

    sum = 0

    for i in input:
        lookup = {
            0: {},
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
            8: {},
            9: {}
        }
        for val in i['key']:
            if len(val) == 2:
                lookup[1] = val
            elif len(val) == 3:
                lookup[7] = val
            elif len(val) == 4:
                lookup[4] = val
            elif len(val) == 7:
                lookup[8] = val

        for val in i['key']:
            if len(val) == 6:
                if not val.issuperset(lookup[1]):
                    lookup[6] = val
                elif val.issuperset(lookup[4]):
                    lookup[9] = val
                else:
                    lookup[0] = val

        c_segment = lookup[1].difference(lookup[6])
        f_segment = lookup[1].intersection(lookup[6])

        for val in i['key']:
            if len(val) == 5:
                if val.issuperset(lookup[1]):
                    lookup[3] = val
                elif val.issuperset(
                        c_segment) and not val.issuperset(f_segment):
                    lookup[2] = val
                elif val.issuperset(
                        f_segment) and not val.issuperset(c_segment):
                    lookup[5] = val

        output: str = ''
        for j in i['signal']:
            for key, val in lookup.items():
                if j == val:
                    output += str(key)

        sum += int(output)

    print('part2:', sum)


# %%
if __name__ == '__main__':

    data = parse('input.txt')

    part1()
    part2(data)
# %%

# %%
