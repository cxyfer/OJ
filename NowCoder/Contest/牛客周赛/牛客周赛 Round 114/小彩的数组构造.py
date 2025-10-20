"""
E-小彩的数组构造
https://ac.nowcoder.com/acm/contest/119273/E

構造
由於所有整數都是 1 的倍數，因此總共洽有 a 個長度為 3 的子陣列，答案長度為 n + 2。
這 a 個子陣列可分為以下四種情況：
1. 為 2 的倍數且為 3 的倍數 (即為 6 的倍數)，令其數量為 d
2. 為 2 的倍數但不為 3 的倍數，其數量為 b - d
3. 為 3 的倍數但不為 2 的倍數，其數量為 c - d
4. 既不為 2 的倍數也不為 3 的倍數，其數量為 a - (b - d) - (c - d) - d = a - b - c + d
其中 d 的取值範圍為 [max(0, b + c - a), min(b, c)]

為使 4. 的數量最多，取 d 為最大值 min(b, c)
接著根據當前構造出的最後兩項，分情況討論構造答案。
"""
def solve():
    a, b, c = map(int, input().split())
    n = a + 2
    d = min(b, c)
    b -= d
    c -= d
    if b + c + d > a:
        print(-1)
        return
    ans = []

    # 1. 為 6 的倍數
    ans.extend([6] * (d + 2))  

    # 2. 為 2 的倍數但不為 3 的倍數
    ans.extend([2, 6] * (b // 2) + [2] * (b & 1))

    # 3. 為 3 的倍數但不為 2 的倍數
    if b & 1:  # 此時最後兩項為 6, 2
        ans.extend([1, 6, 2] * (c // 3))
        ans.extend([1, 6, 2][:c % 3])
    elif b > 0:  # 此時最後兩項為 2, 6
        ans.extend([1, 2, 6] * (c // 3))
        ans.extend([1, 2, 6][:c % 3])
    else:  # b == 0 的情況，此時最後兩項為 6, 6
        ans.extend([3, 6, 6] * (c // 3))
        ans.extend([3, 6, 6][:c % 3])

    # 4. 既不為 2 的倍數也不為 3 的倍數
    for _ in range(a - b - c - d):
        s = (ans[-1] + ans[-2]) % 6
        ans.append(7 - s)

    print(n)
    print(*ans)

if __name__ == "__main__":
    solve()
