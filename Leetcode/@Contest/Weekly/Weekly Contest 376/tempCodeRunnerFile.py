class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        pre_sum = [0] + list(accumulate(nums))

        def cost(l, i, r): # 把 nums[l:r+1] 變成 nums[i]，所需要的 cost
            d1 = (i - l) * nums[i] - (pre_sum[i] - pre_sum[l])
            d2 = (pre_sum[r+1] - pre_sum[i+1]) - (r - i) * nums[i]
            return d1 + d2
        
        # Sliding Window
        ans = 0
        left = 0
        for right in range(n):
            while cost(left, (left+right)//2, right) > k :
                left += 1
            ans = max(ans, right - left + 1) # 更新答案的最大長度
        return ans