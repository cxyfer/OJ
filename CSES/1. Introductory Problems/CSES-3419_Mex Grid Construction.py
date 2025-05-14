def solve1():
    n = int(input())
    ans = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            vis = set()
            for k in range(c):
                vis.add(ans[r][k])
            for k in range(r):
                vis.add(ans[k][c])
            mex = 0
            while mex in vis:
                mex += 1
            ans[r][c] = mex
    for row in ans:
        print(*row)

"""
2. Sprague-Grundy 定理
題意即為求 sg(r, c) = mex(sg(r', c) ∪ sg(r, c'))
"""
def solve2():
    n = int(input())
    ans = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            ans[r][c] = r ^c
    for row in ans:
        print(*row)

if __name__ == "__main__":
    # solve1()
    solve2()