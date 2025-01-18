import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        ck1, ck2 = False, False
        for ch in word:
            if ch.isalpha():
                if ch.lower() in "aeiou":
                    ck1 = True
                else:
                    ck2 = True
            elif not ch.isdigit():
                return False
        return ck1 and ck2