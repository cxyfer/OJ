"""
    Binary Search
    tags: CPE-131001
"""
while True:
    try:
        n = int(input())
    except EOFError:
        break

    left, right = 1, 10**7
    while left <= right:
        mid = (left + right) // 2
        if mid * (mid + 1) // 2 < n:
            left = mid + 1
        else:
            right = mid - 1
    k = n - left * (left - 1) // 2 # 第 left 斜行的第 k 個數字
    if left & 1:
        print(f"TERM {n} IS {left-k+1}/{k}")
    else:
        print(f"TERM {n} IS {k}/{left-k+1}")