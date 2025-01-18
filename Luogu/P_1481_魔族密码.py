def solve1():
    from collections import defaultdict

    n = int(input())
    words = [input().strip() for _ in range(n)]

    class TrieNode:
        def __init__(self):
            self.child = defaultdict(TrieNode)
            self.max_len = 0

    root = TrieNode()
    ans = 0
    for word in words:
        node = root
        mx = 0
        for ch in word:
            c = ord(ch) - ord('a')
            node = node.child[c]
            mx = max(mx, node.max_len)
        node.max_len = mx + 1
        ans = max(ans, node.max_len)

    print(ans)

def solve2():
    from collections import defaultdict
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

    n = int(input())
    words = [input().strip() for _ in range(n)]

    f = defaultdict(int)
    for s in words:
        hs = HashString(s)
        x = hs.query(0, len(s) - 1)
        f[x] = 1
        for i in range(len(s) - 1):
            f[x] = max(f[x], f[hs.query(0, i)] + 1)

    print(max(f.values()))

# solve1()
solve2()