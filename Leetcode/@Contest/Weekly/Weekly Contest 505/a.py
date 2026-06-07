import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *


class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        ans = 0
        for x in range(max(1, n - k), n + k + 1):  # x 必須是正數
            if n & x == 0:
                ans += x
        return ans