"""
pi[i] 表示 t[0..i] 的最長匹配真前後綴(border)長度

Problem:
- 28. Find the Index of the First Occurrence in a String
"""

class Solution:
    def strStr(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        pi = [0] * m
        ln = 0
        for i in range(1, m):
            while ln and t[i] != t[ln]:
                ln = pi[ln - 1]
            if t[i] == t[ln]:
                ln += 1
            pi[i] = ln
        ln = 0
        for i in range(n):
            while ln and s[i] != t[ln]:
                ln = pi[ln - 1]
            if s[i] == t[ln]:
                ln += 1
            if ln == m:
                return i - m + 1
        return -1