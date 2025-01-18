#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#
from preImport import *
# @lc code=start
class Solution:
    """
        Prefix Sum & Hash Table
        - 將問題轉換成 prefix_sum[j] - prefix_sum[i] = k ，且 i < j 的個數
        - 注意：不能用Sliding Window，因為nums中有負數
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int) # tbl[s] = prefix sum 為 s 的個數
        cnt[0] = 1
        pre = 0 # prefix_sum
        ans = 0
        for num in nums:
            pre += num # pre = prefix_sum[j]
            ans += cnt[pre-k] # pre-k = prefix_sum[i] 的個數
            cnt[pre] += 1
        return ans
# @lc code=end
sol = Solution()
print(sol.subarraySum([1,1,1],2)) # 2
print(sol.subarraySum([1,2,3],3)) # 2
print(sol.subarraySum([1,2,3],5)) # 1
print(sol.subarraySum([1], 0)) # 0
print(sol.subarraySum([1], 1)) # 1
print(sol.subarraySum([-1,-1,1], 0)) # 1