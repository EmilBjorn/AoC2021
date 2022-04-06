# -*- coding: iso-8859-1 -*-
#%%
from dataclasses import dataclass, field
from PIL import Image, ImageDraw


def parse(input) -> list:
    """
    Function to parse puzzle input into list of dict with 
    x1, x2, y1, y2 as keys and integers as values.
    
    """
    with open(input) as file:
        coords = []
        for line in file.readlines():
            coords.append(line.strip())
        for index, coord in enumerate(coords):
            coordlist = coord.split(" -> ")
            for i, number in enumerate(coordlist):
                numberlist = number.split(",")
                coordlist[i] = numberlist
            coords[index] = coordlist
        coord_dictlist = []
        for i, coordset in enumerate(coords):
            coord_dictlist.append({
                "x1": int(coordset[0][0]),
                "y1": int(coordset[0][1]),
                "x2": int(coordset[1][0]),
                "y2": int(coordset[1][1])
            })

    return coord_dictlist


#%%
@dataclass
class Seamap:

    xdim: int
    ydim: int
    map: list = field(init=False)
    count_vertical: int = 0
    count_horizontal: int = 0
    count_diagonal: int = 0

    def __post_init__(self) -> None:
        self.map = [[0 for i in range(self.ydim)] for j in range(self.xdim)]

        self.imap = Image.new('RGB', (self.xdim, self.ydim))
        self.imap2 = Image.new('RGB', (self.xdim, self.ydim))

    def __str__(self) -> str:
        string = ''
        for x in self.map:
            for y in x:
                if y == 0:
                    string += '.'
                else:
                    string += y
                string += ' '
            string += '\n'
        return string

    def draw_vent(self, coordset) -> None:
        if coordset['x1'] == coordset['x2']:
            mode = 'vertical'
        elif coordset['y1'] == coordset['y2']:
            mode = 'horizontal'
        else:
            mode = 'diagonal'
        modecolor = {
            'vertical': 'red',
            'horizontal': 'white',
            'diagonal': 'orange'
        }
        count = 0

        new_imap2 = ImageDraw.Draw(self.imap2)

        if mode == 'vertical':
            start = min([coordset['y1'], coordset['y2']])
            end = max([coordset['y1'], coordset['y2']])

            for i in range(start, end + 1):
                self.map[coordset['x1']][i] += 1
                new_imap2.point((coordset['x1'], i), fill='red')
                count += 1
            self.count_vertical += 1

        elif mode == 'horizontal':
            start = min([coordset['x1'], coordset['x2']])
            end = max([coordset['x1'], coordset['x2']])
            for i in range(start, end + 1):
                self.map[i][coordset['y1']] += 1
                new_imap2.point((i, coordset['y1']), fill='red')
                count += 1
            self.count_horizontal += 1

        elif mode == 'diagonal':
            xdiff = coordset['x2'] - coordset['x1']
            xstep = int(xdiff / abs(xdiff))
            ydiff = coordset['y2'] - coordset['y1']
            ystep = int(ydiff / abs(ydiff))

            xcoords = range(coordset['x1'], coordset['x2'] + xstep, xstep)
            ycoords = range(coordset['y1'], coordset['y2'] + ystep, ystep)

            for index, xval in enumerate(xcoords):
                yval = list(ycoords)[index]
                self.map[xval][yval] += 1
                new_imap2.point((xval, yval), fill='red')
                count += 1
            self.count_diagonal += 1

        # print(f'{coordset} added {count} fields {mode}ly')

        # Draws line on Pillow image
        coordlist = []
        for item in coordset.values():
            coordlist.append(item)
        new_imap = ImageDraw.Draw(self.imap)
        new_imap.line(coordlist, modecolor[mode])


#%%
def part1(coordlist, map):

    for coord in coordlist:
        if coord['x1'] == coord['x2'] or coord['y1'] == coord['y2']:
            map.draw_vent(coord)

    count = 0
    for i in map.map:
        for j in i:
            if j > 1:
                count += 1
    print('part 1:', count)


def part2(coordlist, map):
    for coord in coordlist:
        map.draw_vent(coord)

    count = 0
    for i in map.map:
        for j in i:
            if j > 1:
                count += 1

    print(
        f'Added {map.count_diagonal+map.count_horizontal+map.count_vertical} lines'
    )
    print(f'{map.count_vertical=}')
    print(f'{map.count_horizontal=}')
    print(f'{map.count_diagonal=}')

    print('part 2:', count)


if __name__ == "__main__":
    coords = parse("input.txt")
    map = Seamap(1000, 1000)
    part1(coords, map)
    map = Seamap(1000, 1000)
    part2(coords, map)

# %%

# %%

# %%

# %%
