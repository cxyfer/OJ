"""
    Greedy
    子序列分成找比當前數字更小/更大的數字兩種情況；
    - 在找小的時候若遇到比目前數字更大的數，則可以將目前數字更新成此較大的數字，此時由於範圍變大，會更容易找到更小的數字。
    - 反之同理，在找大的時候若遇到比目前數字更小的數，則可以將目前數字更新成此較小的數字
    因此可以維護一個 cur 變數，用來記錄目前的數字，並且用 flag 變數來記錄目前是在找比目前數字更小的數字還是更大的數字。
    但在實作時不難發現 cur 永遠指向前一個數字，因此只要與前一個數字比較即可。
"""
t = int(input())
for _ in range(t):
    n, *nums = map(int, input().split())
    ans = 1
    flag = 0 # 0: find smaller, 1: find larger
    for i in range(1, n):
        if flag == 0:
            if nums[i] < nums[i-1]:
                ans += 1
                flag ^= 1
        else:
            if nums[i] > nums[i-1]:
                ans += 1
                flag ^= 1
    print(ans)

# t = int(input())
# for _ in range(t):
#     n, *nums = map(int, input().split())
#     ans = 1
#     cur = nums[0]
#     flag = 0 # 0: find smaller, 1: find larger
#     for i in range(1, n):
#         if flag == 0:
#             if nums[i] < cur:
#                 ans += 1
#                 flag ^= 1
#                 cur = nums[i]
#             else:
#                 cur = nums[i]
#         else:
#             if nums[i] > cur:
#                 ans += 1
#                 flag ^= 1
#                 cur = nums[i]
#             else:
#                 cur = nums[i]
#     print(ans)