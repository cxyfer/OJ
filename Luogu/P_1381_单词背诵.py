from collections import defaultdict

n = int(input())
words1 = [input().strip() for _ in range(n)]
words1 = set(words1)
m = int(input())
words2 = [input().strip() for _ in range(m)]

cnt = defaultdict(int)
ans1, ans2 = 0, float('inf')
left = have = 0
for right, word in enumerate(words2):
    cnt[word] += 1
    if cnt[word] == 1 and word in words1:
        have += 1
        ans1 = have
        ans2 = right - left + 1
    while left <= right and (words2[left] not in words1 or cnt[words2[left]] > 1):
        cnt[words2[left]] -= 1
        left += 1
    ans2 = min(ans2, right - left + 1)

print(ans1)
print(ans2)