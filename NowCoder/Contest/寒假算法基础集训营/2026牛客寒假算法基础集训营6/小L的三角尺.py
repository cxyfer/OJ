"""
A. 小L的三角尺
https://ac.nowcoder.com/acm/contest/120566/A

注意到操作次數最多只有 1e6，因此可以對每個物品維護操作一次後對答案的貢獻，用 Min Heap 維護即可。
有點卡常，賽時迅速改用 C++ 是對的，不然大概又要紅溫了。
"""
import sys
import math
from heapq import heappush, heappop

it = iter(sys.stdin.read().splitlines())
def input():
    return next(it)
def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)

def solve():
    n, w = map(int, input().split())
    X, Y = [], []  # 分開保存以取得一點常數優化
    for _ in range(n):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    ans = 0.0
    hp = []
    for i, (x, y) in enumerate(zip(X, Y)):
        ans += math.hypot(x, y)
        if y > 0:
            v = math.hypot(x, y) - math.hypot(x, y - 1)
            heappush(hp, (-v, i))

    while hp and w > 0:
        v, i = heappop(hp)
        v = -v
        ans -= v
        Y[i] -= 1
        if Y[i] > 0:
            v = math.hypot(X[i], Y[i]) - math.hypot(X[i], Y[i] - 1)
            heappush(hp, (-v, i))
        w -= 1
    print(f"{ans:.10f}")

if __name__ == "__main__":
    solve()