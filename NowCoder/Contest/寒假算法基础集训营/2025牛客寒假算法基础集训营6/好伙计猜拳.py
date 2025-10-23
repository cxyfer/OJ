"""
B - 好伙计猜拳
https://ac.nowcoder.com/acm/contest/95338/B

DP
類似 LIS 問題，但是多了是否交換的狀態
"""
def solve():
    n, c1, c2 = map(int, input().split())
    A = [tuple(map(int, input().split())) for _ in range(n)]
    assert len(A) == n

    # f[i][swapped] 表示以 A[i] 為最後一個元素，且最後一個元素是否被交換過，使得 A[0..i] 成為好陣列的最小代價
    f = [[float('inf')] * 2 for _ in range(n)]
    for i in range(n):
        for k1 in range(2):
            f[i][k1] = i * c1
            a1, b1 = A[i] if not k1 else (A[i][1], A[i][0])
            for j in range(i):
                for k2 in range(2):
                    a2, b2 = A[j] if not k2 else (A[j][1], A[j][0])
                    if a2 <= a1 and b2 <= b1:
                        f[i][k1] = min(f[i][k1], f[j][k2] + c1 * (i - j - 1))
            f[i][k1] += (c2 if k1 else 0)

    ans = float('inf')
    # 枚舉最後一個元素，後面的元素需要被刪除
    for i in range(n):
        cur = min(f[i][0], f[i][1]) + c1 * (n - i - 1)  
        ans = min(ans, cur)
    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()