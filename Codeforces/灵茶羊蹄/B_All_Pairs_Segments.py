from bisect import *
from collections import *
from itertools import *

def debug(x):
    print(f"debug: {x}")

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())

    A = list(map(int, input().split()))
    quries = list(map(int, input().split()))

    mp = defaultdict(int)

    s = 0
    for i, (x, y) in enumerate(pairwise(A)):
        k = s - i * i + (n - 1 - i)
        debug(k)
        mp[i] = k  # WRONG
        s += (n - 1 - i)

    ans = [0] * q
    for i, k in enumerate(quries):
        ans[i] = mp[k]
    
    print(*ans)

"""
6 15
1 2 3 5 6 7
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

1
(1, 2)	0 + 5
[2, 3)	5 + 4
[3, 5)	


1 2 3 4 5 6 7 8 9 A B C D E F
0 0 0 0 2 0 0 0 3 0 2 0 0 0 0

!!! 端點的算法是不一樣的
"""