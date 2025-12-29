from itertools import accumulate

def solve():
    n = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(n)]
    assert len(intervals) == n
    
    cnt = [0] * (2 * n + 1)
    for l, r in intervals:
        cnt[l] += (l == r)
    s = list(accumulate(cnt, func=lambda x, y: x + (y == 0)))

    ans = []
    for l, r in intervals:
        if l == r:
            ans.append('1' if cnt[l] == 1 else '0')
        else:
            ans.append('1' if s[r] - s[l - 1] > 0 else '0')
    print(*ans, sep='')

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()