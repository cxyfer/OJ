#
# @lc app=leetcode id=40 lang=python3
# @lcpr version=30204
#
# [40] Combination Sum II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []
        path = []
        def dfs(i: int, s: int):
            if s == target:
                ans.append(path[:])
                return
            for j in range(i, n): # 考慮下一個選的元素
                # 若當前元素和上一個元素相同，則不需要再考慮
                # 沒選上一個，則也不能選第二個相同的元素
                # 若有多個相同的元素，則只能從前面開始選
                if j > i and candidates[j] == candidates[j - 1]: # 跳過重複的元素
                    continue
                if s + candidates[j] > target: # 剪枝
                    break
                path.append(candidates[j])
                dfs(j + 1, s + candidates[j])
                path.pop()
        dfs(0, 0)
        return ans
# @lc code=end

sol = Solution()
print(sol.combinationSum2([2,5,2,1,2], 5))


#
# @lcpr case=start
# [10,1,2,7,6,1,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2,5,2,1,2]\n5\n
# @lcpr case=end

#

