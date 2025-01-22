n = int(input())
A = list(map(int, input().split()))

cnt = [0] * 10
for x in A:
    cnt[x] += 1

q, r = divmod(n, 9)
cnt1 = cnt2 = 0
for i in range(1, 10):
    if cnt[i] == q:
        cnt1 += 1
    elif cnt[i] == q+1:
        cnt2 += 1
    else:
        exit(print("NO"))

print("YES" if cnt2 == r and cnt1 == 9 - r else "NO")