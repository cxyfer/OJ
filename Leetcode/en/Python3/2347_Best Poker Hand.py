# @algorithm @lc id=2433 lang=python3 
# @title best-poker-hand


from en.Python3.mod.preImport import *
# @test([13,2,3,1,9],["a","a","a","a","a"])="Flush"
# @test([4,4,2,4,4],["d","a","a","b","c"])="Three of a Kind"
# @test([10,10,2,12,9],["a","b","c","a","d"])="Pair"
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst == lst[::-1]