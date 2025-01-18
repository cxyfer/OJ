#
# @lc app=leetcode id=2440 lang=python3
# @lcpr version=30204
#
# [2440] Create Components With Same Value
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # 判斷是否可以將每個連通分量的總和都變成 tgt
        def dfs(u, fa, tgt):
            cur = nums[u]
            for v in g[u]:
                if v == fa:
                    continue
                res = dfs(v, u, tgt)
                if res == -1:  # 無法得到有效的分割
                    return -1
                cur += res
            if cur == tgt:  # 可以刪除 (u, fa) 這條邊，使子樹所屬的連通分量之總和等於 tgt
                return 0
            return cur if cur < tgt else -1  # 若 cur < tgt，則可以往上考慮：但若 cur > tgt，則無法得到有效的分割

        tot = sum(nums)
        for k in range(tot // max(nums), 1, -1):  # 枚舉連通分量數量
            if tot % k == 0:
                if dfs(0, -1, tot // k) == 0:
                    return k - 1
        return 0
# @lc code=end



#
# @lcpr case=start
# [6,2,2,2,6]\n[[0,1],[1,2],[1,3],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# [2]\n[]\n
# @lcpr case=end

#

