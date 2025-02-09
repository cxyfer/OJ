n = int(input().strip())

mx = idx = -1
for i in range(1, n + 1):
    x = int(input().strip())
    if x > mx:
        mx = x
        idx = i

print(idx)
print(mx)