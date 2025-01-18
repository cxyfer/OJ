"""
難點在於不能直接對A[i]做操作，再和A[i+1]比較，這樣會TLE

就是说比方当前这个数需要×2才能比前一个数大，如果说前一个数为了满足条件已经扩展了2倍了，那当前这个数需要扩大2*2倍（例子：13 7 4）
"""
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    pre = 0 # 保存前一個數字的操作次數
    for i in range(1, N):
        x = A[i]
        if A[i-1] > x:
            while(A[i-1] > x):
                x *= 2
                pre += 1
        else:
            while(A[i-1] * 2 <= x and pre > 0) :
                x /= 2
                pre -= 1
        ans += pre
    print(ans)