N = input()

cnt = [0] * 10
for ch in N:
    cnt[int(ch)] += 1
print("Yes" if (cnt[1] == 1 and cnt[2] == 2 and cnt[3] == 3) else "No")