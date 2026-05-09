def solve():
    d, f = map(int, input().split())

    # while f <= d:
    #     f += 7
    # print(f - d)

    # print(7 - (d - f) % 7)

    ans = (f - d) % 7
    print(ans if ans else 7)


if __name__ == "__main__":
    solve()
