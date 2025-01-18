"""
    模擬(Simulation)
"""
while True:
    H, U, D, F = map(int, input().split())
    if H == 0 and U == 0 and D == 0 and F == 0:
        break
    f = U * F / 100 # fatigue factor
    ans, cur = 0, 0 # day, current height
    while cur >= 0 and cur <= H:
        ans += 1
        cur += U
        U = max(0, U - f) # 上升高度衰減，但不會衰減到負值
        if cur > H: # 爬出井口
            flag = True
            break
        cur -= D # 掉落高度
        if cur < 0:
            flag = False
            break
    print("success" if flag else "failure", "on day", ans)