""" UVA 12428 - Enemy at the Gates
    Greedy (+ Binary Search )
"""

def solve1():
    n, m = map(int, input().split()) # n vertices, m edges
    for k in range(n-1, -1, -1): # 枚舉關鍵點的數量 k
        x = n - k # 剩餘x個點，是否可以構成強連通分量
        # k條邊使k個關鍵點連接到該強連通分量，剩餘 m-k 邊皆屬於該強連通分量，該強連通分量最多有 x*(x-1)/2 條邊
        if x * (x-1) // 2 >= m - k: 
            print(k)
            break
def solve2():
    n, m = map(int, input().split()) # n vertices, m edges
    def check(k):
        x = n - k
        return x * (x-1) // 2 >= m - k
    left, right = 0, n-1 # [0, n-1]
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    print(right) 

T = int(input())
for _ in range(T):
    # solve1()
    solve2()