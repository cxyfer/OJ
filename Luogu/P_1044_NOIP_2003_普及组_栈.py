"""
    Catalan Number
"""
from math import *

n = int(input())
print(comb(2 * n, n) // (n + 1))