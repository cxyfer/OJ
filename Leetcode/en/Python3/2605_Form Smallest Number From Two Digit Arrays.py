# @algorithm @lc id=2668 lang=python3 
# @title form-smallest-number-from-two-digit-arrays


from en.Python3.mod.preImport import *
# @test([4,1,3],[5,7])=15
# @test([3,5,2,6],[3,1,7])=3
class Solution1:
    """
        如果nums1和nums2有交集，則可生成的最小數字為交集中的最小數字
        若nums1和nums2沒有交集，則返回由nums1和nums2中的最小數字組成的最小數字
        1. 用python的set來判斷是否有交集
    """
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        intersection = set(nums1) & set(nums2)
        if intersection:
            return min(intersection)
        else:
            a = min(nums1)
            b = min(nums2)
        return min(a*10+b, b*10+a)
class Solution2:
    """
        2. 用位元運算來判斷是否有交集
    """
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        def number_of_trailing_zeros(n):
            count = 0
            while n % 2 == 0:  #檢查最後一位是否為0
                count += 1
                n //= 2  # 右移一位
            return count
        mask1 = mask2 = 0
        for i in nums1:
            mask1 |= 1 << i
        for i in nums2:
            mask2 |= 1 << i
        if mask1 & mask2:
            return number_of_trailing_zeros(mask1 & mask2)
        else:
            x = number_of_trailing_zeros(mask1)
            y = number_of_trailing_zeros(mask2)
            return min(x*10+y, y*10+x)
class Solution(Solution1):
    ...