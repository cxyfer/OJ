#
# @lc app=leetcode id=3187 lang=python3
# @lcpr version=30203
#
# [3187] Peaks in Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. 維護峰值 + 使用 樹狀陣列/線段樹 維護區間內的峰值數量
      - 每次修改時，會變動的只有修改點以及其左右兩個點，總共三個位置
      - 透過更新這三個位置是否為峰值，來更新區間內的峰值數量
      - 查詢時，不能包含區間的頭尾，所以要查詢的區間為 [l+1, r-1]
"""

class FenwickTree: # PURQ (Point Update Range Query), 1-based, initialization: O(n)
    __slots__ = 'nums', 'tree'

    def __init__(self, nums: List[int]): # 下標從 1 開始
        n = len(nums)
        self.nums = nums
        tree = [0] * (n + 1) # 下標從 1 開始
        for i, x in enumerate(nums, 1): # initialization: O(n)
            tree[i] += x
            nxt = i + (i & -i) # 下一個關鍵區間的右端點
            if nxt <= n:
                tree[nxt] += tree[i]
        self.tree = tree

    def add(self, k: int, x: int) -> None: # 令 nums[k] += x
        k += 1
        while k < len(self.tree):
            self.tree[k] += x
            k += (k & -k)

    def update(self, k: int, x: int) -> None: # 令 nums[k] = x
        self.add(k, x - self.nums[k])
        self.nums[k] = x

    def sum(self, l: int, r: int) -> int: # 區間查詢 (區間求和): 求 nums[l] 到 nums[r] 之和
        if l > r: # 本題中會出現 l > r 的情況
            return 0
        return self.preSum(r+1) - self.preSum(l)

    def preSum(self, k: int) -> int: # 求前綴和: 求 nums[0] 到 nums[k] 的區間和
        s = 0
        while k > 0:
            s += self.tree[k]
            k &= k - 1 # 等同 k -= (k & -k)
        return s
 
class Solution1:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        # peaks[i] = 1 if nums[i-1] < nums[i] > nums[i+1]
        peaks = [0] + [1 if nums[i-1] < nums[i] > nums[i+1] else 0 for i in range(1, n-1)] + [0]
        bit = FenwickTree(peaks)
        ans = []
        for op, *args in queries:
            if op == 1:
                l, r = args
                ans.append(bit.sum(l+1, r-1)) # 不包含頭尾
            else:
                idx, val = args
                nums[idx] = val
                for i in range(idx-1, idx+2): # 更新 idx-1, idx, idx+1 三個位置
                    if i <= 0 or i >= n-1:
                        continue
                    if nums[i-1] < nums[i] > nums[i+1]: # 現在是峰值
                        if bit.nums[i] == 0: # 之前不是峰值
                            bit.update(i, 1)
                    else: # 現在不是峰值
                        if bit.nums[i] == 1: # 之前是峰值
                            bit.update(i, 0)
        return ans

"""
    2. 使用線段樹以區間合併的方式維護區間內的峰值數量
      - 兩個區間合併時，會新增的峰值為左區間的最後一個元素和右區間的第一個元素
      - 透過檢查這兩個元素是否為峰值，來更新合併後的區間的峰值數量
"""
class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.nums = [0] + nums # 讓 index 從 1 開始
        self.tree = [0 for _ in range(4 * n)]
        self.build(1, 1, n)
 
    def build(self, o, left, right): # node, left, right
        if left == right: # Leaf node initialization
            self.tree[o] = 0
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid) # left child
        self.build(2*o+1, mid + 1, right) # right child
        self.tree[o] = self.merge(self.tree[2*o], self.tree[2*o+1], left, mid, right)

    # 合併 [left, mid] 和 [mid+1, right] 兩部分的結果
    def merge(self, left_part, right_part, left, mid, right):
        res = left_part + right_part
        # if right - left < 2: # 區間內需要至少有三個元素才能形成峰值
        #     return res
        # 檢查 mid 和 mid+1 是否為峰值，因為這兩種情況是互斥的，最多只會有一個成立，所以可以用 or 來合併
        if mid - 1 >= left and self.nums[mid-1] < self.nums[mid] > self.nums[mid+1] \
            or mid + 2 <= right and self.nums[mid] < self.nums[mid+1] > self.nums[mid+2]:
            res += 1
        return res

    def update(self, o, left, right, idx, val):
        if left == right:
            self.nums[idx] = val
            self.tree[o] = 0
            return
        mid = (left + right) // 2
        if idx <= mid:
            self.update(2*o, left, mid, idx, val)
        else:
            self.update(2*o+1, mid + 1, right, idx, val)
        self.tree[o] = self.merge(self.tree[2*o], self.tree[2*o+1], left, mid, right)
 
    def query(self, o, left, right, l, r):
        if left == l and r == right:
            return self.tree[o]
        mid = (left + right) // 2
        if r <= mid: # 只需要查詢左半部分
            return self.query(2*o, left, mid, l, r)
        if mid < l: # 只需要查詢右半部分
            return self.query(2*o+1, mid + 1, right, l, r)
        left_part = self.query(2*o, left, mid, l, mid)
        right_part = self.query(2*o+1, mid+1, right, mid+1, r)
        return self.merge(left_part, right_part, l, mid, r) # 合併左右兩部分
    
class Solution2:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg = SegmentTree(nums)
        ans = []
        for op, *args in queries:
            if op == 1:
                l, r = args
                ans.append(seg.query(1, 1, n, l+1, r+1))
            else:
                idx, val = args
                seg.update(1, 1, n, idx+1, val)
        return ans
    
class Solution(Solution1):
    pass
# class Solution(Solution2):
#     pass
# @lc code=end

sol = Solution()
print(sol.countOfPeaks([3,1,4,2,5], [[2,3,4],[1,0,4]])) # [0]
print(sol.countOfPeaks([4,1,4,2,1,5], [[2,2,4],[1,0,2],[1,0,4]])) # [0,1]
print(sol.countOfPeaks([4,5,5], [[1,2,2],[1,0,1],[1,1,2]])) # [0, 0, 0]
print(sol.countOfPeaks([7,10,7], [[1,2,2],[2,0,6],[1,0,2]])) # [0, 1]
print(sol.countOfPeaks([4,8,7,7,6,9], [[1,5,5],[1,2,4],[1,0,0]])) # [0, 0, 0]
print(sol.countOfPeaks([10,5,10,3,7], [[2,4,2],[1,1,4],[1,1,3],[1,2,2]])) # [1, 1, 0]

#
# @lcpr case=start
# [3,1,4,2,5]\n[[2,3,4],[1,0,4]]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,4,2,1,5]\n[[2,2,4],[1,0,2],[1,0,4]]\n
# @lcpr case=end

#

