from itertools import groupby

def solve():
    n = int(input())
    s = input()
    assert len(s) == n

    arr = [len(list(lst)) for c, lst in groupby(s) if c == "."]
    if any(ln >= 3 for ln in arr):
        print(2)
    else:
        print(sum(arr))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()