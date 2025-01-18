#
# @lc app=leetcode id=46 lang=python3
# @lcpr version=30202
#
# [46] Permutations
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return self.solve1(nums)
        return self.solve2(nums)
    """
        1. 用一個 visited 陣列來記錄是否已經選過
    """
    def solve1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = [0] * n
        visited = [False] * n
        def dfs(i: int):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(n):
                if not visited[j]:
                    visited[j] = True
                    path[i] = nums[j]
                    dfs(i+1)
                    visited[j] = False
        dfs(0)
        return ans
    """
        2. 交換法，把未選過的數字放到後面
    """
    def solve2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def perm(i): # 當前考慮第 i 個位置
            # if i == n:
            if i == n-1: # 剩下一個位置，不用再交換，故到 n-1 即可
                ans.append(nums.copy())
                return
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i] # swap
                perm(i+1)
                nums[i], nums[j] = nums[j], nums[i] # swap back
        perm(0)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

