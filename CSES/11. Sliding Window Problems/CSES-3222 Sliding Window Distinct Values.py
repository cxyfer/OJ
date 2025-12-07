from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    ans = []
    cnt = defaultdict(int)
    for r, x in enumerate(A):
        cnt[x] += 1
        if r >= k - 1:
            ans.append(len(cnt))
            y = A[r - k + 1]
            cnt[y] -= 1
            if cnt[y] == 0:
                del cnt[y]
    print(*ans)

if __name__ == "__main__":
    solve()