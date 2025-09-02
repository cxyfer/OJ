N = int(input())
A = list(map(int, input().split()))
mx = max(A) # 10**6

cnt, s = [0] * (mx + 1), [0] * (mx + 1)
for a in A:
    cnt[a] += 1
for i in range(1, mx + 1): # Prefix Sum
    s[i] = s[i - 1] + cnt[i]
ans = 0
for i in range(1, mx + 1):
    ans += cnt[i] * (cnt[i] - 1) // 2 # 和自己本身對答案的貢獻
    for j in range(i, mx + 1, i):
        l = i + 1 if j == i else j # 排除自己本身
        r = min(mx, j + i - 1)
        ans += cnt[i] * (j // i) * (s[r] - s[l - 1])
print(ans)