from collections import Counter

N = int(input())
A = list(map(int, input().split()))

ans = [0] * N

cnt = Counter(A)
nums = [(val, idx) for idx, val in enumerate(A)]
nums.sort()

suf = [0] * N # suf[i]表示nums中大於nums[i]的元素之和

for i in range(N-2, -1, -1):
    cur = nums[i][0] # 當前元素
    nxt = nums[i+1][0] # Array中的下一個元素，計算後綴和過程的前一個元素
    if cur < nxt: # 元素不相等，則後綴和為後一個元素的後綴和加上後一個元素的個數乘以後一個元素的值
        suf[i] = suf[i+1] + cnt[nxt] * nxt
    else: # 元素相等，則不能更新後綴和，後綴和為後一個元素的後綴和
        suf[i] = suf[i+1]

for i, (val, idx) in enumerate(nums): # 按照原本的順序，更新答案
    ans[idx] = suf[i]
print(*ans)
