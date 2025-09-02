# 直接模擬吧
from itertools import permutations
from math import factorial

mtrx = [ list(map(int, input().split(" "))) for _ in range(3) ]

target = []
if mtrx[0][0] == mtrx[1][1]:
    target += [[(2,2), (0, 0), (1, 1)]]
if mtrx[0][0] == mtrx[2][2]:
    target += [[(1,1), (0, 0), (2, 2)]]
if mtrx[1][1] == mtrx[2][2]:
    target += [[(0,0), (1, 1), (2, 2)]]
if mtrx[0][2] == mtrx[1][1]:
    target += [[(2,0), (0, 2), (1, 1)]]
if mtrx[0][2] == mtrx[2][0]:
    target += [[(1,1), (0, 2), (2, 0)]]
if mtrx[1][1] == mtrx[2][0]:
    target += [[(0,2), (1, 1), (2, 0)]]
for i in range(3):
    if mtrx[0][i] == mtrx[1][i]:
        target += [[(2,i), (0, i), (1, i)]]
    if mtrx[0][i] == mtrx[2][i]:
        target += [[(1,i), (0, i), (2, i)]]
    if mtrx[1][i] == mtrx[2][i]:
        target += [[(0,i), (1, i), (2, i)]]
    if mtrx[i][0] == mtrx[i][1]:
        target += [[(i,2), (i, 0), (i, 1)]]
    if mtrx[i][0] == mtrx[i][2]:
        target += [[(i,1), (i, 0), (i, 2)]]
    if mtrx[i][1] == mtrx[i][2]:
        target += [[(i,0), (i, 1), (i, 2)]]
ans = 0
fac9 = factorial(9)
idxs = [(i//3, i%3) for i in range(9)]
perm = permutations(idxs)
ans = fac9
for p in list(perm):
    for (a,b,c) in target:
        if p.index(b) < p.index(a) and p.index(c) < p.index(a):
            ans -= 1
            break
print(ans/fac9)