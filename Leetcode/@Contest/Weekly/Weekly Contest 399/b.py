import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        ans = ""
        i = 0
        while i < n:
            st = i
            while i < n and word[i] == word[st] and i - st < 9:
                i += 1
            ans += str(i - st) + word[st]
        return ans