def solve():
    n, l, r = map(int, input().split())
    
    s = list(range(n + 1))
    s[r] = s[l - 1]
    ans = [s[i + 1] ^ s[i] for i in range(n)]
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()