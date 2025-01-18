"""
均值不等式
Ref: https://www.luogu.com.cn/article/zwoav93f
"""

S = int(input())
a, b, c = map(int, input().split())

if a + b + c == 0:
    print(S, 0, 0)
else:
    f = S / (a + b + c)
    print(a * f, b * f, c * f)
