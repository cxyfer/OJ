# You are given two arrays nums1 and nums2 consisting of positive integers.

# You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

# Return the minimum equal sum you can obtain, or -1 if it is impossible.

from typing import List

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

sol = Solution()
print(sol.minSum([3,2,0,1,0], [6,5,0])) # 12
print(sol.minSum([2,0,2,0], [1,4])) # -1
print(sol.minSum([20,0,18,11,0,0,0,0,0,0,17,28,0,11,10,0,0,15,29], [16,9,25,16,1,9,20,28,8,0,1,0,1,27])) # 169