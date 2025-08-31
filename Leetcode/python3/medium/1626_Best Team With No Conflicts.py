#
# @lc app=leetcode id=1626 lang=python3
# @lcpr version=30202
#
# [1626] Best Team With No Conflicts
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
2D LIS

1. O(n^2)
若 player[j] 可以接在 player[i] 後面，則 player[i] 的 score 和 age 都必須小於等於 player[j] 的 score 和 age

2. 基於值域計算 : O(nlogn + nU) , U 為 ages 的最大值
    由於 age <= 1e3 ，所以可以基於 age 的值域進行計算。
    首先對 players 依照 score 由小到大排序，若 score 相同則按照 age 由小到大排序。
    令 max_sum[i] 表示 age 最大為 i 的情況下的最大分數和，則 max_sum[age] = max(max_sum[:age+1]) + score
    * 由於排序後確保了 score 是遞增的，所以在已經遍歷過的方案中，並不會出現更大的 score ，也就確保了 max_sum[age] 的正確性。
3. 基於值域計算 + Binary Indexed Tree (BIT) 優化: O(nlogn + nlogU)
    類似於 2 ，但是使用 BIT 進行優化，可以將 max_sum[age] 的計算從 O(U) 降低到 O(logU)
Reference:
    - https://leetcode.cn/problems/best-team-with-no-conflicts/solutions/2183029/zui-chang-di-zeng-zi-xu-lie-cong-on2-dao-ojqu/
"""
# @lc code=start
class Solution1:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = sorted(zip(ages, scores)) # 排序後確保若 i < j ，則 ages[i] <= ages[j]
        f = [0] * n
        for i, (_, score) in enumerate(players):
            f[i] = score
            for j in range(i): # i 可以接在 j 後面
                if players[j][1] <= score:
                    f[i] = max(f[i], f[j] + score)
        return max(f)

class Solution2:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(scores, ages))
        f = [0] * (max(ages) + 1)
        for score, age in players:
            f[age] = max(f[:age+1]) + score
        return max(f)

class Solution3:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # sz = max(ages)
        # 離散化 
        mp = {v: i + 1 for i, v in enumerate(sorted(set(ages)))}
        sz = len(mp)

        # f[v] 表示當 age 最大為 v 的情況下的最大分數和，使用 BIT 維護前綴最大值
        tree = [0] * (sz + 1)
        def update(k: int, x: int) -> None:  # 更新 f[k] 為 max(f[k], x)
            while k <= sz:
                tree[k] = max(tree[k], x)
                k += (k & -k)

        def query(k: int) -> int:  # 返回 max(f[:k+1])
            res = 0
            while k > 0:
                res = max(res, tree[k])
                k -= (k & -k)
            return res
        
        for w, v in sorted(zip(scores, ages)):
            # update(v, query(v) + w)
            update(mp[v], query(mp[v]) + w)
        return query(sz)

Solution = Solution1
# Solution = Solution2
# Solution = Solution3
# @lc code=end



#
# @lcpr case=start
# [1,3,5,10,15]\n[1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,5]\n[2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n[8,9,10,1]\n
# @lcpr case=end

#

