from math import inf


def solve1():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    if m > 0:
        B = list(map(int, input().split()))
    else:
        B = []
    assert len(A) == n and len(B) == m

    A.sort()
    B.sort()
    B.append(inf)

    i = j = 0
    groups = []
    while i < n:
        group = []
        while B[j] < A[i]:
            j += 1
        while i < n and A[i] < B[j]:
            group.append(A[i])
            i += 1
        groups.append(group)

    if len(groups) > 1:
        print(-1)
    else:
        g = groups[0]
        k = len(g)
        mid = g[k // 2]
        ans = sum(abs(x - mid) for x in g)
        print(ans)


def solve2():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    if m > 0:
        B = list(map(int, input().split()))
    else:
        B = []
    assert len(A) == n and len(B) == m

    A.sort()

    for b in B:
        if A[0] <= b <= A[-1]:
            print(-1)
            return

    mid = A[n // 2]
    ans = sum(abs(x - mid) for x in A)
    print(ans)


if __name__ == "__main__":
    # solve1()
    solve2()
