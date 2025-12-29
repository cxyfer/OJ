def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n
    
    pre = 0
    suf = sum(A) - A[0]
    ans = -suf
    for i in range(1, n):
        suf -= A[i]
        ans = max(ans, A[0] + pre - suf)
        pre += abs(A[i])
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()