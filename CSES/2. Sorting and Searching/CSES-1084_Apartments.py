n, m, k = map(int, input().split())
arr = sorted(map(int, input().split()))
brr = sorted(map(int, input().split()))

ans = 0
i = j = 0
while i < n and j < m:
    if arr[i] + k < brr[j]: # 公寓面積比最大需求大，換下一個人
        i += 1
    elif arr[i] - k > brr[j]: # 公寓面積比最小需求小，換下一個公寓
        j += 1
    else: # 符合條件
        i += 1
        j += 1
        ans += 1
print(ans)