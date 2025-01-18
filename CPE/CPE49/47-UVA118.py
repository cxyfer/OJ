"""
    Simulation
    原題目(UVA)的測資有個很怪的地方，在四個角落往兩個方向都會使機器人掉落，
    按照題意應該要記錄面朝方向，所以要視為兩種情況，
    但是在的測資中是「在某個位置掉落過就不會再從該位置掉落」。
"""
from collections import *

X, Y = map(int, input().split())
DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIR_MAP = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
STR_MAP = "NESW"
# scent = defaultdict(list)
scent = set()

while True:
    try:
        x, y, z = input().split()
        s = input()
    except:
        break
    x, y = int(x), int(y)
    d = DIR_MAP[z]
    lost = False
    for i, ch in enumerate(s):
        if ch == 'F':
            dx, dy = DIR[d]
            nx, ny = x + dx, y + dy
            if 0 <= nx <= X and 0 <= ny <= Y: # in the grid
                x, y = nx, ny
            else:
                # if d not in scent[(x, y)]:
                #     scent[(x, y)].append(d)
                #     lost = True
                #     break
                if (x, y) not in scent:
                    scent.add((x, y))
                    lost = True
                    break
        elif ch == 'L':
            d = (d - 1) % 4
        elif ch == 'R':
            d = (d + 1) % 4
    print(x, y, STR_MAP[d], end="")
    print(' LOST' if lost else '')