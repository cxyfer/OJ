"""
P1102 A-B 数对
https://www.luogu.com.cn/problem/P1102
枚舉右維護左
A − B = C => A = B + C / B = A - C
枚舉 B 計算 B + C 的數量；枚舉 A 計算 A - C 的數量
"""


def solve():
    N, C = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == N

    ans = 0
    cnt = dict()  # 本題用 defaultdict 會 MLE
    for x in A:
        ans += cnt.get(x - C, 0)  # 作為 B，滿足條件的 A 數量
        ans += cnt.get(x + C, 0)  # 作為 A，滿足條件的 B 數量
        cnt[x] = cnt.get(x, 0) + 1
    print(ans)


if __name__ == "__main__":
    solve()
