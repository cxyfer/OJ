"""
I. 智乃挖坑
https://ac.nowcoder.com/acm/contest/120565/I

二分 + 二階差分

若使用前 k 次操作可以挖面地面，則使用前 k + 1 次操作也可以挖面地面，
因此具有單調性，可以二分搜尋。

每一次操作等同於在區間上加上兩個等差數列，可以用差分來維護。
對於 [l, r] 區間加上一個首項為 a 、公差為 d 、末項為 t = a + d * (r - l) 的等差數列
等同於在一階差分上做以下操作：
- diff1[l] += a
- diff1[l+1...r] += d
- diff1[r+1] -= t

注意到出現了在 diff1 的 [l+1...r] 的區間加 d 的操作，因此可以再維護差分上的差分(二階差分)。
- diff2[l + 1] += d
- diff2[r + 1] -= d

可以維護上述兩個差分來得到最終的數列，但實際上可以僅維護二階差分，因為一階差分可以透過二階差分還原，故等同於在二階差分上做以下操作：
- diff2[l] += a
- diff2[l + 1] += d - a
- diff2[r + 1] += -t - d
- diff2[r + 2] += t
"""
def solve():
    n, m, h = map(int, input().split())
    ops = [tuple(map(int, input().split())) for _ in range(m)]

    def check(k):
        diff2 = [0] * (n + 3)  # 二階差分

        # 在 [l, r] 區間加上一個首項為 a 、公差為 d 的等差數列
        def update(l, r, a, d):
            if l > r:
                return
            t = a + d * (r - l)  # 末項
            diff2[l] += a
            diff2[l + 1] += d - a
            diff2[r + 1] += -t - d
            diff2[r + 2] += t

        for i in range(k):
            p, f = ops[i]
            
            l, r = max(1, p - f + 1), p
            update(l, r, (f - p) + l, 1)
            l, r = p + 1, min(n, p + f - 1)
            update(l, r, (f + p) - l, -1)

        s = s1 = 0
        for d2 in diff2:
            s1 += d2
            s += s1
            if s > h:
                return True
        return False

    left, right = 1, m
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1

    if left <= m:
        print("Yes")
        print(left)
    else:
        print("No")

if __name__ == "__main__":
    solve()