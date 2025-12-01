def solve():
    n = int(input())
    y, r = map(int, input().split())
    print(min(n, y // 2 + r))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()