#
# @lc app=leetcode.cn id=2506 lang=python3
# @lcpr version=30204
#
# [2506] 统计相似字符串对的数目
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for word in words:
            s = 0
            for ch in word:
                i = ord(ch) - ord("a")
                s |= (1 << i)
            ans += cnt[s]
            cnt[s] += 1
        return ans
# @lc code=end

sol = Solution()
print(sol.similarPairs(["aba","aabb","abcd","bac","aabc"]))  # 2
print(sol.similarPairs(["aabb","ab","ba"]))  # 3
print(sol.similarPairs(["nba","cba","dba"]))  # 0

#
# @lcpr case=start
# ["aba","aabb","abcd","bac","aabc"]\n
# @lcpr case=end

# @lcpr case=start
# ["aabb","ab","ba"]\n
# @lcpr case=end

# @lcpr case=start
# ["nba","cba","dba"]\n
# @lcpr case=end

#

