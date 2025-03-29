#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        cnt = Counter(s)

        # most_common(k) 取出頻率最高的 k 個元素，返回的 是[(element, number), ...] ，所以要取[0][1]
        mx = cnt.most_common(1)[0][1]
        if mx > (n + 1) // 2:
            return ""
        
        # 用 m 個 bucket 來存放 element
        buckets = [[] for _ in range(mx)]
        idx = 0
        for ch, v in cnt.most_common():
            for _ in range(v):
                buckets[idx].append(ch)
                idx = (idx + 1) % mx  # 填入不同idx的bucket中，循環填入
        return "".join(["".join(bucket) for bucket in buckets])
        
class Solution2:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        cnt = Counter(s)

        # 找出出現次數最多的字元，判斷是否能重組
        ch, mx = cnt.most_common(1)[0]
        if mx > (n + 1) // 2:
            return ""
        
        # 先填入出現次數最多的字元
        ans = [''] * n
        i = 0
        for _ in range(mx):
            ans[i] = ch
            i += 2
        del cnt[ch]

        # 填入其他字元，注意當偶數位填滿時，要從奇數位開始填
        for ch, v in cnt.items():
            for _ in range(v):
                if i >= n:
                    i = 1
                ans[i] = ch
                i += 2
        return "".join(ans)
    
# Solution = Solution1
Solution = Solution2
# @lc code=end