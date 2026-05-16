#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
和 153. Find Minimum in Rotated Sorted Array 相比，需要考慮重複元素
最主要的問題是當 nums[mid] == nums[-1] 時，無法判斷最小值在 mid 的左側還是右側

T: 最小值在 mid 的左側或 mid 是最小值本身
F: 最小值在 mid 的右側

有兩種處理方式：

### 1. 改成與 nums[right + 1] 的比較，且當遇到重複元素時，將 right 向左移動一格

以下用閉區間 [left, right] 來說明，初始時 right = n - 2。
由於最小值一定在 nums[-1] 左側或是 nums[-1] 本身，我們正是利用這個性質來透過與 nums[-1] 的比較來判斷最小值的位置，
而在二分的過程中，right + 1 也滿足這個性質，因此可以改成與 nums[right + 1] 的比較。
那麼當遇到與 nums[mid] == nums[right + 1] 時，我們就可以將 right 向左移動。
此時 nums[mid] 的位置可能在前綴或後綴重複元素中，而 nums[right + 1] 可能是最小值或並非最小值，考慮這 2 * 2 種情況，可以證明移動 right 後不影響區間的性質，且不會錯過最小值。

### 2. 在二分前先移除前綴的重複元素

在把 153 改成允許重複後，只有前綴中與 nums[-1] 相同的元素會導致判斷錯誤，移除這些元素即可。
後綴中的相同元素在 <= 的條件下，不會影響二分的性質。

我比較喜歡這種方式，一是不用更改比較對象，二是如果題目能保證每個元素最多重複 k 次，那麼以上作法為 O(k + log n)。
"""
# @lc code=start
class Solution1:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        left, right = 0, n - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == nums[right + 1]:
                right -= 1
            elif nums[mid] < nums[right + 1]:  # 最小值是 mid 或在 mid 的左側
                right = mid - 1
            else:  # 只可能是兩段遞增，最小值一定在 mid 的右側
                left = mid + 1
        return nums[left]


class Solution2:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        n = len(nums)

        def check(mid: int) -> bool:
            return nums[mid] <= nums[-1]

        left, right = 0, n - 2
        while left <= right and nums[left] == nums[-1]:
            left += 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):  # 最小值是 mid 或在 mid 的左側
                right = mid - 1
            else:  # 只可能是兩段遞增，最小值一定在 mid 的右側
                left = mid + 1
        return nums[left]


Solution = Solution1
# Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.findMin([3, 4, 5, 1, 2]))  # 1
print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
print(sol.findMin([11, 13, 15, 17]))  # 11
print(sol.findMin([1]))  # 1
print(sol.findMin([3,1,3]))  # 1
