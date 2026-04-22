"""
P2671 [NOIP 2015 普及组] 求和
https://www.luogu.com.cn/problem/P2671
貢獻法

只有相同顏色的兩兩配對才會有貢獻，接著可以注意到 y 對答案沒有貢獻，只限定了 x 和 z 的關係，
從編號關係 y - x = z - y 可以獲得 2 * y = x + z，即 x 和 z 的奇偶性相同。
因此可以按照「相同顏色」且「編號奇偶性相同」分組，每組中的元素可以任意配對，計每組組內元素數量為 m。

將貢獻公式展開：
(x + z) * (number_x + number_z)
= x * number_x + z * number_z + x * number_z + number_x * z

其中 x * number_x 和 z * number_z 是每個元素本身的貢獻，這種貢獻會發生在與同組其他元素配對時，共 m - 1 次。
對於剩餘兩項可以用「枚舉右維護左」處理，維護 x 和 number_x 的前綴和即可。
"""

from collections import defaultdict

MOD = 10007


def solve():
    n, m = map(int, input().split())

    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    assert len(A) == len(C) == n

    groups = defaultdict(list)
    for i, (x, c) in enumerate(zip(A, C)):
        groups[(c, i & 1)].append((i + 1, x))

    ans = 0
    for g in groups.values():
        m = len(g)
        s1 = s2 = 0
        for a, b in g:
            ans += a * b * (m - 1)  # 每個元素本身的貢獻
            ans += a * s2 + b * s1  # 枚舉右維護左
            ans %= MOD
            s1 += a
            s2 += b
    print(ans)


if __name__ == "__main__":
    solve()
