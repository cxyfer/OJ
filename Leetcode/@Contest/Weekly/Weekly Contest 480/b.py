import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        cnt = sum(ch in "aeiou" for ch in words[0])
        for i, w in enumerate(words):
            if i > 0 and sum(ch in "aeiou" for ch in w) == cnt:
                words[i] = w[::-1]
        return " ".join(words)