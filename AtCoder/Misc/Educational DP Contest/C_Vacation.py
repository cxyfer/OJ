def solve():
    N = int(input())
    days = [tuple(map(int, input().split())) for _ in range(N)]

    f0 = f1 = f2 = 0
    for a, b, c in days:
        f0, f1, f2 = max(f1, f2) + a, max(f0, f2) + b, max(f0, f1) + c
    print(max(f0, f1, f2))

if __name__ == "__main__":
    solve()