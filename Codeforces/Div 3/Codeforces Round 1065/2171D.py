"""
題目意思等同於：是否存在一個位置 i ，使得 i + 1 到 n 的數字都小於 1 到 i 的數字。
那麼只要前 i 個數字是最大的 i 個數字，就會導致無法滿足題目條件。
可以用維護前綴最小值來判斷。
"""
def solve():
    n = int(input())
    P = list(map(int, input().split()))

    mn = float('inf')
    for i in range(n - 1):
        mn = min(mn, P[i])
        if mn == n - i:  # 前綴最小值等於 n - i ，則前 i 個數字是最大的 i 個數字
            print("No")
            break
    else:
        print("Yes")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()