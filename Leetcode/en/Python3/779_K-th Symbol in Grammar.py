# @algorithm @lc id=795 lang=python3 
# @title k-th-symbol-in-grammar


from en.Python3.mod.preImport import *
# @test(1,1)=0
# @test(2,1)=0
# @test(2,2)=1
class Solution:
    """
        recursion
        - 若是parent的left child, 则和parent相同，否则相反
        - 透過k是奇數還是偶數來判斷是parent的left child還是right child
    """
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0 # base case
        res = self.kthGrammar(n-1, (k+1)//2) # parent
        return res ^ 1 if k % 2 == 0 else res # left child or right child