from collections import defaultdict
from string import ascii_lowercase

n, f = map(int, input().split())
s = list(input())

ans = set()
cnt = defaultdict(int)

def check(i):
    if i < 0 or i + 2 >= n:
        return False
    return s[i] != s[i + 1] and s[i + 1] == s[i + 2]

def modify(i, ch):
    for j in range(i - 2, i + 1):
        if check(j):
            sub = "".join(s[j:j + 3])
            cnt[sub] -= 1
    s[i] = ch
    for j in range(i - 2, i + 1):
        if check(j):
            sub = "".join(s[j:j + 3])
            cnt[sub] += 1
            if cnt[sub] == f:
                ans.add(sub)

for i in range(n):
    if check(i):
        sub = "".join(s[i:i + 3])
        cnt[sub] += 1
        if cnt[sub] == f:
            ans.add(sub)

for i in range(n):
    ori = s[i]
    for ch in ascii_lowercase:
        if ch == ori:
            continue
        modify(i, ch)
    modify(i, ori)

print(len(ans))
for sub in sorted(ans):
    print(sub)