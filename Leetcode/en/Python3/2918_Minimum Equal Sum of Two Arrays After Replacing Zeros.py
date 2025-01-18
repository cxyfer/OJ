# @algorithm @lc id=3171 lang=python3 
# @title minimum-equal-sum-of-two-arrays-after-replacing-zeros


from en.Python3.mod.preImport import *
# @test([3,2,0,1,0],[6,5,0])=12
# @test([2,0,2,0],[1,4])=-1
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        zero1, zero2 = nums1.count(0), nums2.count(0)
        print(sum1, sum2, zero1, zero2)
        if sum1 == sum2:
            if zero1 == zero2:
                return sum1 + zero1
            elif zero1 == 0 or zero2 == 0:
                return -1
            else:
                return sum1 + max(zero1, zero2)
        elif sum1 > sum2:
            if zero2 == 0:
                return -1
            elif zero1 == 0 and sum2 + zero2 > sum1:
                return -1
            else:
                return max(sum1+zero1, sum2+zero2)
        else:
            if zero1 == 0:
                return -1
            elif zero2 == 0 and sum1 + zero1 > sum2:
                return -1
            else:
                return max(sum1+zero1, sum2+zero2)