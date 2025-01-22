from collections import defaultdict

"""
移動最後一段的 1
x       xxxxx00110011110
x+lb    xxxxx00110100000
xor               111110
res     xxxxx00110100111
"""
def g(x):
    lb = x & -x
    res = x + lb
    xor = x ^ res
    # for i in range(bin(xor)[2:].count('1') - 2):
    #     res |= (1 << i)
    # return res
    return res | (xor >> (lb.bit_length() - 1 + 2))

n = int(input())
A = list(map(int, input().split()))

f = defaultdict(int)
st = -1
for x in sorted(set(A), reverse=True):
    y = g(x)
    f[x] = 1 + f[y]
    if f[x] > f[st]:
        st = x

ans = []
x = st
while f[x] > 0:
    ans.append(x)
    x = g(x)

print(len(ans))
print(*ans)