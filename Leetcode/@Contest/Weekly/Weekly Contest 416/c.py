import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        cnt2 = Counter(word2)
        required = len(cnt2)
        cnt = defaultdict(int) # window
        ans = left = formed = 0
        n = len(word1)
        for right in range(n):
            ch = word1[right]
            cnt[ch] += 1
            if ch in cnt2 and cnt[ch] == cnt2[ch]:
                formed += 1
            while left <= right and formed == required:
                ans += n - right
                ch = word1[left]
                cnt[ch] -= 1
                if ch in cnt2 and cnt[ch] < cnt2[ch]:
                    formed -= 1
                left += 1
        return ans
    
# 建立 Solution 的實例
solution = Solution()

# 範例 1
word1_1 = "bcca"
word2_1 = "abc"
print(solution.validSubstringCount(word1_1, word2_1))  # 輸出: 1

# 範例 2
word1_2 = "abcabc"
word2_2 = "abc"
print(solution.validSubstringCount(word1_2, word2_2))  # 輸出: 10

# 範例 3
word1_3 = "abcabc"
word2_3 = "aaabc"
print(solution.validSubstringCount(word1_3, word2_3))  # 輸出: 0
