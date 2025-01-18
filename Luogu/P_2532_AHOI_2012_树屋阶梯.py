"""
    考慮左下角格子連接到哪個犄角，可以將問題分成兩部分的子問題，
    故 f(n) = f(0)f(n - 1) + f(1)f(n - 2) + ... + f(n - 1)f(0)
    即為Catalan Number

    包含高精度處理。
"""
from math import comb

n = int(input())
print(comb(2 * n, n) // (n + 1))