#
# @lc app=leetcode id=321 lang=python3
# @lcpr version=30201
#
# [321] Create Maximum Number
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Similar to 402. Remove K Digits
        將問題轉換成從兩個陣列中分別選擇最大的 k1 和 k2 個數字，再合併成最大的數字
    """
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def pick(nums, k): # 從 nums 中選擇 k 個數字，使其最大
            st = []
            d = len(nums) - k # 要刪除的數字個數
            for x in nums:
                while d and st and st[-1] < x: # 前面的數字比較小，且還有剩餘的數字可以刪
                    st.pop()
                    d -= 1
                st.append(x)
            return st[:k]
        
        ans = []
        m, n = len(nums1), len(nums2)
        for k1 in range(k+1):
            k2 = k - k1
            if k1 > m or k2 > n: continue
            mx1, mx2 = pick(nums1, k1), pick(nums2, k2)
            cur = []
            while mx1 or mx2:
                bigger = mx1 if mx1 > mx2 else mx2
                cur.append(bigger[0])
                bigger.pop(0)
            ans = max(ans, cur)
        return ans
# @lc code=end



#
# @lcpr case=start
# [3,4,6,5]\n[9,1,2,5,8,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [6,7]\n[6,0,4]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,9]\n[8,9]\n3\n
# @lcpr case=end

#

