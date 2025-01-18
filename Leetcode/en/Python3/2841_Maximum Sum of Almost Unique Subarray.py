# @algorithm @lc id=2954 lang=python3 
# @title maximum-sum-of-almost-unique-subarray


from en.Python3.mod.preImport import *
# @test([2,6,7,3,1,7],3,4)=18
# @test([5,9,9,2,4,5,4],1,3)=23
# @test([1,2,1,2,1,2,1],3,3)=0
class Solution:
    """
        Sliding window
    """
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cnt = Counter(nums[:k])
        s = sum(nums[:k]) # 統計前k-1個元素的和
        ans = 0
        if len(cnt) >= m:
            ans = max(ans, s)
        left = 0
        for i in range(k, len(nums)):
            num = nums[i]
            # 移除左邊的元素
            cnt[nums[left]] -= 1
            s -= nums[left]
            if cnt[nums[left]] == 0: # 如果移除後的元素個數為0，則pairwise - 1
                del cnt[nums[left]]
                
            # 加入右邊的元素
            cnt[num] += 1
            s += num
            if len(cnt) >= m:
                ans = max(ans, s)
            left += 1
        return ans