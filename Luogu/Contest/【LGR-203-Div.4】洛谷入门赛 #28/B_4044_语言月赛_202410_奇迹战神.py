n = int(input())

arr = []
for _ in range(n):
    w, d = map(int, input().split())
    arr.append(w + d * 7)

print(min(arr) - 6)