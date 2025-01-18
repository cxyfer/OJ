from functools import cache
t = int(input())

for _ in range(t):
    x = input()
    y = input()

    # 當前匹配到 y 的第 i 個字元，x 的第 j 個字元，此區段剩餘修改次數為 k
    @cache
    def f(i, j, k):
        if i == len(y) and j == len(x):
            return True
        if i == len(y):
            return False
        if j == len(x):
            j = 0
        res = False
        if x[j] == y[i]: # 可以不修改
            res |= f(i + 1, j + 1, k)
        if k > 0: # 可以修改
            res |= f(i + 1, j, k - 1) # 增加
            res |= f(i, j + 1, k - 1) # 刪除
            res |= f(i + 1, j + 1, k - 1) # 修改
        return res

    left, right = 0, min(len(x), len(y))
    while left <= right:
        mid = (left + right) // 2
        if f(0, 0, mid):
            right = mid - 1
        else:
            left = mid + 1
    print(right if right != -1 else 0)

