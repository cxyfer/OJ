#
# @lc app=leetcode id=3138 lang=python3
#
# [3138] Minimum Length of Anagram Concatenation
#
from preImport import *
# @lc code=start
class Solution:
    def minAnagramLength(self, s: str) -> int:
        # return self.solve1(s)
        # return self.solve2(s) # 邏輯一樣，但更簡潔
        return self.solve3(s) # 改用排序來比對，在Python中會更快
    def solve1(self, s: str) -> int:
        n = len(s)
        cnt = [0] * 26
        for k in range(1, n//2+1): # 枚舉可能的長度，最大長度為n//2
            cnt[ord(s[k-1]) - ord("a")] += 1
            if n % k != 0: continue
            flag = True
            for i in range(k, n, k):
                cnt2 = [0] * 26
                for j in range(k):
                    cnt2[ord(s[i+j]) - ord("a")] += 1
                if cnt2 != cnt:
                    flag = False
                    break
            if flag:
                return k
        return n
    def solve2(self, s: str) -> int:
        n = len(s)
        cnt = Counter()
        for k in range(1, n//2+1):
            cnt[s[k-1]] += 1
            if n % k != 0: continue
            if all(cnt == Counter(s[i:i+k]) for i in range(k, n, k)):
                return k
        return n
    def solve3(self, s: str) -> int:
        n = len(s)
        for k in range(1, n//2+1):
            if n % k != 0: continue
            cnt = sorted(s[:k])
            if all(cnt == sorted(s[i:i+k]) for i in range(k, n, k)):
                return k
        return n
# @lc code=end

