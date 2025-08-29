"""
P3375 【模板】KMP
https://www.luogu.com.cn/problem/P3375

注意輸入可能有多餘的空格，需要使用 strip() 去除
"""
s = input().strip()
t = input().strip()
n, m = len(s), len(t)

# 計算 t 的 pi 陣列
pi = [0] * m
ln = 0
for i in range(1, m):
    while ln and t[i] != t[ln]:
        ln = pi[ln - 1]
    if t[i] == t[ln]:
        ln += 1
    pi[i] = ln

ln = 0
for i in range(n):
    while ln > 0 and (ln == m or s[i] != t[ln]):
        ln = pi[ln - 1]
    if s[i] == t[ln]:
        ln += 1
    if ln == m:
        print(i - m + 2)

print(*pi)