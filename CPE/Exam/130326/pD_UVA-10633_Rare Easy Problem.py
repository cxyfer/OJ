"""
N = M * 10 + x
d = N - M = M * 9 + x
M = (d - x) / 9
"""

while True:
    d = int(input())
    if d == 0:
        break
    ans = []
    for x in range(10):
        q, r = divmod(d - x, 9)
        if r == 0:
            ans.append(q * 10 + x)
    ans.sort()
    print(*ans)