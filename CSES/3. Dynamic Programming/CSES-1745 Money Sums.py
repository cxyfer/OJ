"""
CSES-1745 Money Sums
https://cses.fi/problemset/task/1745

solve2 因為 CSES 使用的 PyPy3 版本不支援 bit_count 和 bit_length，需要使用 CPython 3 提交。
"""
def solve1():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    f = set()
    for x in A:
        nf = f.copy()
        for y in f:
            nf.add(y + x)
        nf.add(x)
        f = nf
    print(len(f))
    print(*sorted(f))

def solve2():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    f = 1  # f >> i == 1 表示可以湊出 i 元
    for x in A:
        f |= (f << x)
    f >>= 1  # 移除初始值 0

    print(f.bit_count())
    ans = []
    while f:
        lb = f & -f
        ans.append(lb.bit_length())
        f ^= lb
    print(*ans)

if __name__ == "__main__":
    # solve1()
    solve2()