"""
P8792 [蓝桥杯 2022 国 A] 最大公约数
https://www.luogu.com.cn/problem/P8792

枚舉 / 雙指標 + 資料結構

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
"""
import math

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

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    if (cnt1 := nums.count(1)) > 0:
        print(n - cnt1)
        return
    ans = float('inf')
    st = SparseTable(nums, math.gcd)
    i = 0  # Two pointers
    for j in range(n):
        while i < j and st.query(i, j) == 1:
            i += 1
        # 找到以 j 為右端點且區間 gcd 為 1 的最小區間 [i - 1, j]
        if i > 0 and st.query(i - 1, j) == 1:
            ans = min(ans, j - i + n)
    print(ans if ans != float('inf') else -1)

if __name__ == "__main__":
    solve()