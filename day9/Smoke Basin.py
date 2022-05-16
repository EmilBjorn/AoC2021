#%%


def parse(input):
    with open(input) as f:
        data = [i for i in f.read().strip().split("\n")]

        for index, item in enumerate(data):
            data[index] = [int(i) for i in data[index]]

        data = addPadding(data)

        return data


# %%
def addPadding(input, padding=10):

    matrix = [[j for j in i] for i in input]

    matrix.insert(0, [padding for i in matrix[0]])
    matrix.append([padding for i in matrix[0]])

    for i, _ in enumerate(matrix):
        matrix[i].insert(0, padding)
        matrix[i].append(padding)

    return matrix


def findLowPoints(input):

    len1 = len(input)
    len2 = len(input[0])

    lowPointDict = {}
    for i in range(1, len1 - 1):
        for j in range(1, len2 - 1):
            value = input[i][j]
            if value < min([
                    input[i - 1][j],  # Coordinates for up
                    input[i + 1][j],  # Coordinates for down
                    input[i][j - 1],  # Coordinates for left
                    input[i][j + 1]  # Coordinates for right
            ]):
                lowPointDict[(i, j)] = {'size': 1, 'height': value}

    return lowPointDict


def printMatrix(input):
    for row in input:
        rowstr = ''
        for val in row:
            rowstr += f'{val:>2}, '
        print(f'[{rowstr[:-2]}]')


#%%
def part1(input):
    lowpoints = findLowPoints(input)
    risksum = 0
    for val in lowpoints.values():
        risksum += (val['height'] + 1)
    print('Part 1 answer:', risksum)


def part2(input):
    lowpointsdict = findLowPoints(input)

    for key in lowpointsdict.keys():
        coordlist = [key]
        pickedcoordset = set(coordlist)
        for coord in coordlist:
            for adj_coord in [
                (coord[0], coord[1] - 1), (coord[0], coord[1] + 1),
                (coord[0] - 1, coord[1]), (coord[0] + 1, coord[1])
            ]:
                if input[adj_coord[0]][
                        adj_coord[1]] < 9 and adj_coord not in pickedcoordset:
                    lowpointsdict[key]['size'] += 1
                    coordlist.append(adj_coord)
                    pickedcoordset.add(adj_coord)

    basinList = [val['size'] for val in lowpointsdict.values()]

    basinList.sort(reverse=True)
    mult = 1
    for i in basinList[:3]:
        mult = mult * i

    print('Part 2 answer:', mult)


#%%
if __name__ == "__main__":
    # ==== Initialize data =====
    data = parse("input.txt")
    test = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],  #
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],  #
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],  #
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],  #
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
    ]
    test = addPadding(test)
    # ==========================

    part1(data)
    part2(data)
# %%
