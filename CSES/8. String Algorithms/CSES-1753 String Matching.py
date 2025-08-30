s = input().strip()
t = input().strip()

s = t + "#" + s
n, m = len(s), len(t)

ans = 0
pi = [0] * n
ln = 0
for i in range(1, n):
    while ln and s[i] != s[ln]:
        ln = pi[ln - 1]
    if s[i] == s[ln]:
        ln += 1
    pi[i] = ln
    if ln == m:
        ans += 1
        ln = pi[ln - 1]
print(ans)