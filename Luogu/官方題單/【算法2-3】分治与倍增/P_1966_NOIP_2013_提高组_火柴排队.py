class BIT:
    __slots__ = ["tree"]

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, k: int, x: int) -> None:
        while k < len(self.tree):
            self.tree[k] += x
            k += k & -k

    def preSum(self, k: int) -> int:
        res = 0
        while k > 0:
            res += self.tree[k]
            k -= k & -k
        return res

    def query(self, l: int, r: int) -> int:
        if l > r:
            return 0
        return self.preSum(r) - self.preSum(l - 1)


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = int(1e8) - 3

    # 將 A 和 B 離散化，按照大小映射到 [1, n] 的整數
    mp1 = {x: i for i, x in enumerate(sorted(A), start=1)}
    mp2 = {x: i for i, x in enumerate(sorted(B), start=1)}
    A = [mp1[x] for x in A]
    B = [mp2[x] for x in B]

    # 把一個亂序的排列透過相鄰交換變成有序的操作次數，等同於求逆序對的數量
    # 把 A 再按照位置映射為 [1, n]，並做 B 做同樣的映射，則就等同於上述求逆序對的問題
    mp = {x: i for i, x in enumerate(A, start=1)}

    ans = 0
    bit = BIT(n)
    for x in B:
        ans = (ans + bit.query(mp[x] + 1, n)) % MOD
        bit.add(mp[x], 1)
    print(ans)


if __name__ == "__main__":
    solve()
