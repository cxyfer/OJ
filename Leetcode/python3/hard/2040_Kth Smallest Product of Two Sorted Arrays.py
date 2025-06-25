#
# @lc app=leetcode id=2040 lang=python3
#
# [2040] Kth Smallest Product of Two Sorted Arrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        i0 = bisect_left(nums1, 0)
        j0 = bisect_left(nums2, 0)
        def check(mx):
            cnt = 0
            # 右下區（從左上往右下遞增）
            j = m - 1
            for i in range(i0, n):
                while j >= j0 and nums1[i] * nums2[j] > mx:
                    j -= 1
                cnt += j - j0 + 1
            # 左上區（從右下往左上遞增）
            j = 0
            for i in range(i0 - 1, -1, -1):
                while j < j0 and nums1[i] * nums2[j] > mx:
                    j += 1
                cnt += j0 - j
            # 右上區（從右上往左下遞增）
            j = j0
            for i in range(0, i0):
                while j < m and nums1[i] * nums2[j] > mx:
                    j += 1
                cnt += m - j
            # 左下區（從左下往右上遞增）
            j = j0 - 1
            for i in range(n - 1, i0 - 1, -1):
                while j >= 0 and nums1[i] * nums2[j] > mx:
                    j -= 1
                cnt += j + 1
            return cnt >= k
        
        corners = [nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1]]
        left, right = min(corners), max(corners)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

class Solution2:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        i0 = bisect_left(nums1, 0)
        j0 = bisect_left(nums2, 0)
        pos1, neg1 = nums1[i0:], nums1[:i0]
        pos2, neg2 = nums2[j0:], nums2[:j0]
        below0 = len(neg1) * len(pos2) + len(pos1) * len(neg2)
        def cal(arr1, arr2, mx):
            cnt = 0
            j = len(arr2) - 1
            for x in arr1:
                while j >= 0 and x * arr2[j] > mx:
                    j -= 1
                cnt += j + 1
            return cnt
        def check(mx):
            if mx >= 0:  # 一定包含全部的左下跟右上，只需要檢查左上跟右下
                return below0 + cal(neg1[::-1], neg2[::-1], mx) + cal(pos1, pos2, mx) >= k
            else:  # 只需要檢查左下跟右上
                return cal(pos1[::-1], neg2, mx) + cal(neg1, pos2[::-1], mx) >= k
        corners = [nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1]]
        left, right = min(corners), max(corners)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

# Solution = Solution1  
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.kthSmallestProduct([2,5], [3,4], 2)) # 8
print(sol.kthSmallestProduct([-4,-2,0,3], [2,4], 6)) # 0
print(sol.kthSmallestProduct([-2,-1,0,1,2], [-3,-1,2,4,5], 3)) # -6