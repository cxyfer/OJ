# @algorithm @lc id=735 lang=python3 
# @title asteroid-collision


from en.Python3.mod.preImport import *
# @test([5,10,-5])=[5,10]
# @test([8,-8])=[]
# @test([10,2,-5])=[10]
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            if a > 0:
                st.append(a)
            else:
                if st and st[-1] == -a: # same size
                    st.pop()
                    continue
                while st and st[-1] > 0 and st[-1] < -a:
                    st.pop()
                if not st or st[-1] < 0:
                    st.append(a)
                elif st[-1] == -a:
                    st.pop()
        return st