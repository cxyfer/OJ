def solve():
    X, C = map(int, input().split())
    # 1000Y * (1 + 0.001 * C) <= X
    # Y * (1000 + C) <= X
    print((X // (1000 + C)) * 1000)

if __name__ == "__main__":
    solve()