#
# @lc app=leetcode id=2901 lang=python3
#
# [2901] Longest Unequal Adjacent Groups Subsequence II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        mp = defaultdict(list)
        for w, g in zip(words, groups):
            mp[len(w)].append((w, g))

        ans = []
        for _, v in mp.items():
            m = len(v)
            f = [1] * m
            pre = [-1] * m
            mx_idx = 0
            for j in range(1, m):
                for k in range(j):
                    if sum(x != y for x, y in zip(v[k][0], v[j][0])) == 1 \
                        and v[k][1] != v[j][1]:
                        if f[j] < f[k] + 1:
                            f[j] = f[k] + 1
                            pre[j] = k
                if f[j] > f[mx_idx]:
                    mx_idx = j
            if f[mx_idx] > len(ans):
                ans.clear()
                while mx_idx != -1:
                    ans.append(v[mx_idx][0])
                    mx_idx = pre[mx_idx]
                ans.reverse()
        return ans
# @lc code=end

