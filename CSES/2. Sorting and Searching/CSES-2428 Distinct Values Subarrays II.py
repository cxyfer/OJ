from collections import defaultdict


def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    ans = left = 0
    cnt = defaultdict(int)
    for right, x in enumerate(A):
        cnt[x] += 1
        while len(cnt) > k:
            y = A[left]
            cnt[y] -= 1
            if cnt[y] == 0:
                del cnt[y]
            left += 1
        ans += right - left + 1
    print(ans)


if __name__ == "__main__":
    solve()
