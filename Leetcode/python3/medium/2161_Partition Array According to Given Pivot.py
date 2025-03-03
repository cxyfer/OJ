#
# @lc app=leetcode.cn id=2161 lang=python3
# @lcpr version=30204
#
# [2161] 根据给定数字划分数组
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        p1, p2, p3 = [], [], []
        for x in nums:
            if x < pivot:
                p1.append(x)
            elif x == pivot:
                p2.append(x)
            else:
                p3.append(x)
        return p1 + p2 + p3

class Solution2:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = [pivot] * n
        l, r = 0, n - 1
        for x in nums:
            if x < pivot:
                ans[l] = x
                l += 1
            elif x > pivot:
                ans[r] = x
                r -= 1
        ans[r + 1:] = ans[n - 1:r:-1]  # 翻轉 > pivot 的元素
        return ans

class Solution3:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = [pivot] * n
        l, r = 0, n - 1
        for x, y in zip(nums, nums[::-1]):
            if x < pivot:
                ans[l] = x
                l += 1
            if y > pivot:
                ans[r] = y
                r -= 1
        return ans

# class Solution(Solution1):
# class Solution(Solution2):
# class Solution(Solution3):
    pass
# @lc code=end


#
# @lcpr case=start
# [9,12,5,10,14,3,10]\n10\n
# @lcpr case=end

# @lcpr case=start
# [-3,4,3,2]\n2\n
# @lcpr case=end

#
