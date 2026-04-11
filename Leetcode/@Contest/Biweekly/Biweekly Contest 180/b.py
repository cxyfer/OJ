import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        # return sum(str(x).count(str(digit)) for x in nums)
        ans = 0
        for x in nums:
            while x > 0:
                if x % 10 == digit:
                    ans += 1
                x //= 10
        return ans