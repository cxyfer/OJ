from math import gcd
from functools import reduce

n = int(input())
A = list(map(int, input().split()))

g = reduce(gcd, A)
print(n * g)