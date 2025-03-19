#
# @lc app=leetcode id=2610 lang=python3
#
# [2610] Convert an Array Into a 2D Array With Conditions
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        mx = max(cnt.values())
        ans = [[] for _ in range(mx)]
        for k, v in cnt.items():
            for i in range(v):
                ans[i].append(k)
        return ans

class Solution2:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        cnt = [0] * (n + 1)
        for x in nums:
            if cnt[x] == len(ans):
                ans.append([])
            ans[cnt[x]].append(x)
            cnt[x] += 1
        return ans

# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.findMatrix())