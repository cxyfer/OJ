"""
    KMP
    tags: CPE-130528
    Similar to
        - Leetcode 214. Shortest Palindrome
        - 111台大資工所 第11題
    差別在上面兩題是從**前面*添加，這題是從**後面**添加
"""
while True:
    try:
        s = input()
    except EOFError:
        break
    n = len(s)
    s = ' ' + s[::-1] + '#' + s # 使下標從1開始
    m = 2 * n + 1 # 實際長度
    next = [0] * (m + 1)
    k = 0
    for i in range(2, m + 1):
        while k > 0 and s[k + 1] != s[i]:
            k = next[k]
        if s[k + 1] == s[i]:
            k += 1
        next[i] = k
    # next[m] 表示 rev(s) 的前綴 和 s 的後綴 的最長公共部分
    added = n - next[m] # 需要在原字串**後面**添加的字元數
    print(s[n+2:] + s[n+1-added:n+1]) # 原字串(後半) + 反轉部分(前半)去除**重疊前綴**

