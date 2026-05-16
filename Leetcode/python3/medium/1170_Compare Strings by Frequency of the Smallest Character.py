#
# @lc app=leetcode id=1170 lang=python3
#
# [1170] Compare Strings by Frequency of the Smallest Character
#


# @lcpr-template-start
from preImport import *


# @lcpr-template-end
# @lc code=start
class Solution1:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            cnt = Counter(s)
            return cnt[min(cnt)]

        ans = []
        B = sorted(f(w) for w in words)
        for q in queries:
            idx = bisect_right(B, f(q))
            ans.append(len(B) - idx)
        return ans


class Solution2:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord("a")] += 1
            for i in range(26):
                if cnt[i] > 0:
                    return cnt[i]
            return 0

        A = sorted((f(q), qid) for qid, q in enumerate(queries))
        B = sorted(f(w) for w in words)

        ans = [-1] * len(queries)
        i = 0
        for x, qid in A:
            while i < len(B) and B[i] <= x:
                i += 1
            ans[qid] = len(B) - i
        return ans


Solution = Solution1
# Solution = Solution2
# @lc code=end
