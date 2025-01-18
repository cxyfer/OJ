T = int(input())

for _ in range(T):
    n, m = map(int, input().split()) # n vertices, m edges
    for k in range(n-1, -1, -1): # 枚舉關鍵點的數量 k
        x = n - k # 剩餘x個點，是否可以構成強連通分量
        # k條邊使k個關鍵點連接到該強連通分量，剩餘 m-k 邊皆屬於該強連通分量，該強連通分量最多有 x*(x-1)/2 條邊
        if x * (x-1) // 2 >= m - k: 
            print(k)
            break