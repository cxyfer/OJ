from random import randint

U = (1 << 64) - 1


def solve():
    n, m = map(int, input().split())

    W = [randint(1, U) for _ in range(n)]  # 節點隨機權重
    tgt = sum(W)  # 目標雜湊值

    base = [0] * n  # base[v]: 初始入邊權重和
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        base[v] += W[u]
    curr = base[:]  # curr[v]: 當前入邊權重和

    h = sum(curr)  # 全域雜湊值

    q = int(input())
    ans = []
    for _ in range(q):
        op, *args = map(int, input().split())
        if op == 1:  # 移除 (u, v) 邊
            u, v = map(lambda x: x - 1, args)
            h -= curr[v]
            curr[v] -= W[u]
            h += curr[v]
        elif op == 2:  # 移除 v 的全部入邊
            v = args[0] - 1
            h -= curr[v]
            curr[v] = 0
        elif op == 3:  # 恢復 (u, v) 邊
            u, v = map(lambda x: x - 1, args)
            h -= curr[v]
            curr[v] += W[u]
            h += curr[v]
        else:  # 恢復 v 的全部入邊
            v = args[0] - 1
            h -= curr[v]
            curr[v] = base[v]
            h += curr[v]
        ans.append("YES" if h == tgt else "NO")
    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
