"""
I. BenzenE
https://ac.nowcoder.com/acm/contest/120563/I
線性基

由於 C[i] 只能是 A[i] 或 B[i]，可以先欽定所有 C[i] = A[i]。
之後選定一個下標集合 S，對集合內的下標 i，將 C[i] 從 A[i] 替換成 B[i]。
替換對於 XOR(C) 的貢獻等同先異或 A[i]，再異或 B[i]。

根據題意，需要滿足：
   XOR(C) = XOR(A) ^ XOR(A[i] ^ B[i]) = 0
=> XOR(A[i] ^ B[i]) = XOR(A)

此問題等同於將所有 A[i] ^ B[i] 作為基底，是否可以表示 XOR(A)。
若能表示 XOR(A)，則存在一個下標集合 S，使得 XOR(C) = 0；否則無解。
"""

from functools import reduce
from operator import xor
from typing import Optional, List

class XorBasis:
    """
    線性基模板
    """

    def __init__(self, B: int = 30):
        self.B = B
        self.b = [0] * self.B  # b[i]：最高位為 i 的基底向量值
        self.m = [0] * self.B  # m[i]：b[i] 由哪些 pivot 組成（bitmask）
        self.rep: List[int] = []  # pivot-id -> 原始 idx

    def insert(self, x: int, idx: Optional[int] = None) -> bool:
        """
        插入向量 x。若提供 idx，會記錄回溯資訊。
        回傳 True 表示線性無關（成功成為新基底），False 表示線性相關。
        """
        msk = 0
        v = x
        for i in range(self.B - 1, -1, -1):
            if (v >> i) & 1:
                if self.b[i] == 0:
                    pid = len(self.rep)
                    self.rep.append(idx)
                    self.b[i] = v
                    self.m[i] = msk ^ (1 << pid)
                    return True
                v ^= self.b[i]
                msk ^= self.m[i]
        return False

    def represent(self, x: int) -> Optional[int]:
        """
        若能表示 x，回傳一個 bitmask，表示使用了哪些插入時的 pivot。
        若不能表示，回傳 None。
        """
        v = x
        msk = 0
        for i in range(self.B - 1, -1, -1):
            if (v >> i) & 1:
                if self.b[i] == 0:
                    return None
                v ^= self.b[i]
                msk ^= self.m[i]
        return msk

    def choose(self, msk: int) -> List[int]:
        """
        把 represent() 得到的 mask 轉成原始 idx 列表。
        """
        res = []
        while msk:
            lb = msk & -msk
            res.append(self.rep[lb.bit_length() - 1])
            msk ^= lb
        return res

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    assert len(A) == len(B) == n

    x = reduce(xor, A)
    xb = XorBasis(30)
    for i, (a, b) in enumerate(zip(A, B)):
        xb.insert(a ^ b, idx=i)

    msk = xb.represent(x)
    if msk is None:
        print(-1)
        return

    ans = A[:]
    for i in xb.choose(msk):
        ans[i] = B[i]

    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()