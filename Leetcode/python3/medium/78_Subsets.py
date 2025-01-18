#
# @lc app=leetcode id=78 lang=python3
# @lcpr version=30202
#
# [78] Subsets
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. 回溯(Backtracking)：子集型回溯
        2. 狀態壓縮
        3. 逐個元素遍歷
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return self.solve1(nums)
        # return self.solve2(nums)
        return self.solve3(nums)
    def solve1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = []
        def dfs(i: int) -> None:
            if i == n: # 到達葉節點
                ans.append(path[:]) # 複製一份，因為是 Reference
                return
            dfs(i + 1) # 不選 nums[i]
            path.append(nums[i])
            dfs(i + 1) # 選 nums[i]
            path.pop()
        dfs(0)
        return ans
    def solve2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for i in range(1 << n): # 枚舉所有子集，狀態壓縮
            cur = [] # 當前子集
            for j in range(n):
                if i & (1 << j): # nums[j] 在當前子集中
                    cur.append(nums[j])
            ans.append(cur)
        return ans
    def solve3(self, nums: List[int]) -> List[List[int]]:
        ans = [[]] # 初始化答案，只包含一個空集合
        for x in nums: # 枚舉所有元素
            ans += [cur + [x] for cur in ans] # 複製一份當前的所有子集，並在其中添加當前元素 x
        return ans
# @lc code=end

#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

