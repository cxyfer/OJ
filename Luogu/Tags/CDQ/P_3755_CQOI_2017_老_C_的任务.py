"""
P3755 [CQOI2017] 老 C 的任务
https://www.luogu.com.cn/problem/P3755
二維數點問題

首先用二維前綴和的方式理解，令 f(i, j) 表示以 (i, j) 為右下角的矩形內的點的權重和，
則左上角為 (a, b)，右下角為 (c, d) 的矩形內的點的權重和為 f(c, d) - f(a - 1, d) - f(c, b - 1) + f(a - 1, b - 1)
自此可以把每條詢問拆解成四個問題。

而求 f(a, b)，相當於求 x[k] <= a, y[k] <= b 的點的個數，
將查詢的點視為虛擬點，那我們還需要確保所有實際點都先被處理過，但這可以透過對 (x, -v) 排序就能解決。
因此這是二維偏序問題，可以考慮 CDQ 分治來求解。

Similar problems:
- P2163 [SHOI2007] 园丁的烦恼
"""

# fmt: off
import sys
it = iter(sys.stdin.read().splitlines())
def input():
    return next(it)
def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)
# fmt: on


def solve():
    n, m = map(int, input().split())

    points = []
    for _ in range(n):
        x, y, v = map(int, input().split())
        points.append((x, y, 1, v))
    for qid in range(m):
        a, b, c, d = map(int, input().split())
        points.append((a - 1, b - 1, 2, qid, 1))
        points.append((a - 1, d, 2, qid, -1))
        points.append((c, b - 1, 2, qid, -1))
        points.append((c, d, 2, qid, 1))

    points.sort(key=lambda x: (x[0], x[2]))

    # ans[i] 表示第 i 個詢問的答案
    ans = [0] * m

    tmp = [None] * len(points)

    def cdq(left: int, right: int) -> None:
        if left == right:
            return
        mid = (left + right) // 2
        cdq(left, mid)
        cdq(mid + 1, right)

        i = left
        cnt = 0
        for j in range(mid + 1, right + 1):
            y, typ = points[j][1], points[j][2]
            while i <= mid and points[i][1] <= y:
                if points[i][2] == 1:
                    cnt += points[i][3]
                i += 1
            if typ == 2:
                qid = points[j][3]
                factor = points[j][4]
                ans[qid] += cnt * factor

        # 按照 y 排序
        # points[left : right + 1] = sorted(
        #     points[left : right + 1], key=lambda x: (x[1], -x[2])
        # )
        i, j, k = left, mid + 1, left
        while i <= mid and j <= right:
            if points[i][1] <= points[j][1]:
                tmp[k] = points[i]
                i += 1
            else:
                tmp[k] = points[j]
                j += 1
            k += 1
        while i <= mid:
            tmp[k] = points[i]
            i += 1
            k += 1
        while j <= right:
            tmp[k] = points[j]
            j += 1
            k += 1
        for i in range(left, right + 1):
            points[i] = tmp[i]

    cdq(0, len(points) - 1)

    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
