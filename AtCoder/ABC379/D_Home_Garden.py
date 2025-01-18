"""
維護一個變數 tot 表示總經過時間，
則操作 2 中只需將 tot 加上 T 即可，不用真的改變每棵植物的生長時間：
而在操作 1 中，則是紀錄植物的種植時間到 plants 中。

在操作 3 中，我們需要找到有多少還沒被收割的植物高度 >= H。
因此可以維護一個變數 idx 表示第一個還沒被收割的植物下標，
每次操作 3 時，不斷檢查 plants[idx] + tot - H 是否 >= 0，
如果 >= 0 則將 idx 右移，直到不滿足條件為止，則移動的次數即為答案。

也可以用 queue 來維護 plants，思路相同。
此外，由於 plants 是單調遞增的，因此也可以用二分搜尋來找到第一個滿足條件的植物下標。
"""
Q = int(input())
plants = [] # 紀錄植物的種植時間
idx = 0 # 第一個還沒被收割的植物下標
tot = 0 # 總經過時間
for _ in range(Q):
    op, *args = input().split()
    if op == '1':
        plants.append(tot)
    elif op == '2':
        T = int(args[0])
        tot += T
    elif op == '3':
        H = int(args[0])
        st = idx
        while idx < len(plants) and tot - plants[idx] >= H:
            idx += 1
        print(idx - st)