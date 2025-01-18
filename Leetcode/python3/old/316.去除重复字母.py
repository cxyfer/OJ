#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
from mod.preImport import *
from collections import Counter
# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 反悔貪心 ?
        cnt = Counter(s)
        ans = []
        selected = set()
        for ch in s:
            if ch not in selected: # 這個字母還沒被選過
                # 這個字母比前面的字母小，且前面的字母還有剩餘，就把前面的字母刪掉(反悔)
                while ans and ans[-1] > ch and cnt[ans[-1]] > 0:
                    selected.remove(ans.pop())
                ans.append(ch) # 把這個字母加入答案
                selected.add(ch) # 把這個字母標記成已選字母
            cnt[ch] -= 1
        return ''.join(ans)
# @lc code=end

