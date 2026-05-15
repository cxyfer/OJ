from bisect import bisect_right


def solve():
    n, k = map(int, input().split())
    movies = [tuple(map(int, input().split())) for _ in range(n)]
    movies.sort(key=lambda x: x[1])

    ans = 0
    # sl = SortedList([0] * k)
    ends = [0] * k
    fa = list(range(n + k + 1))  # 1-indexed DSU

    def find(x: int) -> int:
        while fa[x] != x:
            fa[x] = fa[fa[x]]
            x = fa[x]
        return x

    for l, r in movies:
        # idx = sl.bisect_right(l)
        # if idx > 0:
        #     sl.pop(idx - 1)
        #     sl.add(r)
        #     ans += 1
        idx = bisect_right(ends, l)
        idx = find(idx)
        if idx > 0:
            fa[idx] = find(idx - 1)
            ends.append(r)
            ans += 1

    print(ans)


if __name__ == "__main__":
    solve()
