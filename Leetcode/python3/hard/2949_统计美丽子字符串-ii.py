#
# @lc app=leetcode.cn id=2949 lang=python3
#
# [2949] 统计美丽子字符串 II
#
from preImport import *
# @lc code=start
class Solution:
    """
        1. 對 k 做質因數分解
        2. 前綴和
        3. 雜湊表，統計 (i % k, pre_sum[i]) 出現的次數
    """
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        # 1. 對 4k 做質因數分解
        k = 4 * k
        for p in range(int(k**0.5), 1, -1): # k <= 1000
            if k % (p ** 2) == 0:
                k //= p
                break

        # 2. 前綴和
        vowels_set = set("aeiou")
        pre_sum = [0]
        for ch in s:
            x = 1 if ch in vowels_set else -1
            pre_sum.append(pre_sum[-1] + x)

        # 3. 雜湊表，統計 (i % k, pre_sum[i]) 出現的次數
        ans = 0
        cnt = Counter()
        for i, s in enumerate(pre_sum):
            p = (i % k, s)
            ans += cnt[p]
            cnt[p] += 1
        return ans
# @lc code=end
sol = Solution()
print(sol.beautifulSubstrings("baeyh",2)) # 2
print(sol.beautifulSubstrings("abba",1)) # 3
print(sol.beautifulSubstrings("bcdf",1)) # 0
print(sol.beautifulSubstrings("eeebjoxxujuaeoqibd", 8)) # 4
print(sol.beautifulSubstrings("ouafupsuhid", 6)) # 0