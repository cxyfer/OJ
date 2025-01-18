"""
    模擬 / 奇偶性
    由於 n <= 100，因此可以直接模擬。
    但可以觀察到 Sakurako 會讓值變成負的奇數；而 Kosuke 會讓值變成正的偶數，
    因此可以直接判斷奇偶性即可。
"""

t = int(input())

for _ in range(t):
    n = int(input())
    print("Kosuke" if n & 1 else "Sakurako")