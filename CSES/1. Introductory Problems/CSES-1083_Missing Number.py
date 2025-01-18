n = int(input())
arr = list(map(int, input().split()))
ans = n
for i, x in enumerate(arr):
    ans ^= (i+1) ^ x
print(ans)