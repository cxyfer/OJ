#
# @lc app=leetcode id=3748 lang=python3
#
# [3748] Count Stable Subarrays
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 離線 + 掃描線 + 線段樹

注意到穩定子陣列是一段非遞減的子陣列，因此可以將給定的陣列分段。
在每一段中添加新的元素作為右端點時，可以與本段中其他元素組成穩定子陣列，貢獻為加入前的本段元素數量。
考慮按照詢問的右端點分組，枚舉右端點，維護每個位置作為左端點對答案的貢獻，
由於維護貢獻需要對區間進行加法操作，以及需要維護區間和，可以使用線段樹來維護。

2. 分段計算 + 前綴和
對於每一個長度為 ln 非遞減段，可以在其中任選兩個元素作為左端點和右端點，故其貢獻為 ln * (ln + 1) // 2。

每個詢問只會有兩種情況：
1. 詢問的左右端點在同一個非遞減段內，以詢問的區間長度計算貢獻即可。
2. 詢問的左右端點跨非遞減段，分成三部分計算：
   - 左端點到第一段末尾的貢獻
   - 最後一段開頭到右端點的貢獻
   - 中間由多個非遞減段組成，可以用前綴和預處理計算貢獻

3. 分段計算 + 前綴和

> https://leetcode.cn/problems/count-stable-subarrays/solutions/3832945/fen-duan-er-fen-cha-zhao-qian-zhui-he-py-ukgs/

令 f[i] 表示以 i 為右端點的穩定子陣列數量，則有：
- f[i] = f[i-1] + 1 如果 nums[i-1] <= nums[i]
- 否則 f[i] = 1

如果我們可以保證 f[l] 到 f[r] 間的貢獻僅由 [l, r] 內的元素提供，則可以通過前綴和快速計算貢獻。
為此我們需要確保 l 是非遞減段的起始位置，但注意不用確保 r 是遞減段的結束位置。
預處理 nxt[i] 表示下一個非遞減段的起始位置，則可以將詢問分成 [l, nxt[l]) 和 [nxt[l], r] 兩部分計算。
"""
# @lc code=start
class SegmentTree:
    def __init__(self, nums: List[int] = None):
        if isinstance(nums, int):
            nums = [0] * nums
        self.n = len(nums)
        self.tree = [0] * (1 << (self.n.bit_length() + 1))
        self.lazy = [0] * (1 << (self.n.bit_length() + 1))
        if nums is not None and len(nums) > 0:
            self.build(1, 1, self.n, nums)

    def update(self, l: int, r: int, v: int) -> None:
        self._update(1, 1, self.n, l, r, v)

    def query(self, l: int, r: int) -> int:
        return self._query(1, 1, self.n, l, r)

    def build(self, o, left, right, nums: List[int]) -> None:
        if left == right:  # Leaf node initialization
            self.tree[o] = nums[left - 1]
            return
        mid = (left + right) // 2
        self.build(o << 1, left, mid, nums)  # left child
        self.build(o << 1 | 1, mid + 1, right, nums)  # right child
        self.pushup(o)

    # update the range [l, r] with value v
    def _update(self, o, left, right, l, r, v) -> None:
        if l <= left and right <= r:
            # apply lazy tag
            self.apply(o, left, right, v)
            return
        self.pushdown(o, left, right)  # push down lazy tags
        mid = (left + right) // 2
        if l <= mid:
            self._update(o << 1, left, mid, l, r, v)
        if r > mid:
            self._update(o << 1 | 1, mid + 1, right, l, r, v)
        self.pushup(o)  # push up node value

    # apply lazy tag
    def apply(self, o, left, right, v) -> None:
        self.tree[o] += v * (right - left + 1)
        self.lazy[o] += v

    # query the range [l, r]
    def _query(self, o, left, right, l, r) -> int:
        if l <= left and right <= r:
            return self.tree[o]
        # Ensure all lazy tags have been pushed down
        self.pushdown(o, left, right)
        mid = (left + right) // 2
        ans = 0
        if l <= mid:
            ans += self._query(o << 1, left, mid, l, r)
        if r > mid:
            ans += self._query(o << 1 | 1, mid + 1, right, l, r)
        return ans

    # push down lazy tags
    def pushdown(self, o, left, right) -> None:
        if self.lazy[o] != 0:
            # apply lazy tag
            mid = (left + right) // 2
            self.apply(o << 1, left, mid, self.lazy[o])
            self.apply(o << 1 | 1, mid + 1, right, self.lazy[o])
            # reset lazy tag
            self.lazy[o] = 0

    # push up node value
    def pushup(self, o) -> None:
        # update node value
        self.tree[o] = self.tree[o << 1] + self.tree[o << 1 | 1]

class Solution1:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        qs = [[] for _ in range(n + 1)]  # 將詢問按照右端點分組
        for qid, (l, r) in enumerate(queries):
            qs[r + 1].append((qid, l + 1))  # 1-based
            
        # tree[i] 表示以 i 為左端點的穩定子陣列數量
        seg = SegmentTree(n)

        ans = [0] * len(queries)
        st = 0  # 每個非遞減段的開頭
        prev = float('inf')  
        for r, x in enumerate(nums, start=1):  # 枚舉右端點
            if prev > x:  # 遇到新的非遞減段
                st = r
            prev = x

            seg.update(l=st, r=r, v=1)  # 當前的右端點，會對 tree[st] ~ tree[r] 產生 1 的貢獻
            for qid, l in qs[r]:
                ans[qid] = seg.query(l=l, r=r)
        return ans

class Solution2:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        segs = []  # 每個非遞減段的起始和結束位置
        pos = [-1] * n  # 每個位置所在的非遞減段索引
        st = 0  # 當前非遞減段的起始位置
        for i, x in enumerate(nums):
            if i > 0 and nums[i-1] > x:
                segs.append((st, i - 1))
                st = i
            pos[i] = len(segs)
        segs.append((st, n - 1))

        # 根據每個非遞減段，計算其貢獻值的前綴和
        m = len(segs)
        s = [0] * (m + 1)
        for i, (l, r) in enumerate(segs):
            ln = r - l + 1
            s[i + 1] = s[i] + ln * (ln + 1) // 2

        ans = [0] * len(queries)
        for qid, (l, r) in enumerate(queries):
            pl, pr = pos[l], pos[r]
            if pl == pr:  # 在同一個非遞減段內
                ln = r - l + 1
                ans[qid] = ln * (ln + 1) // 2
            else:  # 跨非遞減段，分成三部分計算
                L = segs[pl][1] - l + 1
                R = r - segs[pr][0] + 1
                ans[qid] = s[pr] - s[pl + 1] + L * (L + 1) // 2 + R * (R + 1) // 2
        return ans


class Solution3:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        f = [0] * n  # f[i] 表示以 i 為右端點的穩定子陣列數量
        for i, x in enumerate(nums):
            if i > 0 and nums[i-1] > x:
                f[i] = 1
            else:
                f[i] = f[i-1] + 1
        s = list(accumulate(f, initial=0))
        
        nxt = [n] * n  # nxt[i] 表示下一個非遞減段的起始位置
        for i in range(n - 2, -1, -1):
            nxt[i] = nxt[i + 1] if nums[i] <= nums[i + 1] else i + 1

        ans = [0] * len(queries)
        for qid, (l, r) in enumerate(queries):
            if nxt[l] > r:  # 在同一個非遞減段內
                ln = r - l + 1
                ans[qid] = ln * (ln + 1) // 2
            else:  # 跨非遞減段，分成兩部分計算
                # 分成 [l, nxt[l]) 和 [nxt[l], r] 兩部分
                ln = nxt[l] - l
                ans[qid] = ln * (ln + 1) // 2 + s[r + 1] - s[nxt[l]]
        return ans

# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.countStableSubarrays([3,1,2], [[0,1],[1,2],[0,2]]))  # [2,3,4]
print(sol.countStableSubarrays([2,2], [[0,1],[0,0]]))  # [3,1]
print(sol.countStableSubarrays([7,6,16], [[2,2]]))  # [1]
