# You are given two 0-indexed integer arrays, nums1 and nums2, both having length n.

# You are allowed to perform a series of operations (possibly none).

# In an operation, you select an index i in the range [0, n - 1] and swap the values of nums1[i] and nums2[i].

# Your task is to find the minimum number of operations required to satisfy the following conditions:

# nums1[n - 1] is equal to the maximum value among all elements of nums1, i.e., nums1[n - 1] = max(nums1[0], nums1[1], ..., nums1[n - 1]).
# nums2[n - 1] is equal to the maximum value among all elements of nums2, i.e., nums2[n - 1] = max(nums2[0], nums2[1], ..., nums2[n - 1]).
# Return an integer denoting the minimum number of operations needed to meet both conditions, or -1 if it is impossible to satisfy both conditions.

from typing import List

class Solution:
    """
        考慮兩種情況
        - 換了最後一組
        - 沒換最後一組
    """
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        # 沒換最後一組
        if max(nums1) == nums1[-1] and max(nums2) == nums2[-1]:
            return 0
        # 交換最後一組
        tmp1, tmp2 = nums1[:], nums2[:]
        tmp1[-1], tmp2[-1] = tmp2[-1], tmp1[-1]
        if max(tmp1) == tmp1[-1] and max(tmp2) == tmp2[-1]:
            return 1
        # 由前往後，把大於最大值的數字換到另外一個陣列

        tmp1, tmp2 = nums1[:], nums2[:]
        # 先考慮 nums1
        ans1 = 0
        tmp1, tmp2 = nums1[:], nums2[:]
        mx1, mx2 = tmp1[-1], tmp2[-1]
        for i in range(n-1):
            if tmp1[i] > mx1:
                if tmp1[i] > mx2 or tmp2[i] > mx1:
                    ans1 = float('inf')
                    break
                ans1 += 1
        ans1 = ans1 if ans1 != 0 else float('inf')
        # 考慮 nums2
        ans2 = 0
        tmp1, tmp2 = nums1[:], nums2[:]
        mx1, mx2 = tmp1[-1], tmp2[-1]
        for i in range(n-1):
            if tmp2[i] > mx2:
                if tmp2[i] > mx1 or tmp1[i] > mx2:
                    ans2 = float('inf')
                    break
                ans2 += 1
        ans2 = ans2 if ans2 != 0 else float('inf')
        # 交換最後一組
        
        # 先考慮 nums1
        ans3 = 1
        tmp1, tmp2 = nums1[:], nums2[:]
        mx1, mx2 = tmp2[-1], tmp1[-1]
        for i in range(n-1):
            if tmp1[i] > mx1:
                if tmp1[i] > mx2 or tmp2[i] > mx1:
                    ans3 = float('inf')
                    break
                ans3 += 1
        ans3 = ans3 if ans3 != 1 else float('inf')
        # 考慮 nums2
        ans4 = 1
        tmp1, tmp2 = nums1[:], nums2[:]
        mx1, mx2 = tmp2[-1], tmp1[-1]
        for i in range(n-1):
            if tmp2[i] > mx2:
                if tmp2[i] > mx1 or tmp1[i] > mx2:
                    ans4 = float('inf')
                    break
                ans4 += 1
        ans4 = ans4 if ans4 != 1 else float('inf')
        print(ans1, ans2, ans3, ans4)
        ans = min(ans1, ans2, ans3, ans4)
        return ans if ans != float('inf') else -1

sol = Solution()

print(sol.minOperations([1,2,7], [4,5,3])) # 1
print(sol.minOperations([2,3,4,5,9], [8,8,4,4,4])) # 2
print(sol.minOperations([1,5,4], [2,5,3])) # -1

print(sol.minOperations([1,1,8,9], [1,7,1,1])) # 1
print(sol.minOperations([8,6,6,6,7,8], [5,8,8,8,7,7])) # 2

print(sol.minOperations([10,18,12,12], [19,6,5,12])) # -1