# @algorithm @lc id=331 lang=python3 
# @title verify-preorder-serialization-of-a-binary-tree


from en.Python3.mod.preImport import *
# @test("9,3,4,#,#,1,#,#,2,#,6,#,#")=true
# @test("1,#")=false
# @test("9,#,#,1")=false
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        cnt = 1 # number of available slots
        for ch in preorder.split(','):
            if cnt == 0:
                return False
            if ch == '#': # null node, consume a slot
                cnt -= 1
            else: # non-null node, consume a slot and create two more slots
                cnt += 1
        return cnt == 0