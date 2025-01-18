"""
    進制轉換
    base-10 下若一個數字的數位和為 9 的倍數，則該數字也是9的倍數
    可推廣到 base-r 下，若一個數字的每位總和為 r-1 的倍數，則該數字也是 r-1 的倍數

    翻了比較古老的翻譯，測資可能是包含非合法字元的，所以要先判斷是不是英文或數字
"""

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    A = [] # 逐位轉換成數字
    for ch in line:
        if ch.isdigit(): # [0, 9]
            A.append(int(ch))
        elif ch.isupper(): # [10, 35]
            A.append(ord(ch) - ord("A") + 10)
        elif ch.islower(): # [36, 61]
            A.append(ord(ch) - ord("a") + 36)

    ans = -1
    r = max(A) + 1 # 最小必須為 base-r
    s = sum(A) 
    for i in range(max(2, r), 63):
        if s % (i-1) == 0:
            ans = i
            break
    print(ans if ans != -1 else "such number is impossible!")