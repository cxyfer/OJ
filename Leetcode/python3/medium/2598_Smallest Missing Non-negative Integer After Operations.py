#
# @lc app=leetcode id=2598 lang=python3
#
# [2598] Smallest Missing Non-negative Integer After Operations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1a:
    def findSmallestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        for x in nums:
            cnt[x % k] += 1
        for mex in range(n + 1):
            if cnt[mex] == 0:
                return mex
            cnt[mex + k] += cnt[mex] - 1
            cnt[mex] = 1
        return -1

class Solution1b:
    def findSmallestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * k  # 空間優化
        for x in nums:
            cnt[x % k] += 1
        for mex in range(n + 1):
            r = mex % k
            if cnt[r] == 0:
                return mex
            cnt[r] -= 1
        return -1

class Solution2:
    def findSmallestInteger(self, nums: List[int], k: int) -> int:
        cnt = [0] * k
        for x in nums:
            cnt[x % k] += 1
        mn = min(cnt)  # 瓶頸
        return mn * k + cnt.index(mn)

# Solution = Solution1a
# Solution = Solution1b
Solution = Solution2
# @lc code=end

