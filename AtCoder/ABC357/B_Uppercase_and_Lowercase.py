S = input()
cnt1, cnt2 = 0, 0
for ch in S:
    if ch.islower():
        cnt1 += 1
    else:
        cnt2 += 1
print(S.lower() if cnt1 >= cnt2 else S.upper())
