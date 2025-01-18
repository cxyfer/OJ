from itertools import count

for kase in count(1):
    n = int(input().strip())
    if n == 0:
        break
    A = [tuple(map(int, input().strip().split())) for _ in range(n)]
    A.sort(key=lambda x: -x[1])
    ans = 0
    cur = 0
    for (b, j) in A:
        cur += b
        ans = max(ans, cur + j)
    print(f'Case {kase}: {ans}')