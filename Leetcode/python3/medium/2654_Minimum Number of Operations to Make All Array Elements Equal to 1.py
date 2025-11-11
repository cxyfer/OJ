#
# @lc app=leetcode id=2654 lang=python3
#
# [2654] Minimum Number of Operations to Make All Array Elements Equal to 1
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
枚舉 / 雙指標 + 資料結構 / LogTrick

如果 nums 中存在 1，那麼可以用 1 來更新其他元素，因此答案為 n - cnt1
否則我們需要找到一個區間，使得區間內的 gcd 為 1，那麼我們可以用這個 1 來更新其他元素。
如果區間的大小為 sz，則需要 sz - 1 次操作來產生這個 1，又需要 n - 1 次操作來透過這個 1 來更新其他元素。
因此答案為 sz - 1 + n - 1 = sz + n - 2。

顯然我們可以枚舉右端點 r ，然後往左計算 gcd，找到最大的左端點 l 使得區間 gcd 為 1，然後計算答案。
但這需要 O(n(n + log U)) 的時間複雜度，其中 U 是 nums 中的最大值。

注意到當右端點從 r - 1 移動到 r 時，如果區間 [l, r - 1] 的 gcd 為 1，則區間 [l, r] 的 gcd 也必定為 1。
故只需要從 l 開始往右找到最後一個使 [l', r] 的 gcd 為 1 的位置即可。
但由於 gcd 是不可減的，因此需要使用 線段樹/ST表 等資料結構來維護區間的 gcd。
時間複雜度為 O(n log n)。

也能使用 LogTrick 來維護以 r 為右端點的所有區間 gcd 值，對於同樣的 gcd 值只保留左端點最大的。
由於以 r 為右端點的區間 gcd 值最多有 log U 種，因此時間複雜度為 O(n log U)。
"""
# @lc code=start
class Solution1:
    def minOperations(self, nums: List[int]) -> int:
        if reduce(math.gcd, nums) != 1:
            return -1
        n = len(nums)
        if (cnt1 := nums.count(1)) > 0:
            return n - cnt1
        ans = float('inf')
        for i, x in enumerate(nums):
            g = x
            for j in range(i + 1, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    ans = min(ans, j - i + n - 1)
                    break
        return ans

class SparseTable:
    def __init__(self, data, merge_func):
        self.n = len(data)
        self.data = data
        self.merge = merge_func
        self.max_log = math.floor(math.log2(self.n)) if self.n > 0 else 0
        self.st = [[None] * (self.max_log + 1) for _ in range(self.n)]
        for i in range(self.n):
            self.st[i][0] = data[i]
        
        for j in range(1, self.max_log + 1):
            for i in range(self.n):
                self.st[i][j] = self.merge(self.st[i][j - 1], self.st[min(self.n - 1, i + (1 << (j - 1)))][j - 1])
    
    def query(self, L, R):
        k = math.floor(math.log2(R - L + 1))
        return self.merge(self.st[L][k], self.st[R - (1 << k) + 1][k])

class Solution2:
    def minOperations(self, nums: List[int]) -> int:
        if reduce(math.gcd, nums) != 1:
            return -1
        n = len(nums)
        if (cnt1 := nums.count(1)) > 0:
            return n - cnt1
        ans = float('inf')
        st = SparseTable(nums, math.gcd)
        i = 0  # Two pointers
        for j in range(n):
            while i < j and st.query(i, j) == 1:
                i += 1
            # 找到以 j 為右端點且區間 gcd 為 1 的最小區間 [i - 1, j]
            if i > 0 and st.query(i - 1, j) == 1:
                ans = min(ans, j - i + n)
        return ans

class Solution3:
    def minOperations(self, nums: List[int]) -> int:
        if reduce(math.gcd, nums) != 1:
            return -1
        n = len(nums)
        if (cnt1 := nums.count(1)) > 0:
            return n - cnt1
        ans = float('inf')
        gcds = []  # (區間 gcd，最大左端點)
        for r, x in enumerate(nums):
            # 維護以 r 為右端點的所有區間 gcd 值
            for p in gcds:
                p[0] = math.gcd(p[0], x)
            gcds.append([x, r])

            # 原地去重，相同 gcd 值只保留左端點最大的
            idx = 1
            for j in range(1, len(gcds)):
                if gcds[j][0] != gcds[idx - 1][0]:
                    gcds[idx] = gcds[j]
                    idx += 1
                else:
                    gcds[idx - 1][1] = gcds[j][1]
            del gcds[idx:]

            if gcds[0][0] == 1:
                ans = min(ans, r - gcds[0][1] + n - 1)
        return ans

# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

sol = Solution()
print(sol.minOperations([6,10,15]))  # 4
print(sol.minOperations([2,6,3,4]))  # 4