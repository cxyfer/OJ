"""
2136D - For the Champion
https://codeforces.com/contest/2136/problem/D
構造

首先把 d = min{|X - xi| + |Y - yi|} 中兩個絕對值消掉。
當 X >= xi 時，|X - xi| = X - xi，故可以把 X 操作到一定 >= xi 的位置 (X + V)，Y 同理。
此時可以得到 d1 = min{X + Y + 2V - xi - yi}，發生在 xi + yi 最大的點，
移項可以得到 X + Y = d - 2V + xi + yi。

接著移動到 (X + V, Y - V)，
此時可以得到 d2 = min{X + Y - 2V - xi + yi}，發生在 xi - yi 最大的點，
移項可以得到 X - Y = d2 - 2V + xi - yi。

有了 X + Y 和 X - Y 後，解聯立便可以得到 X 和 Y。
"""

K = int(1e9)

def query(s, k):
    print(f"? {s} {k}", flush=True)
    return int(input())

def answer(x, y):
    print(f"! {x} {y}", flush=True)

def move(s, k):
    while k > K:
        query(s, K)
        k -= K
    return query(s, k)

def solve():
    n = int(input())
    anchors = [list(map(int, input().split())) for _ in range(n)]

    move("R", 2 * K)  # (X + 2K, Y)
    d1 = move("U", 2 * K)  # (X + 2K, Y + 2K)
    d2 = move("D", 4 * K)  # (X + 2K, Y - 2K)

    # d1 = min{(X + 2K - xi) + (Y + 2K - yi)}
    # 發生在 xi + yi 最大的點
    # X + Y = d1 - 4K + xi + yi
    s = d1 - 4 * K + max(xi + yi for xi, yi in anchors) 
    # d2 = min{(X + 2K - xi) + (yi - (Y - 2K))}
    # 發生在 xi - yi 最大的點
    # X - Y = d2 - 4K + xi - yi
    d = d2 - 4 * K + max(xi - yi for xi, yi in anchors)

    X, Y = (s + d) // 2, (s - d) // 2
    answer(X, Y)
    return

t = int(input())
for _ in range(t):
    solve()