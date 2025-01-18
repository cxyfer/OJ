T = int(input())

for tc in range(1, T+1):
    s = input()
    n = len(s)

    tol_0 = s.count('0')
    tol_1 = n - tol_0

    def check(k): # 刪除 k 個 字元 是否能滿足條件
        if k == n:
            return True
        cnt_0 = s[:n-k].count('0')
        cnt_1 = s[:n-k].count('1')
        # print(cnt_0, cnt_1, tol_0, tol_1)
        if cnt_1 <= tol_0 and cnt_0 <= tol_1:
            return True
        else:
            return False

    # Binart search
    left, right = 0, n
    while left <= right: # [left, right]
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1

        else:
            left = mid + 1
            
    print(left)
