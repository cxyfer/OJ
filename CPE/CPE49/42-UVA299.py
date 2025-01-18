"""
    Bubble Sort
"""

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                ans += 1
    print("Optimal train swapping takes {} swaps.".format(ans))