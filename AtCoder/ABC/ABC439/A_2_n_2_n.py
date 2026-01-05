def solve():
    N = int(input())
    print((1 << N) - (N << 1))

if __name__ == "__main__":
    solve()