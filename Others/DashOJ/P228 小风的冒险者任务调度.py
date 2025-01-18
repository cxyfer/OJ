class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, k: int, v: int) -> None:
        while k <= self.size:
            self.tree[k] += v
            k += (k & -k)

    def query(self, k: int) -> int:
        res = 0
        while k > 0:
            res += self.tree[k]
            k -= (k & -k)
        return res

n, m = map(int, input().split())
A = list(map(int, input().split()))

bit = FenwickTree(m + n + 1)

pos = [0] * (n + 1)
for x in range(1, n + 1):
    pos[x] = m + x
    bit.update(pos[x], 1)

ans1 = [0] * (n + 1)  # 最小位置
ans2 = [0] * (n + 1)  # 最大位置
for x in range(1, n + 1):
    ans1[x] = ans2[x] = x

top = m
for idx, x in enumerate(A):
    rank = bit.query(pos[x])
    ans1[x], ans2[x] = 1, max(ans2[x], rank)
    bit.update(pos[x], -1)
    pos[x] = top
    bit.update(pos[x], 1)
    top -= 1

for x in range(1, n + 1):
    rank = bit.query(pos[x])
    ans1[x] = min(ans1[x], rank)
    ans2[x] = max(ans2[x], rank)

for x in range(1, n + 1):
    print(ans1[x], ans2[x])