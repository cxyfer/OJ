"""
    創造一條有N個點的Path，並且有Q個操作，每個操作都是把最後一個點移動到某個點上
    答案不唯一，只要符合條件即可

    以範例的第2個測資為例：
    d1 = 4 => output: (-1, -1, -1)
    1 - 2 - 3 - 4 - 5

    d2 = 2 => output: (5, 4, 2)
    1 - 2 - 3 - 4 
        5

    d3 = 3 => output: (5, 2, 3)
    1 - 2 - 3 - 4
            5
"""
T = int(input())

for _ in range(T):
    N, Q = map(int, input().split())
    D = [int(input()) for _ in range(Q)]
    # print edges
    for i in range(1, N):
        print(i, i + 1)
    # print operation
    last = N - 1 # 上次移動到哪個點上
    for d in D:
        if last == d:
            print(-1, -1, -1)
        else:
            print(N, last, d)
            last = d
