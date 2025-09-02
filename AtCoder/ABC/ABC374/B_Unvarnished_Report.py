S = input()
T = input()
if len(S) < len(T):
    S += "#" * (len(T) - len(S))
elif len(S) > len(T):
    T += "#" * (len(S) - len(T))

for i in range(len(S)):
    if S[i] != T[i]:
        print(i + 1)
        break
else:
    print(0)
