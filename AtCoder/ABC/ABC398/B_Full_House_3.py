A = list(map(int, input().split()))

cnt = [0] * 14
for x in A:
    cnt[x] += 1

cnt2 = cnt3 = 0
for i in range(1, 14):
    if cnt[i] >= 3:
        cnt3 += 1
    if cnt[i] >= 2:
        cnt2 += 1

if cnt3 >= 1 and cnt2 >= 2:
    print("Yes")
else:
    print("No")