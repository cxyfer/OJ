from random import randint

MOD = 1070777777
BASE = randint(233, 2333)
class HashString:
    # 初始化 HashString ，預計算所有冪次和前綴雜湊
    def __init__(self, s: str):
        self.n = len(s)
        self.P = [1] + [0] * self.n  # P[i] = BASE^i % MOD
        self.H = [0] * (self.n + 1)  # H[i] = hash(s[:i])

        for i, b in enumerate(s):
            # 預計算所有冪次
            self.P[i + 1] = self.P[i] * BASE % MOD
            # 預計算所有前綴雜湊
            self.H[i + 1] = (self.H[i] * BASE + ord(b)) % MOD

    # 計算子字串 s[l..r] 的雜湊值 (0-indexed)，計算方法類似前綴和
    def query(self, l: int, r: int) -> int:
        return (self.H[r + 1] - self.H[l] * self.P[r - l + 1]) % MOD

s1 = input()
s2 = input()
n, m = len(s1), len(s2)

hs1 = HashString(s1)
hs2 = HashString(s2)
ans = 0
for i in range(min(n, m)):
    if hs1.query(0, i) == hs2.query(m - i - 1, m - 1) or hs1.query(n - i - 1, n - 1) == hs2.query(0, i):
        ans = i + 1
print(ans)