"""AI 生成，待測試與修改。"""

from functools import reduce
from operator import xor
from typing import Optional, List


class XorBasis:
    """
    通用 XOR 線性基（GF(2)），支援：
    - 插入 / 判斷可表示 / 回溯表示方式（mask -> indices）
    - 最大 XOR / 最小 XOR
    - rebuild + kth（第 k 小 XOR）
    - merge 合併
    """

    def __init__(self, B: int = 30):
        self.B = B
        self.b = [0] * self.B  # b[i]：最高位為 i 的基底向量值
        self.m = [0] * self.B  # m[i]：b[i] 由哪些 pivot 組成（bitmask）
        self.rep: List[int] = []  # pivot-id -> 原始 idx（若 insert 時有提供）
        self.has_dep = False  # 是否插入過線性相關向量（代表可得到 0）

        # rebuild 後用於 kth
        self.p: List[int] = []  # 標準形向量列表（由低到高或任意一致順序）
        self._rebuilt = False

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

        # v 被消成 0：線性相關
        self.has_dep = True
        return False

    def can_represent(self, x: int) -> bool:
        """只判斷 x 是否能由目前線性基表示。"""
        v = x
        for i in range(self.B - 1, -1, -1):
            if (v >> i) & 1:
                if self.b[i] == 0:
                    return False
                v ^= self.b[i]
        return True

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

    def max_xor(self, start: int = 0) -> int:
        """
        求最大 XOR（在所有可由基底生成的值中，start XOR 某組合 的最大值）。
        """
        res = start
        for i in range(self.B - 1, -1, -1):
            if self.b[i] and (res ^ self.b[i]) > res:
                res ^= self.b[i]
        return res

    def min_xor(self, start: int = 0) -> int:
        """
        求最小 XOR（start XOR 某組合 的最小值）。
        若存在線性相關（has_dep=True），則最小可達 0（因為可選出 XOR=0 的非空組合）。
        若 start=0：常見情況下，若有依賴 => 0，否則最小非 0 為最小的基底向量（在標準形後更穩）。
        """
        if self.has_dep:
            return 0

        # 為了正確求最小，建議先 rebuild 成 row-echelon（可選）
        self.rebuild()
        res = start
        # greedy 從低位到高位也可，但最穩是把 p 當作獨立向量後嘗試降低
        for v in self.p:
            if (res ^ v) < res:
                res ^= v
        return res

    def rebuild(self) -> None:
        """
        把 b 轉成「標準形」（上三角/行最簡形），並建立 p 以支援 kth。
        kth 要求向量彼此最高位不同且已消去低位，這樣 k 的二進位才能直接對應組合。
        """
        if self._rebuilt:
            return

        # 先把高位基底對低位消掉，變成 reduced row echelon 的感覺
        for i in range(self.B - 1, -1, -1):
            if self.b[i] == 0:
                continue
            for j in range(i - 1, -1, -1):
                if self.b[j] and ((self.b[i] >> j) & 1):
                    self.b[i] ^= self.b[j]
                    self.m[i] ^= self.m[j]

        # 收集非 0 基底成 p（由低到高排列比較常用於 kth）
        self.p = []
        for i in range(self.B):
            if self.b[i]:
                self.p.append(self.b[i])

        self._rebuilt = True

    def kth(self, k: int) -> int:
        """
        求第 k 小 XOR（1-indexed 常見寫法）：
        - 若 has_dep=True，代表存在非空組合 XOR=0，因此「0 會出現」，序列包含 0
          常見約定：k=1 對應 0
        - 若 has_dep=False，則 0 只由空集合得到，仍通常讓 0 算第一個（看題目）

        這裡採用常見模板慣例：
        - 若 has_dep=True：第 1 小是 0（可以用非空集合做到）
        - 若 has_dep=False：第 1 小也是 0（空集合）

        若 k 超出可生成數量，回傳 -1。
        """
        self.rebuild()
        cnt = len(self.p)

        # 可生成的不同 XOR 值數量：2^cnt
        # 這裡把 0 也算進去（常見）
        if k <= 0 or k > (1 << cnt):
            return -1

        # 令 k-1 的二進位代表選哪些向量
        x = 0
        kk = k - 1
        for i in range(cnt):
            if (kk >> i) & 1:
                x ^= self.p[i]
        return x

    def merge(self, other: "XorBasis") -> None:
        """
        合併另一個線性基：把 other 的基底向量插入進來。
        注意：若你要保留 other 的回溯 idx，需自行協調 idx 空間。
        """
        # 直接插 other 的 b[i] 即可（用值代表 span）
        for i in range(other.B - 1, -1, -1):
            if other.b[i]:
                self.insert(other.b[i], idx=-1)
