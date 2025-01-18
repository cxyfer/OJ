# @algorithm @lc id=3057 lang=python3 
# @title count-k-subsequences-of-a-string-with-maximum-beauty


from en.Python3.mod.preImport import *
# @test("bcca",2)=4
# @test("abbcd",4)=2
class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        """
            Conbinations Math
            Multiplication Principle
        """
        # 用
        MOD = 10 ** 9 + 7
        # 用Counter統計每個字母出現的次數，再用一個Counter統計每個字母出現的次數的次數
        cnt = Counter(Counter(s).values())
        ans = 1
        nums = sorted(cnt.items(), reverse=True)
        for feq, num in nums:
            if num >= k: # 可以選的字母樹大於等於k，>k的話沒辦法全選，所以只能選k個
                # 出現次數為feq的字母有num個，選k個不一樣的字母，有comb(num, k)種選法
                return ans * pow(feq, k, MOD) * comb(num, k) % MOD
            # 每個字母有feq種選法，且出現次數為feq的字母有num個，有pow(feq, num)種選法
            ans *= pow(feq, num, MOD)
            k -= num
        return 0  # k 太大，沒辦法選滿k個不一樣的字母


