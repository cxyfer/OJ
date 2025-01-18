"""
    0	[0, 1] + [0, 0] = [0, 1]	1
    1	[0, 1] + [1, 0] = [1, 1]	2
    2	[0, 1] + [2, 1] = [2, 2]	4
    3	[0, 1] + [4, 2] = [4, 3]	7
"""
while True:
    N = int(input())
    if N < 0:
        break
    m, f = 0, 1
    for _ in range(N):
        m, f = m + f, m + 1
    print(m, m + f)