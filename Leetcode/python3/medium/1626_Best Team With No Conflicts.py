#
# @lc app=leetcode id=1626 lang=python3
# @lcpr version=30202
#
# [1626] Best Team With No Conflicts
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        2D Longest Increasing Subsequence (LIS)
        1. Dynamic Programming: O(n^2)
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
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # return self.solve1(scores, ages)
        # return self.solve2(scores, ages)
        return self.solve3(scores, ages)
    def solve1(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = sorted(zip(ages, scores)) # 排序後確保若 i < j ，則 ages[i] <= ages[j]
        dp = [0] * n
        for j, (age, score) in enumerate(players):
            dp[j] = score
            for i in range(j): # j 可以接在 i 後面
                if players[i][1] <= score:
                    dp[j] = max(dp[j], dp[i] + score)
        return max(dp)
    def solve2(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(scores, ages))
        max_sum = [0] * (max(ages) + 1)
        for score, age in players:
            max_sum[age] = max(max_sum[:age+1]) + score
            # for i in range(age-1, -1, -1):
            #     max_sum[age] = max(max_sum[age], max_sum[i])
            # max_sum[age] += score
        return max(max_sum)
    def solve3(self, scores: List[int], ages: List[int]) -> int:
        mx = max(ages)
        tree = [0] * (mx + 1)

        def update(k: int, x: int) -> None: # 更新 max_sum[k] 為 x
            while k <= mx:
                tree[k] = max(tree[k], x)
                k += (k & -k)

        def query(k: int) -> int: # 返回 max(max_sum[:k+1])
            res = 0
            while k > 0:
                res = max(res, tree[k])
                k -= (k & -k)
            return res
        
        for score, age in sorted(zip(scores, ages)):
            update(age, query(age) + score)
        return query(mx)
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

