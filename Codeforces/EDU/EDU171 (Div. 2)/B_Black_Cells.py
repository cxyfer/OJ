"""
    根據 n 的奇偶性，分別討論
    - n 為奇數，則有一個需要自己一組，和多餘的配對
    - n 為偶數，則必需兩兩配對
"""
t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()

    if n & 1:
        ans = float('inf')
        for i in range(n): # 枚舉需要自己一組的元素
            cur = 0
            j = 0
            while j + 1 < n:
                if j == i:
                    j += 1
                    continue
                cur = max(cur, A[j + 1] - A[j])
                j += 2
            ans = min(ans, cur)
    else:
        ans = 0
        for i in range(0, n, 2):
            ans = max(ans, A[i + 1] - A[i])
    print(max(ans, 1))