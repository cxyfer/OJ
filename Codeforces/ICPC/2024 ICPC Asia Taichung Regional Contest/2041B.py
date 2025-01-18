t = int(input())

def check(k, w, b):
    for x in range(k, 0, -1):
        if w >= b:
            if w >= x:
                w -= x
            else:
                return False
        else:
            if b >= x:
                b -= x
            else:
                return False
    return True

for _ in range(t):
    w, b = map(int, input().split())

    left, right = 0, int(1e5)
    while left <= right:
        mid = (left + right) // 2
        if check(mid, w, b):
            left = mid + 1
        else:
            right = mid - 1
    print(right)