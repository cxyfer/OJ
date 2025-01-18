# @algorithm @lc id=402 lang=python3 
# @title remove-k-digits


from en.Python3.mod.preImport import *
# @test("1432219",3)="1219"
# @test("10200",1)="200"
# @test("10",2)="0"
class Solution:
    """
        Greedy
        貪心思路是讓前面的數字盡量小，所以當遇到比前面的數字還小的數字時，就將前面的數字刪除
        將問題轉換成保留 n - k 個數字
    """
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        left = n - k
        st = []
        for d in num:
            while k and st and st[-1] > d:
                st.pop()
                k -= 1
            st.append(d)
        ans = ''.join(st[:left]).lstrip('0')
        return ans if ans else '0'