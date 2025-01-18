#
# @lc app=leetcode id=1297 lang=python3
# @lcpr version=30204
#
# [1297] Maximum Number of Occurrences of a Substring
#


# @lcpr-template-start
# from preImport import *
from preImport import *
# @lcpr-template-end
# @lc code=start
MOD = 1070777777
BASE = randint(int(233), int(2333))

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        cnt_w = defaultdict(int)
        cnt_d = [0] * 26
        ans = have = hs = 0
        for i in range(minSize - 1):
            d = ord(s[i]) - ord('a')
            cnt_d[d] += 1
            if cnt_d[d] == 1:
                have += 1
            hs = (hs * BASE + d + 1) % MOD
        Pk = pow(BASE, minSize, MOD)
        for r in range(minSize - 1, n):
            dr = ord(s[r]) - ord('a')
            cnt_d[dr] += 1
            if cnt_d[dr] == 1:
                have += 1
            hs = (hs * BASE + dr + 1) % MOD
            if r >= minSize:
                dl = ord(s[r - minSize]) - ord('a')
                cnt_d[dl] -= 1
                if cnt_d[dl] == 0:
                    have -= 1
                hs = (hs - Pk * (dl + 1)) % MOD
            if have <= maxLetters:
                cnt_w[hs] += 1
                ans = max(ans, cnt_w[hs])
        return ans
# @lc code=end

sol = Solution()
print(sol.maxFreq("aababcaab", 2, 3, 4))  # 2
print(sol.maxFreq("aaaa", 1, 3, 3))  # 2
print(sol.maxFreq("aabcabcab", 2, 2, 3))  # 3
print(sol.maxFreq("abcde", 2, 3, 3))  # 0

#
# @lcpr case=start
# "aababcaab"\n2\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n1\n3\n3\n
# @lcpr case=end

#

