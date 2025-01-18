import random

"""
    HashString 模板

    多項式字串雜湊（方便計算子字串雜湊值）
    雜湊函數： hash(s) = s[0] * BASE^(n-1) + s[1] * BASE^(n-2) + ... + s[n-2] * BASE + s[n-1]

    Problem:
    - 3213. Construct String with Minimum Cost

    Reference:
    - https://leetcode.cn/problems/construct-string-with-minimum-cost/solutions/2833949/hou-zhui-shu-zu-by-endlesscheng-32h9
    - https://leetcode.cn/problems/minimum-number-of-valid-strings-to-form-target-ii/solutions/2917834/liang-chong-jie-fa-tan-xin-ac-zi-dong-ji-u6wc
"""

MOD = 1_070_777_777
BASE = random.randint(8 * 10 ** 8, 9 * 10 ** 8)
# MOD = int(1e18) + random.randint(0, int(1e9))
# BASE = 233 + random.randint(0, 1000)

class HashString:
    # 初始化 HashString ，預計算所有冪次和前綴雜湊
    def __init__(self, s: str):
        self.n = len(s)
        self.P = [1] + [0] * self.n  # P[i] = BASE^i % MOD
        self.H = [0] * (self.n + 1)  # H[i] = hash(s[:i])
        
        for i, b in enumerate(s):
            # 預計算所有冪次
            self.P[i + 1] = self.P[i] * BASE % MOD
            # 預計算所有前綴雜湊
            self.H[i + 1] = (self.H[i] * BASE + ord(b)) % MOD 

    # 計算子字串 s[l-1..r-1] 的雜湊值 (1-indexed)，計算方法類似前綴和
    def query(self, l: int, r: int) -> int:
        return (self.H[r] - self.H[l - 1] * self.P[r - l + 1]) % MOD