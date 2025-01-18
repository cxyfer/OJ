# @algorithm @lc id=1286 lang=python3 
# @title constrained-subsequence-sum


from en.Python3.mod.preImport import *
# @test([10,2,-10,5,20],2)=37
# @test([-1,-2,-3],1)=-1
# @test([10,-2,-10,-5,20],2)=23
class Solution:
    """
        Dynamic Programming + Monotonic Queue
    """
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        q = deque()
        q.append(0)
        ans = nums[0]
        for i in range(1, n):
            while q and i - q[0] > k: # pop the out-of-range index
                q.popleft()
            dp[i] = max(nums[i], nums[i] + dp[q[0]])
            ans = max(ans, dp[i])
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)
        return ans