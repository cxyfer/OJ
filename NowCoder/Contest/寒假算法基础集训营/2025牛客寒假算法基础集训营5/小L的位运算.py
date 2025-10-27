"""
C - 小L的位运算
https://ac.nowcoder.com/acm/contest/95337/C

貪心

對於已經滿足條件的數位，不用花費任何代價。
對於不滿足條件的數位，可以分為以下四種情況：
1. (a, b, c) = (0, 0, 1)
2. (a, b, c) = (0, 1, 0)
3. (a, b, c) = (1, 0, 0)
4. (a, b, c) = (1, 1, 1)

對於每一種情況，可以反轉 a 或 b 來滿足一個數位的條件，代價為 x
然侯四種情況中可以兩兩交換 a 或 b 來滿足兩個數位的條件，代價為 y

這裡有一個常見的思路，如果所有情況中沒有任何一種超過一半，可以兩兩交換，
否則可以交換的次數就是去除最大數量的一種情況後，其餘情況的總和。
"""

def solve():
    n, x, y = map(int, input().split())
    a = list(map(int, input()))
    b = list(map(int, input()))
    c = list(map(int, input()))
    assert len(a) == len(b) == len(c) == n

    cnt = [0] * 4
    for ca, cb, cc in zip(a, b, c):
        if ca ^ cb != cc:
            cnt[ca << 1 | cb] += 1
    mx, s = max(cnt), sum(cnt)

    ans = s * x
    if mx > s // 2:
        ans = min(ans, (s - mx) * y + (s - (s - mx) * 2) * x)
    else:
        ans = min(ans, s // 2 * y + (s & 1) * x)
    print(ans)

if __name__ == "__main__":
    solve()