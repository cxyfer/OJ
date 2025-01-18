tc = 1
while True:
    # input
    line = input()
    if tc > 1: # 跳過空行
        line = input() 
    n, d = map(int, line.split())
    if n == 0 and d == 0:
        break
    islands = []
    for _ in range(n):
        line = input()
        islands.append(list(map(int, line.split())))
    
    flag = False
    intervals = []
    for x, y in islands:
        if y > d: # 不可能放置
            flag = True
            break
        dx = (d*d - y*y)**0.5
        intervals.append((x - dx, x + dx)) # 可以涵蓋這個島嶼的雷達其所屬的區間

    intervals.sort(key = lambda x: x[1]) # 按照右端點排序
    ans = 0
    last = -float("inf") # 上一個組的第一個區間的右端點
    for x, y in intervals:
        if x > last: # 和上一組的所有區間不重疊
            last = y
            ans += 1
    print(f"Case {tc}: {ans if not flag else -1}")
    tc += 1
