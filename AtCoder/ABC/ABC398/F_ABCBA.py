s = input()
n = len(s)

s = s[::-1] + '#' + s
m = 2 * n + 1
pi = [0] * m
ln = 0
for i in range(1, m):
    while ln and s[ln] != s[i]:
        ln = pi[ln - 1]
    if s[ln] == s[i]:
        ln += 1
    pi[i] = ln
added = n - pi[m - 1]

print(s[n+1:] + s[n-added:n])