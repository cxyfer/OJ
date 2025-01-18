# @algorithm @lc id=3026 lang=python3 
# @title find-the-minimum-possible-sum-of-a-beautiful-array


from en.Python3.mod.preImport import *
# @test(2,3)=4
# @test(3,3)=8
# @test(1,1)=1
class Solution:
    """
        貪婪(Greedy) + 數學(Math)
        這題在周賽時原本可以用模擬的方式，但是在調整數據範圍後會TLE，故必需從數學的角度來解決

        題目要求構建一個正整數陣列、陣列中的數字兩兩不相等，且任兩個相加不等於 target。
        由於要使得陣列中的和最小，因此基於貪婪的思想，我們應該優先將最小的數字放入陣列中。
        但若故若使用 1 則不能使用 target - 1，因此對於小於 target 的數字 i ，只能添加到 i = floor(target / 2)，
        [floor(target / 2) + 1, target - 1] 這個範圍的數字都不能使用

        為方便表示，令 m = floor(target / 2)，
        故若 n <= m，則答案為 1 + 2 + ... + n
        反之，若 n > m，則答案為 (1 + 2 + ... + m) + (target + (target + 1) + ... + (target + n - m - 1))
    """
    def minimumPossibleSum(self, n: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        m = target // 2
        if n <= m:
            ans = n * (n + 1) // 2
        else:
            ans = m * (m + 1) // 2 + (target + target + n - m - 1) * (n - m) // 2
        return ans % MOD