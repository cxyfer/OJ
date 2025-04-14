#
# @lc app=leetcode id=3514 lang=python3
#
# [3514] Number of Unique XOR Triplets II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums = list(set(nums))  # 去重
        n = len(nums)

        pre = set([0])  # nums[i] ^ nums[j]
        ans = set([nums[0]])
        for k in range(1, n):
            for i in range(k + 1):
                pre.add(nums[i] ^ nums[k])  # nums[i] ^ nums[j]
            for p in pre:
                ans.add(p ^ nums[k])  # (nums[i] ^ nums[j]) ^ nums[k]
        return len(ans)
# @lc code=end

sol = Solution()
print(sol.uniqueXorTriplets([1,3])) # 2
print(sol.uniqueXorTriplets([6,7,8,9])) # 4

st = set()
for i in range(1, 1501):
    for j in range(1, 1501):
        st.add(i ^ j)
print(min(st), max(st))