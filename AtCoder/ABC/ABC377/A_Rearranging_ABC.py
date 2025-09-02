from collections import Counter

cnt = Counter(input())
print("Yes" if all(cnt[ch] == 1 for ch in "ABC") else "No")