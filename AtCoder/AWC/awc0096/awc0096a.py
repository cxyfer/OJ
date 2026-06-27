def solve():
    n = int(input())
    data = [map(int, input().split()) for _ in range(n)]

    ans = 0
    for a, b in data:
        ans = max(ans, a) + b
    print(ans)

if __name__ == "__main__":
    solve()