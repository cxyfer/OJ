def solve():
    s = input()
    n = len(s)

    if n & 1:
        print("No")
        return

    vis = set()
    for i in range(0, n, 2):
        if s[i] != s[i + 1] or s[i] in vis:
            print("No")
            return
        vis.add(s[i])
    print("Yes")


if __name__ == "__main__":
    solve()
