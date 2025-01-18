#
# @lc app=leetcode.cn id=2003 lang=python3
#
# [2003] 每棵子树内缺失的最小基因值
#
from typing import *
# @lc code=start
class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        ans = [1] * n # 先預設每個節點都缺失基因值 1
        if 1 not in nums: # 如果沒有基因值 1，那麼答案就是 1
            return ans

        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parents[i]].append(i)

        visited = set()
        def dfs(x: int) -> None:
            visited.add(nums[x]) 
            for son in g[x]:
                if nums[son] not in visited:
                    dfs(son)

        # 除了1的ancestor以外，其他節點都缺失基因值1
        mex = 2 # mex: minimum excluded number 缺失的最小基因值
        node = nums.index(1) # 
        while node >= 0:
            dfs(node)
            while mex in visited:  # node 子树包含这个基因值
                mex += 1
            ans[node] = mex # 缺失的最小基因值
            node = parents[node]  # 往上走
        return ans
# @lc code=end

