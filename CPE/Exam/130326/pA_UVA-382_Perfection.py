import sys

MAXN = int(6e4) + 5
s = [0] * MAXN # 因數的和
for i in range(1, MAXN): 
    for j in range(i, MAXN, i):
        s[j] += i
for i in range(1, MAXN): # 去除自己
    s[i] -= i

data = map(int, sys.stdin.read().split())

print("PERFECTION OUTPUT")
for x in data:
    if x == 0:
        break
    if s[x] == x:
        print(f"{x:>5}  PERFECT")
    elif s[x] < x:
        print(f"{x:>5}  DEFICIENT")
    else:
        print(f"{x:>5}  ABUNDANT")
print("END OF OUTPUT")