#
# @lc app=leetcode id=3171 lang=python3
# @lcpr version=30204
#
# [3171] Find Subarray With Bitwise OR Closest to K
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
改過題目，賽時是 AND ，即 1521 題。
Similar to 1521. Find a Value of a Mysterious Function Closest to Target

1. LogTrick: O(n log U)
  a. Stack
    OR 只會讓數字變大，所以可以用 Stack 來保存所有可能的 OR 結果
  b. 原地更新

2. 滑動窗口 + 按位統計: O(n log U)
由於 OR 運算只會使結果變大，具有單調性。
因此在枚舉右端點 right 時，若左端點 left 使得 OR(nums[left...right]) >= k，則 OR(nums[left-1...right]) 只會更大。
因此我們可以維護一個窗口，使窗口內的 OR 結果是最大的 < k 的結果。

3. 滑動窗口 + Stack: O(n)
因為 OR 沒有逆運算，所以通常的滑動窗口沒辦法用 O(1) 來處理出窗口的情況。

但我們可以將窗口拆分成兩部分，分別用 Stack 和 right_or 來維護，
維護一個 Stack ，由上到下保存 OR(nums[i...bottom]), OR(nums[i+1...bottom]) 之結果，
另外維護一個 right_or，保存 OR(nums[bottom...right]) 。

此時計算窗口內的 OR 結果只需將 Stack 的 top 和 right_or 做 OR 運算即可；
出窗口時，也只需要 pop stack。但如果出窗口後 Stack 為空，則需要重新構建 Stack，並重置 right_or 。

4. 線段樹二分: O(n log n log n)
Python 會超時，C++ 可以過，這裡僅做參考用。
"""
# @lc code=start
class Solution1a:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        st = []
        ans = float('inf')
        for x in nums: # 枚舉右端點
            # 保存以 x 為右端點的所有 OR 結果，注意由於 OR 的性質，這裡的 st2 是遞增的
            st2 = [x]
            for y in st:
                if y | x != st2[-1]:
                    st2.append(y | x)
            # 更新答案
            for y in st2:
                ans = min(ans, abs(y - k))
            st = st2
        return ans

class Solution1b:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        # 枚舉右端點 i，在枚舉 i 時將 nums[j] 原地修改成 OR(nums[j...i])
        # 此時有 A_j ⊇ A_{j+1} ⊇ A_{j+2} ⊇ ... ⊇ A_i 的性質，即 A_{j+1} 是 A_j 的子集，以此類推
        for i, x in enumerate(nums):
            ans = min(ans, abs(x - k))
            for j in range(i - 1, -1, -1):
                # 如果 x 是 nums[j] 的子集，則 x 也會是 nums[j-1] 的子集，以此類推，故不用更新
                if nums[j] | x == nums[j]:
                    break
                nums[j] |= x
                ans = min(ans, abs(nums[j] - k))
        return ans
    
class Solution2:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        left = cur = 0
        cnt = [0] * 32
        for right, x in enumerate(nums):
            for b in range(32):
                if x & (1 << b):
                    cnt[b] += 1
                    if cnt[b] == 1:
                        cur |= 1 << b
            ans = min(ans, abs(cur - k))
            while left < right and cur >= k:
                for b in range(32):
                    if nums[left] & (1 << b):
                        cnt[b] -= 1
                        if cnt[b] == 0:
                            cur &= ~(1 << b)
                left += 1
                ans = min(ans, abs(cur - k))
        return ans
    
class Solution3a:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        # Stack 由上到下保存 OR(nums[i...bottom]), OR(nums[i+1...bottom]) 等結果
        st = [0]  # 加入哨兵，避免 st 為空
        left = right_or = 0
        for right, x in enumerate(nums):
            right_or |= x
            while left <= right and st[-1] | right_or >= k:
                ans = min(ans, (st.pop() | right_or) - k)
                left += 1
                # 重新構建 Stack
                if not st:
                    st.append(0)  # 哨兵
                    for i in range(right, left - 1, -1):
                        st.append(st[-1] | nums[i])
                    right_or = 0
            if left <= right:
                ans = min(ans, k - (st[-1] | right_or))
        return ans

class Solution3b:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = float('inf')
        # 原地使用 nums 作為 Stack，由上到下保存 OR(nums[i...bottom]), OR(nums[i+1...bottom]) 之結果
        left = bottom = right_or = 0
        for right, x in enumerate(nums):
            right_or |= x
            while left <= right and nums[left] | right_or >= k:
                ans = min(ans, (nums[left] | right_or) - k)
                left += 1
                # 重新構建 Stack
                if bottom < left:
                    for i in range(right - 1, left - 1, -1):
                        nums[i] |= nums[i + 1]
                    bottom = right
                    right_or = 0
            if left <= right:
                ans = min(ans, k - (nums[left] | right_or))
        return ans

class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        n = len(nums)
        self.k = k
        self.nums = [0] + nums  # 讓 index 從 1 開始
        self.tree = [0 for _ in range(4 * n)]  # (OR)
        self.build(1, 1, n)

    def build(self, o, left, right):  # node, left, right
        if left == right:  # Leaf node initialization
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

class Solution4:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seg = SegmentTree(nums, k)
        ans = float('inf')
        for i in range(1, n + 1):  # 枚舉左端點
            left, right = i, n
            while left <= right:
                mid = (left + right) // 2
                if seg.query(1, 1, n, i, mid) >= k:
                    right = mid - 1
                else:
                    left = mid + 1
            if left <= n:
                ans = min(ans, seg.query(1, 1, n, i, left) - k)
            if right >= i:
                ans = min(ans, k - seg.query(1, 1, n, i, right))
        return ans

# Solution = Solution1a
# Solution = Solution1b
# Solution = Solution2
Solution = Solution3a
# Solution = Solution3b
# @lc code=end

sol = Solution()
print(sol.minimumDifference([1,2,4,5], 3))  # 0
print(sol.minimumDifference([1,3,1,3], 2))  # 1
print(sol.minimumDifference([1], 10))  # 9
print(sol.minimumDifference([42,49,95,76,66], 12))  # 30
print(sol.minimumDifference([7,4], 2))  # 2

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

