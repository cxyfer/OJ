from itertools import pairwise


def solve():
    n = int(input())
    s = input()
    assert len(s) == n

    ans = 1
    for a, b in pairwise(s.split("/")):
        i = len(a) - 1
        j = 0
        while i >= 0 and j < len(b) and a[i] == "1" and b[j] == "2":
            i -= 1
            j += 1
        ans = max(ans, 1 + (j << 1))
    print(ans)


if __name__ == "__main__":
    solve()
