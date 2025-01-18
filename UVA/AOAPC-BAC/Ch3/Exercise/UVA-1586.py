t = int(input())

mp = {'C': 12.01, 'H': 1.008, 'O': 16.00, 'N':14.01}

for _ in range(t):
    s = input().strip() # 居然有空格，因為這個一直RE
    n = len(s)
    ans = 0
    i = 0
    while (i < n): # 分組循環
        ch = s[i]
        i += 1
        cur = 0
        while (i < n and s[i].isdigit()):
            cur = cur * 10 + int(s[i])
            i += 1
        if not cur:
            cur = 1
        ans += mp[ch] * cur
    print(f"{ans:.3f}")