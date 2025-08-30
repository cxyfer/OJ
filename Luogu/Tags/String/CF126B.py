"""
CF126B Password
https://codeforces.com/problemset/problem/126/B

所求同時為 s 的前綴、後綴、且在 s 中出現，
即 s 的一個真前後綴(border)，且也是 s 的某個子字串的真前後綴

abcabcabca
   abca
      abca
"""
from functools import reduce

s = input()
n = len(s)

pi = [0] * n
ln = 0
for i in range(1, n):
    while ln and s[ln] != s[i]:
        ln = pi[ln - 1]
    if s[ln] == s[i]:
        ln += 1
    pi[i] = ln

# mx = max(pi[:-1], 0)
mx = reduce(max, pi[:-1], 0)
ln = pi[n - 1]
while ln > mx:  #
    ln = pi[ln - 1]
if ln == 0:
    print("Just a legend")
else:
    print(s[:ln])