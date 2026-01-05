from bisect import bisect_left

def solve():
    n = int(input())
    P = [tuple(map(int, input().split())) for _ in range(n)]
    assert len(P) == n

    P.sort(key=lambda x: (x[0], -x[1]))
    f = []
    for _, b in P:
        idx = bisect_left(f, b)
        if idx == len(f):
            f.append(b)
        else:
            f[idx] = b
    print(len(f))

if __name__ == '__main__':
    solve()