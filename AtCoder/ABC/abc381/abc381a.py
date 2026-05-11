def solve():
    n = int(input())
    s = input()
    assert len(s) == n

    if s.count("/") != 1:
        print("No")
        return

    a, b = s.split("/")
    if not all(ch == "1" for ch in a) or not all(ch == "2" for ch in b):
        print("No")
        return

    print("Yes" if len(a) == len(b) else "No")


if __name__ == "__main__":
    solve()
