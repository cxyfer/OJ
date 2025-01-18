#
# @lc app=leetcode id=786 lang=python3
# @lcpr version=30201
#
# [786] K-th Smallest Prime Fraction
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        1. Custom sort
        2. Priority Queue(Heap)
    """
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # return self.solve1(arr, k)
        return self.solve2(arr, k)
    """
        1. Custom sort
        自定義分數的比較函數，構造出所有的分數，然後排序，返回第k個分數
    """
    def solve1(self, arr: List[int], k: int) -> List[int]:
        def cmp(x: List[int], y: List[int]) -> int:
            return -1 if x[0] * y[1] < x[1] * y[0] else 1 # a[0] / a[1] < b[0] / b[1] => a[0] * b[1] < a[1] * b[0]
        n = len(arr)
        ans = []
        for i in range(n):
            for j in range(i + 1, n):
                ans.append([arr[i], arr[j]])
        ans.sort(key=cmp_to_key(cmp))
        return ans[k-1]
    """
        2. Priority Queue(Heap)
        可以從範例一思考，最小的分數顯然是 arr[0] / arr[-1] ， 而這個分數又能構造出一個大一些的分數 arr[1] / arr[-1] 。

        我們就可以構造出一個 Heap ，首先將所有 arr[0] / arr[i] 加入Heap，
        每次取出最小的分數 arr[i] / arr[j]，然後將 arr[i+1] / arr[j] 加入優先佇列。
        從 Heap 中取出 k-1 次後，堆頂元素就是第 k 小的分數。

        由於 Python 的 heapq 不能自訂比較函數，所以我們需要創建一個Clasee Frac ，並在其內定義 __lt__ 方法。
    """
    def solve2(self, arr: List[int], k: int) -> List[int]:
        class Frac:
            def __init__(self, idx, idy, x, y):
                self.idx, self.idy = idx, idy # index
                self.x, self.y = x, y # value
            def __lt__(self, other):
                return self.x * other.y < self.y * other.x
        n = len(arr)
        hp = [Frac(0, i, arr[0], arr[i]) for i in range(1, n)]
        heapify(hp)
        for _ in range(k - 1):
            frac = heappop(hp)
            i, j = frac.idx, frac.idy
            if i + 1 < j: # 還可以構造出更大的分數
                heappush(hp, Frac(i + 1, j, arr[i + 1], arr[j]))
        return [hp[0].x, hp[0].y]
# @lc code=end



#
# @lcpr case=start
# [1,2,3,5]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,7]\n1\n
# @lcpr case=end

#

