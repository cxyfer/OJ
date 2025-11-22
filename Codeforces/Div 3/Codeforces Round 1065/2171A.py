def solve():
    n = int(input())

    if n & 1:
        print(0)
    else:
        print(n // 4 + 1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()