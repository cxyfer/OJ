# @algorithm @lc id=3362 lang=python3 
# @title find-the-median-of-the-uniqueness-array


from en.Python3.mod.preImport import *
# @test([1,2,3])=1
# @test([3,4,3,4,5])=2
# @test([4,3,5,4])=2
class Solution:
    """ 二分搜尋 + 滑動窗口
        中位數 → 第 m 大/小的數 → 二分答案
    """
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        m = n * (n + 1) // 2 # 非空子陣列的數量
        k = (m + 1) // 2 # 中位數是第 k 小的數

        def check(upper: int) -> bool: # distinct 值 <= upper 的子陣列數量是否 >= k
            cnt = 0 # distinct 值 <= upper 的子陣列數量
            l = 0
            f = Counter()
            for r, inx in enumerate(nums):
                f[inx] += 1
                while len(f) > upper: # 當前子陣列的 distinct 值數量 > upper
                    out = nums[l]
                    f[out] -= 1
                    if f[out] == 0:
                        del f[out]
                    l += 1
                cnt += r - l + 1
                if cnt >= k:
                    return True
            return False
        # return bisect_left(range(len(set(nums))), True, 1, key=check)
        left, right = 1, len(set(nums))
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left