from bisect import bisect_left


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    pos = [[] for _ in range(21)]
    for i, x in enumerate(A):
        pos[x].append(i)

    f = [n] * (1 << 20)
    f[0] = -1
    U = (1 << 20) - 1

    ans = 0
    for s1 in range(1 << 20):
        if f[s1] == n:
            continue
        ans = max(ans, s1.bit_count())
        s2 = U ^ s1
        while s2:
            lb = s2 & -s2
            v = lb.bit_length()
            idx = bisect_left(pos[v], f[s1]) + 1
            if idx < len(pos[v]):
                f[s1 | lb] = min(f[s1 | lb], pos[v][idx])
            s2 ^= lb
    print(ans << 1)


if __name__ == "__main__":
    solve()
