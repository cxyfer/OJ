#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#


# @lcpr-template-start
import math
from math import *
from typing import *
from collections import *
from functools import *
from itertools import *
from bisect import *
from heapq import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n # 紀錄words[i]出現過的字母
        for idx, w in enumerate(words):
            tmp = 0
            for ch in w:
                tmp |= (1 << (ord(ch) - ord('a')))
            masks[idx] = tmp
            idx += 1
        ans = 0
        for i in range(n):
            for j in range(i):
                if masks[i] & masks[j] == 0: # no common letters
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
# @lc code=end
sol = Solution()
print(sol.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])) # 16
print(sol.maxProduct(["a","ab","abc","d","cd","bcd","abcd"])) # 4
print(sol.maxProduct(["a","aa","aaa","aaaa"])) # 0

