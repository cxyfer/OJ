"""
    觀察：
    將最小元素插入到最後面後，即不會再發生變化
    因此若最小元素後有遞減的情況，則不可能操作成非遞減序列
    反之，操作數為最小元素前的元素個數
"""
T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    min_val = float("inf")
    min_idx = -1
    for idx, num in enumerate(A):
        if num < min_val:
            min_val = num
            min_idx = idx
    flag = False # 最小元素後是否有遞減的情況
    for i in range(min_idx + 1, N):
        if A[i - 1] > A[i]: # 出現遞減的情況
            flag = True
            break
    if flag:
        print(-1)
    else:
        print(min_idx)