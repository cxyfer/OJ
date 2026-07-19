import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q2: 貪心
要構造最大的數可以在增加時 +m ，而減少時只 -1 。
增加次數最多為 n // 2 次，在最高值之前的減少次數為 max(0, n // 2 - 1) 次，因此可以直接計算出答案。
"""


class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        add = n // 2
        sub = max(0, n // 2 - 1)
        return s + add * m - sub
