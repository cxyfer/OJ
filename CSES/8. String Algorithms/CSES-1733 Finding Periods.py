s = input().strip()
n = len(s)

pi = [0] * n
ln = 0
for i in range(1, n):
    while ln and s[i] != s[ln]:
        ln = pi[ln - 1]
    if s[i] == s[ln]:
        ln += 1
    pi[i] = ln

ans = []
ln = pi[-1]
while ln > 0:
    ans.append(n - ln)
    ln = pi[ln - 1]
ans += [n]
print(*ans)