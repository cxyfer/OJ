N = int(input())
S = input()
ans = "No"
for i in range(1, N):
    if S[i] == "a" and S[i-1] == "b" or S[i] == "b" and S[i-1] == "a":
        ans = "Yes"
        break
print(ans)