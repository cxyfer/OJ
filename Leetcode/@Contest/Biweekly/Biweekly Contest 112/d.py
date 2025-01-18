"""
8050. Count K-Subsequences of a String With Maximum Beauty

You are given a string s and an integer k.

A k-subsequence is a subsequence of s, having length k, and all its characters are unique, i.e., every character occurs once.

Let f(c) denote the number of times the character c occurs in s.

The beauty of a k-subsequence is the sum of f(c) for every character c in the k-subsequence.

For example, consider s = "abbbdd" and k = 2:

f('a') = 1, f('b') = 3, f('d') = 2
Some k-subsequences of s are:
"abbbdd" -> "ab" having a beauty of f('a') + f('b') = 4
"abbbdd" -> "ad" having a beauty of f('a') + f('d') = 3
"abbbdd" -> "bd" having a beauty of f('b') + f('d') = 5
Return an integer denoting the number of k-subsequences whose beauty is the maximum among all k-subsequences. Since the answer may be too large, return it modulo 109 + 7.

A subsequence of a string is a new string formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

Notes

f(c) is the number of times a character c occurs in s, not a k-subsequence.
Two k-subsequences are considered different if one is formed by an index that is not present in the other. So, two k-subsequences may form the same string.
"""
from collections import Counter
from functools import cache
from itertools import combinations
class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        cnt = Counter(s)
        n = len(cnt)

        # 先算出最大的beauty
        max_beauty = sum(sorted(list(cnt.values()), reverse=True)[:k])

        # Digit DP ?
        # s 只有 26 種字母，所以可以用 mask 來表示集合
        # 前一個字母是什麼，可以用 alphabet 來表示
        # 前面的和，可以用 pre 來表示
        @cache # memoize
        def cal(i: int, mask: int, pre=0) -> int:
            print(i, format(mask, 'b'), pre)
            if i == k:
                if pre == max_beauty:
                    return 1
                else:
                    return 0
            res = 0 # 當前位數下，符合條件的特殊數字數量，初始為0
            for alphabet in cnt:  # 遍歷當前digit可填入的數字d
                # alphabet = chr(d + ord('a'))
                d = ord(alphabet) - ord('a')
                if (mask >> d & 1) == 0 and alphabet in cnt:  # 若 d 不在 mask 中，即 d 沒有填過
                    new_pre = pre + cnt[alphabet]
                    res += cal(i + 1, mask | (1 << d), new_pre) # 將此位填入 d，並更新 mask
            return res
        return cal(0, 0, 0)
sol = Solution()
print(sol.countKSubsequencesWithMaxBeauty("bcca", 2)) # 4
print(sol.countKSubsequencesWithMaxBeauty("abbcd", 4)) # 2