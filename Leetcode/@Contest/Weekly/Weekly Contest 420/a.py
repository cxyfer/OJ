import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        s = ""

        for ch in target:
            s += 'a'
            ans.append(s)
            for _ in range(ord(ch) - ord('a')):
                s = s[:-1] + chr(((ord(s[-1]) - ord('a') + 1) % 26) + ord('a'))
                ans.append(s)
        return ans