#
# @lc app=leetcode id=3445 lang=python3
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
由於數字只有 5 個，因此可以直接枚舉 (a, b)，其中 a 是奇數頻率的字母，b 是偶數頻率的字母。
而統計區間內的某個數字數量不難想到前綴和，故題目等同求 (sa[i] - sa[j]) - (sb[i] - sb[j]) 的最大值，
可以改寫成 (sa[i] - sb[i]) - (sa[j] - sb[j])，整理後就是枚舉右維護左的題目。

但由於題目要求奇偶性，因此維護左以及更新答案的時候都需要分類討論。
具體來說是 sa[j] 需和 sa[i] 的奇偶性相反，sb[j] 需和 sb[i] 的奇偶性相同，
這裡用 state = ((sa[j] & 1) << 1) | (sb[j] & 1) 來維護四種情況的最小值。

另外需要注意，由於本題不允許空子陣列，而當 s[j] = s[i] 時，該字母會不在子字串中，這時左端點還不能加入。
這個剛好在範例 2 可以被測出來
"""
# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        nums = list(map(int, s))
        cnt = [0] * 5
        for x in nums:
            cnt[x] += 1

        ans = -inf
        for a in range(5):
            for b in range(5):
                if a == b or cnt[a] == 0 or cnt[b] == 0:
                    continue
                # min(sa[j] - sb[j])，且 (sa_j, sb_j) 的奇偶性分別為 (0, 0), (0, 1), (1, 0), (1, 1)
                min_sl = [inf] * 4
                sa = [0] * (n + 1)
                sb = [0] * (n + 1)
                left = 0
                for i, x in enumerate(nums, start=1):
                    sa[i] = sa[i - 1] + (x == a)
                    sb[i] = sb[i - 1] + (x == b)
                    while i - left >= k and sa[left] < sa[i] and sb[left] < sb[i]:
                        state = ((sa[left] & 1) << 1) | (sb[left] & 1)
                        min_sl[state] = min(min_sl[state], sa[left] - sb[left])
                        left += 1
                    # 因為 a 需要有奇數個，因此 sa[j] 的奇偶性需要與 sa[i] 相反
                    state = ((sa[i] & 1 ^ 1) << 1) | (sb[i] & 1)
                    ans = max(ans, sa[i] - sb[i] - min_sl[state])
        return ans  # 題目保證至少有一個合法的子字串
# @lc code=end

sol = Solution()
print(sol.maxDifference("12233", 4))  # -1
print(sol.maxDifference("1122211", 3))  # 1