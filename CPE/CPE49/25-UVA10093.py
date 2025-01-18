"""
    進制轉換
    base-10下若一個數字的數位和為 9 的倍數，則該數字也是9的倍數
    可推廣到 base-r 下，若一個數字的每位總和為 r-1 的倍數，則該數字也是 r-1 的倍數

    翻了比較古老的翻譯，測資可能是包含非合法字元的，所以要先判斷是不是英文或數字
"""

while True:
    try:
        # N = list(input().strip())
        line = input().strip()
    except EOFError:
        break
    # for i, x in enumerate(N):
    #     if ord("A") <= ord(x) <= ord("Z"):
    #         N[i] = ord(x) - ord("A") + 10
    #     elif ord("a") <= ord(x) <= ord("z"):
    #         N[i] = ord(x) - ord("a") + 36
    #     else:
    #         N[i] = int(x)
    N = []
    for ch in line:
        if ch.isupper():
            N.append(ord(ch) - ord("A") + 10)
        elif ch.islower():
            N.append(ord(ch) - ord("a") + 36)
        elif ch.isdigit():
            N.append(int(ch))

    ans = -1
    r = max(N) + 1 # 最小必須為 base-r
    s = sum(N) 
    for i in range(max(2, r), 63):
        if s % (i-1) == 0:
            ans = i
            break
    print(ans if ans != -1 else "such number is impossible!")