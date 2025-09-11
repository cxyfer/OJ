def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    mp = [[] for _ in range(2)]
    for x in A:
        mp[x & 1].append(x)
    ans = []
    for xs in mp:
        xs.sort()
        ans.extend(xs)
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()