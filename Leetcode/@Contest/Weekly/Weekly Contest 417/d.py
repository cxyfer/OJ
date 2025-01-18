import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)
        ln = [1] 
        for op in operations:
            ln.append(ln[-1] * 2)
        
        def helper(k, i):
            if i == -1:
                return 'a'
            op = operations[i]
            prev_length = ln[i]
            if k <= prev_length:
                return helper(k, i-1)
            else:
                offset = k - prev_length
                if op == 0:
                    return helper(offset, i-1)
                else:
                    ch = helper(offset, i-1)
                    return 'a' if ch == 'z' else chr(ord(ch) + 1)

        return helper(k, n - 1)
    
# 測試範例
if __name__ == "__main__":
    sol = Solution()
    
    # 範例 1
    print(sol.kthCharacter(5, [0,0,0]))  # 預期輸出: "a"
    
    # 範例 2
    print(sol.kthCharacter(10, [0,1,0,1]))  # 預期輸出: "b"
    
    # 新增測試案例
    print(sol.kthCharacter(7, [1,0,1]))  # 根據操作，預期輸出: "b"
