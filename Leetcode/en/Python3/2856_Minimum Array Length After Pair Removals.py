# @algorithm @lc id=3081 lang=python3 
# @title minimum-array-length-after-pair-removals


from en.Python3.mod.preImport import *
# @test([1,3,4,9])=0
# @test([2,3,6,9])=0
# @test([1,1,2])=1
class Solution:
    """
        討論
        1. 出現次數最多的數字超過一半 (cx > n/2)，不能全部抵銷
        2. 出現次數最多的數字不超過一半 (cx <= n/2)，若n為偶數可以全部抵銷
            a. Counter.most_common(1) 取出出現次數最多的數字
                Time complexity: O(n)
            b. 用Binary Search 確定出現次數最多的數字有沒有超過一半
                Time complexity: O(logn)
    """
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        # cnt = Counter(nums)
        # cx = cnt.most_common(1)[0][1]
        x = nums[n // 2] # median
        cx = bisect_right(nums, x) - bisect_left(nums, x)
        if cx > n // 2:
            return cx * 2 - n # n - (n-cx) * 2
        else:
            return 0 if n % 2 == 0 else 1