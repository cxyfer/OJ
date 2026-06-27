from atcoder.fenwicktree import FenwickTree


def solve():
    n, q = map(int, input().split())
    H = list(map(int, input().split()))

    queries = []
    for qid in range(q):
        l, r = map(lambda x: int(x) - 1, input().split())
        queries.append((l, r, qid))
    queries.sort()

    # P[i] 表示 H[i] 左側第一個 > H[i] 的位置，若不存在則為 -1
    P = [-1] * n
    st = []
    for i in range(n):
        while st and H[st[-1]] <= H[i]:
            st.pop()
        if st:
            P[i] = st[-1]
        st.append(i)

    points = [(p, idx) for idx, p in enumerate(P)]
    points.sort()

    bit = FenwickTree(n)
    ans = [0] * q

    j = 0
    for l, r, qid in queries:
        while j < n and points[j][0] < l:
            _, idx = points[j]
            bit.add(idx, 1)
            j += 1
        ans[qid] = bit.sum(l, r + 1)

    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()