import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
本質就是維護一個Stask，檢查和 Stask 中相同元素的最短距離是否超過 k，若超過則將該元素加入 Stask，否則則跳過當前元素。
注意因為會有刪除操作，因此需要額外維護一個 offset 來記錄當前已經刪除了多少元素。
在檢查和更新位置時，需要使用 i - offset 來得到當前元素的位置。
"""


class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        last = [float("-inf")] * 26
        st = []
        offset = 0
        for i, ch in enumerate(s):
            c = ord(ch) - ord("a")
            if i - offset - last[c] <= k:
                offset += 1
                continue
            else:
                st.append(ch)
                last[c] = i - offset
        return "".join(st)
