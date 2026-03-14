#
# @lc app=leetcode id=3296 lang=python3
# @lcpr version=30204
#
# [3296] Minimum Number of Seconds to Make Mountain Height Zero
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
1. 對答案二分搜尋

對於 workerTimes[i] = t 秒的工人，在 m 秒內可以降低的高度 x 為：
t + 2t + 3t + ... + xt <= m
t * (x * (x + 1) / 2) <= m
x^2 + x - (2m / t) <= 0
x <= (-1 + sqrt(1 + 8 * m / t)) / 2

對於二分搜尋的右邊界，可以假設所有工人皆為 max_t = max(workerTimes)，
則每個工人需要降低的高度皆為 h = ceil(mountainHeight / n)。
最少需要 max_t * (1 + 2 + ... + h) = max_t * h * (h + 1) / 2 秒。

2. 使用 Min Heap 模擬
由於是不同工人是同時降低高度，因此哪個工人先降低高度是確定的，
因此可以使用 Min Heap 模擬每次高度降低時是由哪個工人降低的，並更新堆積中的資訊。
最後一次降低時的時間即為答案。
"""
class Solution1:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(m: int) -> bool:
            tot = 0
            for t in workerTimes:  # 枚舉每個工人，計算工人可以降低的高度
                tot += (-1 + math.isqrt(1 + 8 * m // t)) // 2
                if tot >= mountainHeight:
                    return True
            return False

        # 更精妙的計算上界
        h = math.ceil(mountainHeight / len(workerTimes))
        left = 0
        right = max(workerTimes) * h * (h + 1) // 2
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution2:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        hp = [(t, t, 1) for t in workerTimes]
        heapify(hp)
        for _ in range(mountainHeight):
            t, d, m = hp[0]
            m += 1
            heapreplace(hp, (t + d * m, d, m))
        return t

# Solution = Solution1
Solution = Solution2
# @lc code=end
sol = Solution()
print(sol.minNumberOfSeconds(4, [2,1,1]))  # 3

#
# @lcpr case=start
# 4\n[2,1,1]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[3,2,2,4]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[1]\n
# @lcpr case=end

#

