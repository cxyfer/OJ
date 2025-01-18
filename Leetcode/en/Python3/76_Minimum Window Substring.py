# @algorithm @lc id=76 lang=python3 
# @title minimum-window-substring


from en.Python3.mod.preImport import *
from collections import Counter
# @test("ADOBECODEBANC","ABC")="BANC"
# @test("a","a")="a"
# @test("a","aa")=""
class Solution:
    """
        Sliding window, two pointers
        - Similar to 209. Minimum Size Subarray Sum
        - Similar to 904. Fruit Into Baskets
    """
    def minWindow(self, s: str, t: str) -> str:
        # return self.solve1(s, t)
        return self.solve2(s, t)
    """
        1. 比較簡潔的寫法，但判斷符合條件時，需要遍歷 t 中的所有字母
    """
    def solve1(self, s: str, t: str) -> str:
        ans = ""
        cnt = Counter() # 窗口中的字母以及其數量
        cnt_t = Counter(t) # 需要的字母以及其數量
        left = 0 # 左端點
        for right, ch in enumerate(s):
            cnt[ch] += 1 # 入窗口
            while (all(cnt[c] >= cnt_t[c] for c in cnt_t)): # 符合條件，開始縮小窗口
                if not ans or len(ans) > (right - left + 1): # 可以更新答案
                    ans = s[left:right+1]
                cnt[s[left]] -= 1 # 縮小窗口
                left += 1
        return ans
    """
        2. 用 need 來紀錄還需要的字母數量，這樣就不用每次都遍歷 t 中的所有字母
    """
    def solve2(self, s: str, t: str) -> str:
        ans = ""
        cnt_t = Counter(t) # 紀錄每個字母需要的數量
        need = len(t) # 還需要的字母總數量
        left = 0 # 左端點
        for right, ch in enumerate(s):
            if ch in cnt_t: # 入窗口時，只需要考慮 t 中的字母
                if cnt_t[ch] > 0: # 還需要這個字母
                    need -= 1
                cnt_t[ch] -= 1
            
            while (need == 0): # 符合條件，開始縮小窗口
                if not ans or len(ans) > (right - left + 1): # 更新答案
                    ans = s[left:right+1]
                if s[left] in cnt_t:
                    cnt_t[s[left]] += 1 
                    if cnt_t[s[left]] > 0: # 這個字母變成需要了
                        need += 1
                left += 1
        return ans