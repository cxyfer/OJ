# @algorithm @lc id=2904 lang=python3 
# @title sorting-three-groups


from en.Python3.mod.preImport import *
# @test([2,1,3,2,1])=3
# @test([1,3,2,1,3,3])=2
# @test([2,2,2,2,3,3])=0
# @test([3,1,2])=1
# @test([3,2,2,1,2])=2
# @test([3,1,3])=1
# @test([2,1,1,3,3,2])=2
# @test([1,1,2,1,1])=1
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*3 for _ in range(n)]
        for i in range(n):
            # dp[i][j] 表示前i個數字，最後一個數字可以填的最小數字是j+1的最小操作次數
            # dp[i][0] 表示最後一位是 1 的最小操作次數，因此需要使前面都是1，若當前數字大於1，則需要操作一次
            # dp[i][1] 表示最後一位是 2 的最小操作次數，因此需要使前面都是1或2，若當前數字大於2，則需要操作一次
            #   若前一位數字是2，但當前數字小於2，則從dp[i-1][1]後仍需操作一次
            # dp[i][2] 表示最後一位是 3 的最小操作次數，因此需要使前面都是1或2或3
            #   若前一位數字是2，但當前數字小於2，則從dp[i-1][1]後仍需操作一次
            #   若前一位數字是3，但當前數字小於3，則從dp[i-1][2]後仍需操作一次
            dp[i][0] = dp[i-1][0] + (1 if (nums[i] > 1) else 0)
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]+(1 if (nums[i] < 2) else 0)) + (1 if (nums[i] > 2) else 0)
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]+(1 if (nums[i] < 2) else 0), dp[i-1][2]+(1 if (nums[i] < 3) else 0))
        return dp[-1][-1]

if __name__ == "__main__":
    nums = [2,1,3,1,2]
    sol = Solution()
    print(sol.minimumOperations([2,1,3,2,1])) # 3
    print(sol.minimumOperations([1,3,2,1,3,3])) # 2
    print(sol.minimumOperations([2,2,2,2,3,3])) # 0
    print(sol.minimumOperations([3,1,2])) # 1
    print(sol.minimumOperations([3,2,2,1,2])) # 2
    print(sol.minimumOperations([3,1,3])) # 1
    print(sol.minimumOperations([2,1,1,3,3,2])) # 2
    print(sol.minimumOperations([1,1,2,1,1])) # 1