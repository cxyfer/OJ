"""
P14575 坤班
https://www.luogu.com.cn/problem/P14575

二分答案
當班級數量越少時，顯然越容易滿足條件，故滿足單調性，可以二分答案。
注意到當一個願意當班主任的老師不當班主任時，可以多教一個班級。
因此可以先假設所有願意當班主任的老師都「當」班主任，然後檢查是否需要反悔這個決定。
對於一個給定的答案 ans，可以在 O(n) 時間內檢查是否滿足條件。
時間複雜度為 O(nlogn)，空間複雜度為 O(n)。
"""
def solve():
    n, m = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(n)]

    k = sum(c for _, _, c in A)  # 願意當班主任的老師總人數
    cnt1 = [0] * m  # 教第 i 門課且願意當班主任的老師人數
    cnt2 = [0] * m  # 在所有願意當班主任的老師都當班主任時，每門課能夠教授的班級數量
    for a, b, c in A:
        cnt1[a - 1] += c
        cnt2[a - 1] += b - c

    def check(mid):
        cnt = k
        for x, y in zip(cnt1, cnt2):
            if x + y < mid:
                return False
            cnt -= max(0, mid - y)
            if cnt < mid:
                return False
        return True

    left, right = 0, k
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    print(right)

if __name__ == "__main__":
    solve()