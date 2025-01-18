from collections import Counter

n = int(input())
s = input()

cnt = Counter(s)
ans = ""
for ch in cnt:
    if cnt[ch] > cnt[ans]:
        ans = ch
print(ans)