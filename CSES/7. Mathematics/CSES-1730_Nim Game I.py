from functools import reduce

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    x = reduce(lambda x, y: x ^ y, A)
    print("second" if x == 0 else "first")