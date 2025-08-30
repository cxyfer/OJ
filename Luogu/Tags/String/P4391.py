"""
P4391 [BalticOI 2009] Radio Transmission 无线传输
https://www.luogu.com.cn/problem/P4391
String Hashing / KMP

所求為 n - 最長匹配真前後綴的長度
cab|cab|cab|ca.|..
...|cab|cab|cab|ca
"""
from random import randint

n = int(input())
s = input()

class HashString:
    # 初始化 HashString ，預計算所有冪次和前綴雜湊
    def __init__(self, s: str, MOD: int = 1070777777, BASE: int = randint(int(1e8), int(1e9))):
        self.MOD = MOD
        self.BASE = BASE
        self.n = len(s)
        self.P = [1] + [0] * self.n  # P[i] = BASE^i % MOD
        self.H = [0] * (self.n + 1)  # H[i] = hash(s[:i])

        for i, b in enumerate(s):
            # 預計算所有冪次
            self.P[i + 1] = self.P[i] * self.BASE % self.MOD
            # 預計算所有前綴雜湊
            self.H[i + 1] = (self.H[i] * self.BASE + ord(b)) % self.MOD

    # 計算子字串 s[l..r] 的雜湊值 (0-indexed)
    def query(self, l: int, r: int) -> int:
        return (self.H[r + 1] - self.H[l] * self.P[r - l + 1]) % self.MOD

def solve1():
    hs = HashString(s)
    for ln in range(n - 1, 0, -1):
        if hs.query(0, ln - 1) == hs.query(n - ln, n - 1):
            print(n - ln)
            return
    print(n)

def solve2():
    pi = [0] * n
    ln = 0
    for i in range(1, n):
        while ln and s[i] != s[ln]:
            ln = pi[ln - 1]
        if s[i] == s[ln]:
            ln += 1
        pi[i] = ln

    print(n - pi[n - 1])

solve1()
# solve2()