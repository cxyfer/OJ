""" UVA 10170 - The Hotel with Infinite Rooms
    Math + Binary Search
    Python 不二分會 TLE
"""
while True:
    try:
        S, D = map(int, input().split())
    except:
        break
    # (S + S + k) * (k + 1) / 2 >= D
    # for k in range(0, D+1):
    #     if (2 * S + k) * (k + 1) >= 2 * D:
    #         print(S + k)
    #         break
    left, right = 0, D
    while left <= right:
        mid = (left + right) // 2
        if (2 * S + mid) * (mid + 1) >= 2 * D:
            right = mid - 1
        else:
            left = mid + 1
    print(S + left)

