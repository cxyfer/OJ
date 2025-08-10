#
# @lc app=leetcode id=3646 lang=python3
#
# [3646] Next Special Palindrome Number
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
odds = [-1, 1, 3, 5, 7, 9]
evens = [2, 4, 6, 8]
ANS = []

for i in range(1 << len(evens)):
    cur_evens = []
    for j, even in enumerate(evens):
        if (i >> j) & 1:
            cur_evens.append(even)
    for odd in odds:
        digits = cur_evens + [odd] if odd != -1 else cur_evens
        if not digits:
            continue
        s = sum(digits)
        if s > 16:
            continue
        cnt = defaultdict(int)
        for d in digits:
            cnt[d] += d // 2
        n = sum(cnt.values())
        def dfs(i, cur):
            if i == n:
                ANS.append(int(cur + (str(odd) if odd != -1 else "") + cur[::-1]))
                return
            for d in cnt:
                if cnt[d] == 0:
                    continue
                cnt[d] -= 1
                dfs(i + 1, cur + str(d))
                cnt[d] += 1
        dfs(0, '')
ANS.sort()

class Solution:
    def specialPalindrome(self, n: int) -> int:
        idx = bisect_right(ANS, n)
        return ANS[idx]
# @lc code=end

sol = Solution()
print(sol.specialPalindrome(2))  # 22
print(sol.specialPalindrome(33))  # 212