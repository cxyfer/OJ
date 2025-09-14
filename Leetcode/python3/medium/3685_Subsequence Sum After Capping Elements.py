#
# @lc app=leetcode id=3685 lang=python3
#
# [3685] Subsequence Sum After Capping Elements
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        n = len(nums)
        heapify(nums)

        f = [1] + [0] * k
        ans = [False] * n
        for i in range(n):
            x = i + 1
            while nums and nums[0] <= x:
                v = heappop(nums)
                for j in range(k, v - 1, -1):
                    f[j] |= f[j - v]
            for j in range(min(len(nums), k // x) + 1):
                if f[k - j * x]:
                    ans[i] = True
                    break
        return ans
# @lc code=end
sol = Solution()
print(sol.subsequenceSumAfterCapping([4,3,2,4], 5))  # [false,false,true,true]
print(sol.subsequenceSumAfterCapping([1,4,5,4,4,4,7], 6))  # [true,true,true,false,true,true,true]