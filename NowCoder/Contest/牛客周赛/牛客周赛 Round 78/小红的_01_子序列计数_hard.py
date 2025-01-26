MOD = 10**9 + 7

class Modular:
    def __init__(self, val):
        self.val = val % MOD

    def __int__(self):
        return self.val

    def __add__(self, other):
        if isinstance(other, Modular):
            return Modular(self.val + other.val)
        else:
            return Modular(self.val + other)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Modular):
            return Modular(self.val - other.val)
        else:
            return Modular(self.val - other)

    def __rsub__(self, other):
        return Modular(other - self.val)

    def __mul__(self, other):
        if isinstance(other, Modular):
            return Modular(self.val * other.val)
        else:
            return Modular(self.val * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Modular):
            return self * other.inv()
        else:
            return self * pow(other, MOD - 2, MOD)

    def __rtruediv__(self, other):
        return Modular(other) / self

    def __pow__(self, other):
        return Modular(pow(self.val, other, MOD))

    def __neg__(self):
        return Modular(-self.val)

    def inv(self):
        return pow(self, MOD - 2)

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

Z = lambda x: Modular(x)

n = int(input())
s = input()
s = "?" + s + s  # 擴展字串處理環形
ps = [0] * (2 * n + 1) # 前綴和陣列，紀錄 '0' 的數量
for l in range(1, 2 * n + 1):
    ps[l] = ps[l - 1] + (1 if s[l] == '0' else 0)

mul = Z(0)
sum0 = Z(0)
cnt = Z(0)
pos = Z(0)
for l in range(1, n + 1):
    if s[l] == '1':
        mul += ps[l] * (n - (l - 1))
        sum0 += ps[l]
        cnt += 1
        pos += (n - (l - 1))

ans = mul
for l in range(2, n + 1):
    r = l + n - 1
    if s[l - 1] == '1': # 視窗滑出一個 '1'
        mul -= ps[l - 1] * n
        sum0 -= ps[l - 1]
        cnt -= 1
        pos -= n

    mul += sum0 # 更新 mul 和 pos
    pos += cnt

    if s[r] == '1': # 視窗滑入一個 '1'
        mul += ps[r]
        sum0 += ps[r]
        cnt += 1
        pos += 1

    add = mul - Modular(ps[l - 1]) * pos # 計算權值增量
    ans += add

print(int(ans))