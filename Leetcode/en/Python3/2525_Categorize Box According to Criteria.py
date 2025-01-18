# @algorithm @lc id=2619 lang=python3 
# @title categorize-box-according-to-criteria


from en.Python3.mod.preImport import *
# @test(1000,35,700,300)="Heavy"
# @test(200,50,800,50)="Neither"
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        isBulky = any(dimension >= 10**4 for dimension in [length, width, height]) or length * width * height >= 10**9
        isHeavy = mass >= 100
        if isBulky and isHeavy:
            return "Both"
        elif isBulky:
            return "Bulky"
        elif isHeavy:
            return "Heavy"
        else:
            return "Neither"