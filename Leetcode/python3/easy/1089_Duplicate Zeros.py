#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)

        # i 為修改後最後一個元素在原始陣列中的位置，j 用來統計修改後的陣列長度
        i = j = 0
        while i < n:
            j += 2 if arr[i] == 0 else 1
            if j >= n:
                break
            i += 1
        j -= 1
        if j == n:  # 超過範圍，代表最後一個元素是0
            arr[j - 1] = 0
            j -= 2
            i -= 1
        while i >= 0:
            if arr[i] == 0:
                arr[j] = 0
                arr[j - 1] = 0
                j -= 2
            else:
                arr[j] = arr[i]
                j -= 1
            i -= 1
# @lc code=end

sol = Solution()
arr = [1,0,2,3,0,4,5,0]
sol.duplicateZeros(arr)
print(arr)
arr = [1,2,3]
sol.duplicateZeros(arr)
print(arr)
arr = [1,0,2,3,0,0,5,0]
sol.duplicateZeros(arr)
print(arr)