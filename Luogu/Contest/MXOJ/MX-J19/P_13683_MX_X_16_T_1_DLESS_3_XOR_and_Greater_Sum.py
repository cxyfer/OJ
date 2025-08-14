"""
XOR(arr1) > XOR(arr2)
=> XOR(arr1) != XOR(arr2)
-> XOR(nums) != 0
"""
from functools import reduce
from operator import xor

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print("Yes" if reduce(xor, A) != 0 else "No")