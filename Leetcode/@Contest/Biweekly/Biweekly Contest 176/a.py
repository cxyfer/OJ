import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from string import *

"""
按照題意模擬即可
"""


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # return ''.join(ascii_lowercase[25 - (sum(weights[ord(ch) - ord('a')] for ch in word) % 26)] for word in words)
        ans = []
        for word in words:
            w = sum(weights[ord(ch) - ord('a')] for ch in word) % 26
            ans.append(ascii_lowercase[25 - w])
        return ''.join(ans)
