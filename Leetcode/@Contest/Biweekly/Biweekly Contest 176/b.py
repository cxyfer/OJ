import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
乍一看還以為要 Trie，但其實按照前綴分組後判斷出現次數大於 1 的組數即可。
注意前綴需要至少 k 個字元。
"""


class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        groups = defaultdict(int)
        for word in words:
            if len(word) >= k:
                groups[word[:k]] += 1
        return sum(v > 1 for v in groups.values())
