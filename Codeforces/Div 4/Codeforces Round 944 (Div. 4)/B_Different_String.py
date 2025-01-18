"""
    檢查字串 s 是否僅由一個字元組成即可
    以第一個字元為基準，檢查有沒有不同的字元
    重構方案可以直接交換第一個字元和第一個不同的字元
    但因為python不能直接交換字串的字元，所以用另外一種方式，將第一個不同的字元左移到字串的最左邊
"""
t = int(input())
for _ in range(t):
    s = input()
    for i in range(1, len(s)):
        if s[i] != s[0]:
            print("YES")
            print(s[i:] + s[:i])
            break
    else:
        print("NO")