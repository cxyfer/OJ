#
# @lc app=leetcode id=3171 lang=python3
# @lcpr version=30204
#
# [3171] Find Subarray With Bitwise OR Closest to K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    Similar to 1521. Find a Value of a Mysterious Function Closest to Target
    OR 只會讓數字變大，所以可以用 Stack 來保存所有可能的 OR 結果
    改過題目，賽時是 AND ，即 1521 題。

    賽時寫的是線段樹二分，Python 會超時，C++ 可以過。
"""
class Solution1:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        st = []
        ans = float('inf')
        for x in nums: # 枚舉右端點
            st2 = [x] # 保存以 x 為右端點的所有 OR 結果，注意由於 OR 的性質，這裡的 st2 是遞增的
            for y in st:
                if x | y != st2[-1]:
                    st2.append(x | y)
            st = st2
            for y in st:
                ans = min(ans, abs(k - y))
        return ans
    
class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        n = len(nums)
        self.k = k
        self.nums = [0] + nums # 讓 index 從 1 開始
        self.tree = [0 for _ in range(4 * n)] # (OR)
        self.build(1, 1, n)

    def build(self, o, left, right): # node, left, right
        if left == right: # Leaf node initialization
            self.tree[o] = self.nums[left]
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid)
        self.build(2*o+1, mid + 1, right)
        self.tree[o] = self.merge(2*o, 2*o+1)

    def merge(self, left_child, right_child):
        return self.tree[left_child] | self.tree[right_child]

    def query(self, o, left, right, l, r):
        if l <= left and right <= r:
            return self.tree[o]
        mid = (left + right) // 2
        ans = 0
        if l <= mid:
            ans |= self.query(2*o, left, mid, l, r)
        if r > mid:
            ans |= self.query(2*o+1, mid + 1, right, l, r)
        return ans
 
class Solution2:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seg = SegmentTree(nums, k)
        ans = float('inf')
        for i in range(1, n+1): # 枚舉左端點
            left, right = i, n
            while left <= right:
                mid = (left + right) // 2
                if seg.query(1, 1, n, i, mid) >= k:
                    right = mid - 1
                else:
                    left = mid + 1
            ans = min(ans, abs(seg.query(1, 1, n, i, left) - k))
            if right >= i:
                ans = min(ans, abs(k - seg.query(1, 1, n, i, right)))
        return ans
    
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.minimumDifference([1,2,4,5], 3)) # 0
print(sol.minimumDifference([1,3,1,3], 2)) # 1
print(sol.minimumDifference([1], 10)) # 9
print(sol.minimumDifference([42,49,95,76,66], 12)) # 30

#
# @lcpr case=start
# [1,2,4,5]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,3,1,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n10\n
# @lcpr case=end

#

