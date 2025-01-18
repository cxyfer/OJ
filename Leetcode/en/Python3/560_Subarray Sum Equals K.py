# @algorithm @lc id=560 lang=python3 
# @title subarray-sum-equals-k


from en.Python3.mod.preImport import *
# @test([1,1,1],2)=2
# @test([1,2,3],3)=2
class Solution:
    """
        Prefix Sum & Hash Table
        - 將問題轉換成 prefix_sum[j] - prefix_sum[i] = k ，且 i < j 的個數
        - 注意：不能用Sliding Window，因為nums中有負數
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int) # tbl[s] = prefix sum 為 s 的個數
        cnt[0] = 1
        pre = 0 # prefix_sum
        ans = 0
        for num in nums:
            pre += num # pre = prefix_sum[j]
            ans += cnt[pre-k] # pre-k = prefix_sum[i] 的個數
            cnt[pre] += 1
        return ans