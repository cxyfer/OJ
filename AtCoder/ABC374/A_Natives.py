n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(sum(arr[(n+1)//2:]))