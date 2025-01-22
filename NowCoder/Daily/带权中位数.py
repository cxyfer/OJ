from itertools import *

n = int(input())
P = list(map(int, input().split()))
A = list(map(int, input().split()))

tot = sum(A)
s = list(accumulate(A))
for i in range(n):
    if 2 * s[i] >= tot:
        print(i + 1)
        break