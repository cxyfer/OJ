"""
    TLE
"""

N = int(1e6) + 5
cnt = [0] * N
for i in range(1, N):
    for j in range(i, N, i):
        cnt[j] += 1

s = [0] * N
for i in range(1, N):
    s[i] = i if cnt[s[i - 1]] <= cnt[i] else s[i - 1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(s[n])