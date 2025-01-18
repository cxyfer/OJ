from typing import List

MAX_N = 10 ** 5
MOD = 10 ** 9 + 7

fac = [1]
for i in range(1, MAX_N+ 1): # 計算階乘
    fac.append(fac[-1] * i % MOD)

"""
    對於 m = (a / b) % MOD 的問題，因為除法不能用同餘定理，我們需要將除法轉換成乘法
    (a / b) % MOD = (a * inv(b, MOD)) % MOD = (a % MOD * inv(b, MOD) % MOD) % MOD
    而 inv(b, MOD) = b ^ (MOD - 2) % MOD ， 證明如下：
    b * inv(b, MOD) = 1 % MOD
    b * inv(b, MOD) = b ^ (MOD - 1) % MOD (費馬小定理)
    inv(b, MOD) = b ^ (MOD - 2) % MOD ，得證
"""
def inv(x): # 求 x 在 MOD 下的乘法逆元(乘法反元素)
    return pow(x, MOD-2, MOD)

class Solution:
    """
        - 首先，將每段視為同一種顏色，排列方式為 n! / (n1! * n2! * n3! * ...)，其中 n1, n2, n3, ... 為各段的長度
        - 再來考慮每個區間的感染方式：
            - 對於只有一側感染的區間，其感染的方法數為 1
            - 對於兩側都感染的區間，其感染的方法數為 2 ^ (區間長度 - 1)
        範例：sick = [0, 4, 8, 12], n = 16
            XaaaXbbbXcccXddd (X表感染)
            非感染區間的長度分別為 3, 3, 3, 3，總長度為 12
            所求為12! / (3! * 3! * 3! * 3!) * 2 ^ (3 - 1) * 2 ^ (3 - 1) * 2 ^ (3 - 1)
    """
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        cl = sick[0] # 左段的長度
        cr = n - 1 - sick[-1] # 右段的長度
        ans = fac[n - len(sick)] # n - len(sick) 為非感染區間的總長度
        for i in range(1, len(sick)):
            di = sick[i] - sick[i-1] - 1 # 兩個感染區間之間的長度
            if di == 0:
                continue
            ans = ans * pow(2, di-1, MOD) % MOD # 2 ^ (di - 1)，此感染區間的感染方式
            ans = ans * inv(fac[di]) % MOD # 除去重複的排列方式
        ans = ans * inv(fac[cl]) * inv(fac[cr]) # 除去左右兩端的重複排列方式
        return ans % MOD

sol = Solution()
print(sol.numberOfSequence(5, [0,4])) # 4
print(sol.numberOfSequence(4, [1])) # 3