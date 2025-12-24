def solve():
    n = int(input())
    
    U = (1 << n) - 1
    ans = [U]
    for k in range(n - 1, -1, -1):
        ans.extend(range((1 << k) - 1, U, (1 << (k + 1))))
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()