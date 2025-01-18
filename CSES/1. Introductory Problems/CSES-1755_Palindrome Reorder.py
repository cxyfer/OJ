S = input()

cnt = [0] * 26
for ch in S:
    cnt[ord(ch) - ord('A')] += 1
flag = True
ans = ""
mid = ""
for i in range(26):
    ch = chr(i + ord('A'))
    if cnt[i] & 1:
        if mid != "":
            flag = False
            break
        mid = ch
    ans += ch * (cnt[i] // 2)
if not flag:
    print("NO SOLUTION")
else:
    print(ans + mid + ans[::-1])
