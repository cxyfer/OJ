#
# @lc app=leetcode id=1717 lang=python3
# @lcpr version=30204
#
# [1717] Maximum Score From Removing Substrings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)
        if x < y: # 保證 x > y ，否則將 s 中的 a 和 b 互換，並交換 x 和 y 的值
            lst = list(s)
            for i, ch in enumerate(lst):
                if ch == 'a': lst[i] = 'b'
                elif ch == 'b': lst[i] = 'a'
            x, y = y, x
            s = ''.join(lst)
        ans = 0
        i = 0
        while (i < n): # 分組循環
            while i < n and s[i] != 'a' and s[i] != 'b': # 跳過非 a 和 b 的字元
                i += 1
            st1 = [] # 用來消除 "ab"
            while i < n and (s[i] == 'a' or s[i] == 'b'):
                if s[i] == 'a':
                    st1.append('a')
                else:
                    if st1 and st1[-1] == 'a':
                        ans += x
                        st1.pop()
                    else:
                        st1.append('b')
                i += 1 
            st2 = [] # 用來消除 "ba"
            while st1:
                if st1[-1] == 'a':
                    st2.append(st1.pop())
                else:
                    if st2 and st2[-1] == 'a':
                        ans += y
                        st1.pop()
                        st2.pop()
                    else: # 這裡可以提前 break
                        # break
                        st2.append(st1.pop())
        return ans
    
class Solution2:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        n = len(s)
        if x < y:
            lst = list(s)
            for i, ch in enumerate(lst):
                if ch == 'a': lst[i] = 'b'
                elif ch == 'b': lst[i] = 'a'
            x, y = y, x
            s = ''.join(lst)
        ans = 0
        i = 0
        while (i < n):
            while i < n and s[i] != 'a' and s[i] != 'b': # skip non a and b
                i += 1
            cnt_a = cnt_b = 0
            while i < n and (s[i] == 'a' or s[i] == 'b'):
                if s[i] == 'a':
                    cnt_a += 1
                else:
                    if cnt_a > 0:
                        ans += x
                        cnt_a -= 1
                    else:
                        cnt_b += 1
                i += 1
            ans += min(cnt_a, cnt_b) * y
        return ans
    
class Solution(Solution1):
# class Solution(Solution2):
    pass
# @lc code=end

#
# @lcpr case=start
# "cdbcbbaaabab"\n4\n5\n
# @lcpr case=end

# @lcpr case=start
# "aabbaaxybbaabb"\n5\n4\n
# @lcpr case=end

#

