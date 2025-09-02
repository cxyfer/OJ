from itertools import accumulate

N = int(input())
D = list(map(int, input().split()))

for i, x in enumerate(D):
    print(*list(accumulate(D[i:])))