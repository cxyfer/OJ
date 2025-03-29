#
# @lc app=leetcode id=2818 lang=python3
#
# [2818] Apply Operations to Maximize Score
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 質數篩預處理出 prime score
2. 貪心思路是越大的數要盡可能的使用越多次
3. 考慮每個 x = nums[i] 可以使用多少次，即多少區間的貢獻是 x
    - 往左找到第一個 >= scores[x] 的下標 l，則左端點可以是 [l + 1, i]
    - 往右找到第一個 > scores[x] 的下標 r，則右端點可以是 [i, r - 1]
    - 共有 (i - l) * (r - i) 個區間
4. 排序並根據可以使用的次數計算貢獻。
"""
# @lc code=start
MOD = int(1e9+7)
MAXN = int(1e5+10)
scores = [0] * MAXN
for i in range(2, MAXN):
    if not scores[i]:
        for j in range(i, MAXN, i):
            scores[j] += 1

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [-1] * n
        suf = [n] * n
        st = [-1]  # Monotonic Stack，值由大到小，保存的是下標
        for i, x in enumerate(map(lambda x: scores[x], nums)):
            while st[-1] != -1 and scores[nums[st[-1]]] < x:
                suf[st.pop()] = i
            pre[i] = st[-1]
            st.append(i)

        idxs = list(range(n))
        idxs.sort(key=lambda x: nums[x], reverse=True)
        ans = 1
        for i in idxs:
            v = min((i - pre[i]) * (suf[i] - i), k)
            ans = ans * pow(nums[i], v, MOD) % MOD
            k -= v
            if k <= 0: break
        return ans
# @lc code=end

sol = Solution()
print(sol.maximumScore([8,3,9,3,8], 2))
print(sol.maximumScore([19,12,14,6,10,18], 3))
print(sol.maximumScore([6,30,210,30,6], 10))
