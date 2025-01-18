"""
    1. 組合數學
    由於出現連續三個以上U的情況被視為不合法，因此可以反過來求合法的情況，再用總情況減去合法情況即可
    枚舉單獨1個U的數量 u1 和連續2個U的數量 u2，再使其不相鄰。
    插空格的方法：假設有 k 個L，則有 k+1 個空格可以插入，因此有 C(n+1, u1+u2) 種插法
    而 u1 和 u2 又可以存在排列，因此又有 (u1+u2)! / (u1! * u2!) = C(u1+u2, u1) 種排列方式

    2. 動態規劃(DP)
"""
def solve1(): # Math
    # from math import factorial as fact # built-in 的 fact 已經預先計算好部分數值了，速度較快
    from functools import cache

    @cache
    def fact(n):
        return 1 if n <= 1 else n * fact(n-1)
    
    while True:
        n = int(input())
        if n == 0:
            break
        legal = 0
        for u1 in range(n+1):
            for u2 in range(n//2+1):
                k = n - u1 - 2*u2 # 剩餘的L數量
                if k + 1 < u1 + u2: # 空格不夠
                    break
                # c1 = fact(k+1) // (fact(u1+u2) * fact(k+1-u1-u2)) # C(k+1, u1+u2) 插空格的方法
                c1 = fact(k+1) // fact(k+1-u1-u2)
                # c2 = fact(u1+u2) // (fact(u1) * fact(u2)) # (u1+u2)! / (u1! * u2!) 重複物排列
                c2 = (fact(u1) * fact(u2))
                # legal += c1 * c2
                legal += c1 // c2
                # print(c1, c2, legal)
        print(pow(2, n)- legal) # 總情況 - 合法情況

def solve2():
    from functools import cache

    @cache
    def f(i, j): # f(i, j) 表示長度為 i 的字串，後綴中有連續 j 個 U 的情況數
        if i == 0:
            return 1 if j == 0 else 0
        if j == 0:
            return f(i-1, 0) + f(i-1, 1) + f(i-1, 2)
        if j == 1:
            return f(i-1, 0)
        if j == 2:
            return f(i-1, 1)

    while True:
        n = int(input())
        if n == 0:
            break
        print((1 << n) - sum(f(n, i) for i in range(3)))
        
if __name__ == "__main__":
    # solve1()
    solve2()