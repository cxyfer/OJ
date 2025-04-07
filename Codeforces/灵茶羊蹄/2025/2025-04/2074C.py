"""
z = x ^ y

y < x
x + y > z
y + z > x -> z > x - y
z + x > y -> 恆成立

得到 x - y < z < x + y

利用
x + y = (x ^ y) + 2 * (x & y)
x - y = (x ^ y) - 2 * (~x & y)

所以當
x & y = 0 時，x + y = x ^ y
~x & y = 0 時，x - y = x ^ y
此兩種情況會使 x - y < z < x + y 不成立

為了避免這兩種情況，應該取 
x 的最低位 1 和 ~x 的最低位 1
"""

t = int(input())
lowbit = lambda x: x & -x

for _ in range(t):
    x = int(input())
    y = lowbit(x) | lowbit(~x)
    print(y if y < x else -1)