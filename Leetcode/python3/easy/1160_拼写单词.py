#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#
from preImport import *
# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        ans = 0
        for word in words:
            cnt_w = Counter(word)
            if all(cnt_w[ch] <= cnt[ch] for ch in cnt_w):
                ans += len(word)
        return ans
# @lc code=end

