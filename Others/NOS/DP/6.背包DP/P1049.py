"""
P1049 [NOIP 2001 普及组] 装箱问题
https://www.luogu.com.cn/problem/P1049
背包DP模板題，求可行性
"""
def solve():
    V = int(input())
    n = int(input())
    A = [int(input()) for _ in range(n)]

    f = 1
    U = (1 << (V + 1)) - 1
    for x in A:
        f |= (f << x)
        f &= U
    print(V - (f.bit_length() - 1))

if __name__ == "__main__":
    solve()