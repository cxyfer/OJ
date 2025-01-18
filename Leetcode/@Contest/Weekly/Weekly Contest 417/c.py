import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = set('aeiou')

        # pre[i] 表示 word[i] 前面有多少個連續的母音 (不含 word[i])
        pre = [0] * n
        for i in range(n - 1):
            if word[i] in vowels:
                pre[i + 1] = pre[i] + 1

        cnt_vowel = defaultdict(int)
        have_vowel = 0 # 母音的種類

        ans = 0
        cnt = 0 # 子音的數量
        left = 0
        for right, ch in enumerate(word):
            if ch in vowels:
                if cnt_vowel[ch] == 0:
                    have_vowel += 1
                cnt_vowel[ch] += 1
            else:
                cnt += 1

            while cnt > k:
                lc = word[left]
                if lc in vowels:
                    cnt_vowel[lc] -= 1
                    if cnt_vowel[lc] == 0:
                        have_vowel -= 1
                else:
                    cnt -= 1
                left += 1

            if cnt == k and have_vowel == 5:
                # 把前綴中多餘的母音去掉
                while left < right and word[left] in vowels and cnt_vowel[word[left]] > 1:
                    cnt_vowel[word[left]] -= 1
                    left += 1
                # pre[left] 即窗口可以延伸的長度
                ans += pre[left] + 1

        return ans

sol = Solution()
print(sol.countOfSubstrings("aeioqq", 1)) # 0
print(sol.countOfSubstrings("aeiou", 0)) # 1
print(sol.countOfSubstrings("ieaouqqieaouqq", 1)) # 3
print(sol.countOfSubstrings("iqeaouqi", 2)) # 3
print(sol.countOfSubstrings("aadieuoh", 1)) # 2
print(sol.countOfSubstrings("aoaiuefi", 1)) # 4
