def solve():
    s = input().strip()
    print("YES" if s.count('Y') <= 1 else "NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()