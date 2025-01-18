#
# @lc app=leetcode id=2286 lang=python3
# @lcpr version=30204
#
# [2286] Booking Concert Tickets in Groups
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class SegmentTree:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.n = n
        self.nums = [0] + nums # 讓 index 從 1 開始
        self.tree = [[0, 0]] * (1 << (n.bit_length() + 1)) # (sum, max)
        self.build(1, 1, n)
 
    def build(self, o, left, right): # node, left, right
        if left == right: # Leaf node initialization
            self.tree[o] = [0, 0]
            self.tree[o][0] = self.nums[left]
            self.tree[o][1] = self.nums[left]
            return
        mid = (left + right) // 2
        self.build(2*o, left, mid) # left child
        self.build(2*o+1, mid + 1, right) # right child
        self.tree[o] = self.merge(self.tree[2*o], self.tree[2*o+1], left, mid, right)

    # 合併 [left, mid] 和 [mid+1, right] 兩部分的結果
    def merge(self, left_part, right_part, left, mid, right):
        res = [0, 0]
        res[0] = left_part[0] + right_part[0]
        res[1] = max(left_part[1], right_part[1])
        return res

    # 單點更新，增加 val 的值
    def update(self, o, left, right, idx, val):
        if left == right:
            self.nums[idx] += val
            self.tree[o][0] += val
            self.tree[o][1] += val
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
    
    # 在區間 [l, r] 中，找到第一個剩餘座位數 >= k 的橫排
    def query_first(self, o, left, right, l, r, k):
        if self.tree[o][1] < k: # 整個區間的最大值都 < k，不可能滿足條件
            return -1
        if left == right: # 到達葉子節點，則返回當前節點的 index
            return left
        mid = (left + right) // 2
        if l <= mid and self.tree[2*o][1] >= k: # 左子樹的最大值 >= k，則只需要查詢左子樹
            return self.query_first(2*o, left, mid, l, r, k)
        if r > mid:
            return self.query_first(2*o+1, mid+1, right, l, r, k)
        return -1

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        seats = [m] * n # 初始化為 n 個橫列都有 m 個座位
        self.st = SegmentTree(seats) # 維護剩餘座位數的總和以及最大值

    def gather(self, k: int, maxRow: int) -> List[int]:
        # 從第 1 橫列開始找，直到找到一橫列的剩餘座位數 >= k
        r = self.st.query_first(1, 1, self.n, 1, maxRow + 1, k)
        if r == -1:
            return []
        c = self.m - self.st.query(1, 1, self.n, r, r)[0]
        self.st.update(1, 1, self.n, r, -k) # 更新剩餘座位數
        return [r-1, c]

    def scatter(self, k: int, maxRow: int) -> bool:
        # 先檢查在 [1, maxRow + 1] 橫列的剩餘座位數總和，若小於 k，則無法滿足條件
        if self.st.query(1, 1, self.n, 1, maxRow + 1)[0] < k:
            return False
        # 從第一個有空位的橫排開始，逐個橫排填入座位
        while k > 0:
            r = self.st.query_first(1, 1, self.n, 1, maxRow + 1, 1) # 找到第一個有空位的橫排
            c = self.st.query(1, 1, self.n, r, r)[0] # 當前橫排的剩餘座位數
            left = min(c, k) # 需要使用的座位數
            self.st.update(1, 1, self.n, r, -left) # 更新剩餘座位數
            k -= left
        return True

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)
# @lc code=end
obj = BookMyShow(2, 5)
print(obj.gather(4, 0)) # [0, 0]
print(obj.gather(2, 0)) # []
print(obj.scatter(5, 1)) # True
print(obj.scatter(5, 1)) # False