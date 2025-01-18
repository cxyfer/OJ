B = int(input())
# x ** x = B
ans = -1
for i in range(1, B+1):
    if i**i > B:
        ans = -1
        break
    elif i**i == B:
        ans = i
        break
print(ans)