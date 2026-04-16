def solve():
    W, B = map(int, input().split())
    # n * B > 1000W
    print(1000 * W // B + 1)


if __name__ == "__main__":
    solve()
