class BIT:  # PURQ, 1-based
    __slots__ = ["tree"]

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def add(self, k: int, x: int) -> None:  # 令 nums[k] += x
        while k < len(self.tree):
            self.tree[k] += x
            k += k & -k

    def preSum(self, k: int) -> int:  # 求 nums[:k+1] 之和
        res = 0
        while k > 0:
            res += self.tree[k]
            k -= k & -k
        return res


def main():
    n = int(input())
    A = [int(input()) for _ in range(n)]

    # 按照值由小到大排序，若值相同則依照原本位置排序
    # Python 的排序是穩定排序，若不是穩定排序，則使用雙關鍵字排序即可
    idxs = list(range(n))
    idxs.sort(key=lambda x: A[x])

    rank = [0] * n
    for i, idx in enumerate(idxs, start=1):
        rank[idx] = i

    bit = BIT(n)
    ans = 1
    for i, rk in enumerate(rank, start=1):
        bit.add(rk, 1)
        # 前 i 個位置中，有多少個元素最後應該去右邊
        ans = max(ans, i - bit.preSum(i))
    print(ans)


if __name__ == "__main__":
    main()
