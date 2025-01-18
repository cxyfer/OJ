import math

N, X = map(int, input().split())  
processes = [tuple(map(int, input().split())) for _ in range(N)]

def check(capacity):
    tot = 0  
    for A, P, B, Q in processes:
        cost1 = math.ceil(capacity / A) * P
        cost2 = math.ceil(capacity / B) * Q
        cost = min(cost1, cost2)
        for x_s in range(min(math.ceil(capacity / A), 100) + 1):
            r = capacity - x_s * A
            x_t = math.ceil(r / B) if r > 0 else 0
            cost = min(cost, x_s * P + x_t * Q)
        for x_t in range(min(math.ceil(capacity / B), 100) + 1):
            r = capacity - x_t * B
            x_s = math.ceil(r / A) if r > 0 else 0
            cost = min(cost, x_t * Q + x_s * P)
        tot += cost
        if tot > X:
            return False
    return True

left, right = 0, int(1e9)
while left <= right:  
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)