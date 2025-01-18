T = int(input())

def check(k):
    x, y = 0, 0 # 起始的區間範圍
    for l, r in LR:
        nx = max(x - k, l) # 下一個區間的最左邊界
        ny = min(y + k, r) # 下一個區間的最右邊界
        if nx <= ny: # 如果下一個區間合法，即左邊界<=右邊界，則更新區間範圍
            x, y = nx, ny
        else: 
            return False
    return True

for tc in range(1, T+1):
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]

    l, r = 0, 10**9
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            r = mid - 1
        else:
            l = mid + 1
    print(l)
