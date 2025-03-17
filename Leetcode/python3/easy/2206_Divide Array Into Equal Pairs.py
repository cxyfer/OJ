#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def divideArray(self, nums: List[int]) -> bool:
        # return all((v & 1) == 0 for v in Counter(nums).values())
        n = len(nums) // 2
        ans = 0
        vis = [False] * 501
        for x in nums:
            ans += vis[x]
            vis[x] = not vis[x]
        return ans == n
    
class Solution2:
    def divideArray(self, nums: List[int]) -> bool:
        vis = [False] * 501
        for x in nums:
            vis[x] = not vis[x]
        return all(x == False for x in vis)

class Solution3:
    def divideArray(self, nums: List[int]) -> bool:
        vis = set()
        for x in nums:
            if x in vis:
                vis.remove(x)
            else:
                vis.add(x)
        return len(vis) == 0
    
class Solution(Solution1):
# class Solution(Solution2):
# class Solution(Solution3):
    pass
# @lc code=end
