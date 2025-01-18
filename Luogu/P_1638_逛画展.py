n, m = map(int, input().split())
A = list(map(int, input().split()))

st, ed = 0, n - 1 # ans
cnt = [0] * (m + 1)
left = have = 0
for right, x in enumerate(A):
    cnt[x] += 1
    if cnt[x] == 1:
        have += 1
    while have == m:
        if right - left + 1 < ed - st + 1:
            st, ed = left, right
        cnt[A[left]] -= 1
        if cnt[A[left]] == 0:
            have -= 1
        left += 1
print(st + 1, ed + 1)