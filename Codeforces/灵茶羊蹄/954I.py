MOD = 1070777777
BASE = 233

class HashString:
    def __init__(self, s: str, mp: list[int]):
        self.n = len(s)
        self.P = [1] + [0] * self.n  # P[i] = BASE^i % MOD
        self.H = [0] * (self.n + 1)  # H[i] = hash(s[:i])

        for i, b in enumerate(s):
            # 預計算所有冪次
            self.P[i + 1] = self.P[i] * BASE % MOD
            # 預計算所有前綴雜湊
            self.H[i + 1] = (self.H[i] * BASE + mp[ord(b) - ord('a')] + 1) % MOD

    # 計算子字串 s[l:r+1] 的雜湊值 (0-indexed)，計算方法類似前綴和
    def query(self, l: int, r: int) -> int:
        return (self.H[r + 1] - self.H[l] * self.P[r - l + 1]) % MOD

s = input()
t = input()
n, m = len(s), len(t)

mp = list(range(6))  # 每個字母的所屬的集合中，最小的元素編號，初始化為自己
rt = []  # 已經分配的集合中，其最小的元素編號
ans = [float('inf')] * (n - m + 1)
def dfs(i):
    if i == 6:
        hs1 = HashString(s, mp)
        hs2 = HashString(t, mp)
        for j in range(n - m + 1):
            if hs1.query(j, j + m - 1) == hs2.query(0, m - 1):
                ans[j] = min(ans[j], 6 - len(rt))
    else:
        # 自己一組
        rt.append(i)
        dfs(i + 1)
        rt.pop()

        # 與其他組合
        for x in rt:
            mp[i] = x
            dfs(i + 1)
            mp[i] = i
dfs(0)
print(*ans)