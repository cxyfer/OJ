# @algorithm @lc id=3192 lang=python3 
# @title maximum-xor-product


from en.Python3.mod.preImport import *
# @test(12,5,4)=98
# @test(6,7,5)=930
# @test(1,6,3)=12
class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        # print(bin(a)[2:].zfill(n), bin(b)[2:].zfill(n))
        MOD = 10 ** 9 + 7
        ans = 0
        x = 0
        # 逐位枚舉
        for d in range(n):
            if (a >> d) & 1 and (b >> d) & 1: # a,b的這一位都是 1
                pass # x 的這一位是 0
            elif (a >> d) & 1 or (b >> d) & 1: # a的這一位是 1, b的這一位是 0, 或是反過來
                tmp = x + (1 << d)
                s1 = (a^tmp) * (b^tmp)
                s2 = (a^x) * (b^x)
                if s1 > s2:
                    x = tmp
            else: # a,b的這一位都是 0
                x += 1 << d # x 的這一位是 1
        ans = (a^x) * (b^x) % MOD
        return ans % MOD