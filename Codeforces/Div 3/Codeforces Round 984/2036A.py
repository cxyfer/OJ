from itertools import pairwise

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    for x, y in pairwise(A):
        if abs(x - y) != 5 and abs(x - y) != 7:
            print("NO")
            break
    else:
        print("YES")