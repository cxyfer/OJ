"""
    固定 a 和 b 構成的線段，若 c 和 d 在該線段兩側，則兩條線段相交
    由於 a 和 b 構成的線段中，其中一段會存在 a < b 的大小關係，因此只需判斷 c 和 d 是否在 a 和 b 之間即可\
    若兩個都在 a 和 b 之間、或都不在 a 和 b 之間，則不相交；反之則相交。
"""
t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    if a > b:
        a, b = b, a
    ck1 = a < c < b # c 是否在右側
    ck2 = a < d < b # d 是否在右側
    print("YES" if ck1 ^ ck2 else "NO") # 兩個都不在右側或都在右側，則不相交