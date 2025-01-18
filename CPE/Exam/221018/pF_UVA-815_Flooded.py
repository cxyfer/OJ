"""
    因為少了一個空行吃了 WA ，為甚麼不是 Presentation Error
    uDebug 上面有筆測資好像有精準度問題，在那筆資料上也吃了 WA
    兩邊都 WA 讓我以為是過程中有問題，但其實只是少了一個空行

    下面的寫法是計算上升部分的水體積，另外一種寫法是計算包含建築的總體積
    - https://vjudge.net/solution/51813651
"""
kase = 1
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    grids = []
    for i in range(m):
        grids.extend(list(map(int, input().split())))
    grids.sort()
    waters = int(input())

    h = grids[0] # 水位高度
    cnt = 0 # 淹水格子數
    for i in range(m*n-1):
        if waters == 0:
            break
        d = grids[i+1] - grids[i] # 水位上升高度
        cnt += 1
        if d * cnt * 100 <= waters:
            waters -= d * cnt * 100
            h += d
        else:
            up = waters / (cnt * 100)
            waters = 0
            h += up
    if waters > 0:
        cnt = m * n
        h += waters / ((m*n) * 100)

    print(f"Region {kase}")
    kase += 1
    print(f"Water level is {h:.2f} meters.")
    print(f"{cnt*100/(m*n):.2f} percent of the region is under water.")
    print() # Follow the output for each region with a blank line.