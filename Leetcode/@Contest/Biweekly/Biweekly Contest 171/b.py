import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

def is_palindrome(x):
    s = bin(x)[2:]
    return s == s[::-1]

MAX_X = int(5e3 + 100)
A = []
for x in range(MAX_X):
    if is_palindrome(x):
        A.append(x)

class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            i = bisect_left(A, x)
            ans.append(min(A[i] - x, x - A[i - 1]))
        return ans