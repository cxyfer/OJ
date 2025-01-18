"""
    分組循環，每組都僅由 0 或 1 組成，且相鄰兩組不同
    若有一組 0 後面接著一組 1 ，則這兩組不用分開
"""
t = int(input())

for _ in range(t):
    s = input()
    i = 0
    ans = 0
    flag = False # 有沒有一組 0 後面接著一組 1
    while i < len(s):
        st = i
        i += 1
        while i < len(s) and s[i] == s[st]:
            i += 1
        if s[st] == "0" and i < len(s) and s[i] == "1":
            flag = True
        ans += 1
    print(ans - flag) # 有一組 0 後面接著一組 1，則該兩組不用分開，答案減一