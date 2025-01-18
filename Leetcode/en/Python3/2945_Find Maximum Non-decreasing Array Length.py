# @algorithm @lc id=3211 lang=python3 
# @title find-maximum-non-decreasing-array-length


from en.Python3.mod.preImport import *
# @test([5,2,2])=1
# @test([1,2,3,4])=4
# @test([4,3,2,6])=3
class Solution:
    """
        DP + Monotonic Queue

        錯誤思路：Greedy (x)
        - 1, 2, 1, 3, 3
            - 1, 2, 7 (X)
            - 1, 3 ,3, 3 (O)
        正確思路：單調隊列優化DP (O)
    """
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0] + list(accumulate(nums))

        dp = [0] * (n + 1)
        last = [0] * (n + 1)

        q = deque([0])
        for i in range(1, n + 1):
            # 1. 去掉隊首無用數據
            # - j1 < j2 < i
            while len(q) > 1 and pre_sum[q[1]] + last[q[1]] <= pre_sum[i]:
                q.popleft()
            
            # 2. 計算轉移
            j = q[0]
            dp[i] = dp[j] + 1
            last[i] = pre_sum[i] - pre_sum[j]
            
            # 3. 去掉隊尾無用數據
            while q and pre_sum[q[-1]] + last[q[-1]] >= pre_sum[i] + last[i]:
                q.pop()
            q.append(i)
        return dp[n]

