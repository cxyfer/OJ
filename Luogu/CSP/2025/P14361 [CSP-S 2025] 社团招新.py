"""
P14361 [CSP-S 2025] 社团招新 / club
https://www.luogu.com.cn/problem/P14361

反悔貪心

若不考慮人數限制，則將所有人分配到滿意度最高的社團即可。
但若有社團人數超過 n // 2，則此時需要反悔，把部分人移動到其他社團。

考慮要移動哪些人可以使減少的滿意度最少。
顯然若移動則一定是移動到滿意度第二高的社團更優，此時減少的滿意度為兩者的差值。
因此若需反悔，則應該移動最大滿意度與次大滿意度差值最小的人。
"""
def solve():
    n = int(input())
    A = [tuple(map(int, input().split())) for _ in range(n)]

    ans = 0
    # 不先考慮人數限制，將所有人分配到滿意度最高的社團
    groups = [[] for _ in range(3)]
    for p in A:
        v = sorted(enumerate(p), key=lambda x: x[1], reverse=True)
        ans += v[0][1]
        groups[v[0][0]].append(v[0][1] - v[1][1])  # 最大滿意度與次大滿意度差值

    for g in groups:
        if len(g) > n // 2:
            g.sort()
            ans -= sum(g[:len(g) - n // 2])  # 反悔
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()