M = int(input())
days = list(map(int, input().split()))
mid = (sum(days) + 1) // 2 # Middle day

# Find the middle day
for i in range(0, M):
    if mid - days[i] <= 0:
        print(i + 1, mid)
        break
    else:
        mid -= days[i]