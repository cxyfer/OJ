# @algorithm @lc id=1401 lang=python3 
# @title number-of-burgers-with-no-waste-of-ingredients


from en.Python3.mod.preImport import *
# @test(16,7)=[1,6]
# @test(17,4)=[]
# @test(4,17)=[]
class Solution:
    """
        Math 
        4x + 2y = tomatoSlices 
        x + y = cheeseSlices 

        x = (tomatoSlices - 2 * cheeseSlices) / 2
        y = (4 * cheeseSlices - tomatoSlices) / 2
    """
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x = (tomatoSlices - 2 * cheeseSlices) / 2
        y = (4 * cheeseSlices - tomatoSlices) / 2
        if x < 0 or y < 0 or x != int(x) or y != int(y):
            return []
        return [int(x), int(y)]