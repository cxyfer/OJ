from collections import defaultdict


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    def calc(st: int) -> int:
        res = 0
        left = st
        cnt = defaultdict(int)
        for i in range(st, n - 1, 2):
            x = A[i]
            if x != A[i + 1]:
                left = i + 2
                cnt.clear()
                continue
            while cnt[x] > 0:
                cnt[A[left]] -= 1
                left += 2
            cnt[x] += 1
            res = max(res, i + 2 - left)
        return res

    print(max(calc(0), calc(1)))


if __name__ == "__main__":
    solve()
