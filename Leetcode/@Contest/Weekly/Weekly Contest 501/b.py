import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q2: ||分組循環||?
題意有點繞，但本質上是將給定的 s 分解成單字，並統計每個單字的出現次數。
另外題目中說 `-` 的要被小寫字母包圍這個條件不夠清晰，實際上是 `-` 兩側要與小寫字母相鄰。

這種問題很適合用分組循環處理，找到小寫字母開始的位置，然後添加其他小寫字母或被小寫字母包圍的 `-` 直到遇到不滿足條件的位置。
這樣就能把 s 分成單字，最後用 Hash Table 統計每個單字的出現次數即可。
"""

class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = ''.join(chunks)
        n = len(s)

        def islower(ch: str) -> bool:
            return ord('a') <= ord(ch) <= ord('z')

        i = 0
        cnt = defaultdict(int)
        while i < n:
            if not islower(s[i]):
                i += 1
                continue
            st = i
            i += 1
            while i < n and (islower(s[i]) or i > 0 and i + 1 < n and islower(s[i-1]) and s[i] == '-' and islower(s[i+1])):
                i += 1
            cnt[s[st:i]] += 1
        return [cnt[query] for query in queries]

sol = Solution()
sol.countWordOccurrences(["hello-wor","ld-hello"], ["hello","world","wor"])  # [2,1,0]