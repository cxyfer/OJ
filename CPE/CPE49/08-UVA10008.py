from collections import Counter

T = int(input())
cnt = Counter()

for tc in range(T):
    s = input()
    for ch in s:
        if ch.isalpha():
            cnt[ch.upper()] += 1

for k, v in sorted(cnt.items(), key=lambda x: (-x[1], x[0])):
    print(k, v)