# @algorithm @lc id=983 lang=python3 
# @title validate-stack-sequences


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5],[4,5,3,2,1])=true
# @test([1,2,3,4,5],[4,3,5,1,2])=false
class Solution:
    """
        Stack
    """
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        st = []
        for x in pushed:
            st.append(x)
            while st and st[-1] == popped[i]:
                st.pop()
                i += 1
        return not st