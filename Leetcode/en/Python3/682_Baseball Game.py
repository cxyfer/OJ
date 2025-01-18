# @algorithm @lc id=682 lang=python3 
# @title baseball-game


from en.Python3.mod.preImport import *
# @test(["5","2","C","D","+"])=30
# @test(["5","-2","4","C","D","9","+","+"])=27
# @test(["1","C"])=0
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for op in operations:
            if op == "D":
                st.append(st[-1] * 2)
            elif op == "+":
                st.append(st[-1] + st[-2])
            elif op == "C":
                st.pop()
            else:
                st.append(int(op))
        return sum(st)

        