# @algorithm @lc id=2556 lang=python3 
# @title convert-the-temperature


from en.Python3.mod.preImport import *
# @test(36.50)=[309.65000,97.70000]
# @test(122.11)=[395.26000,251.79800]
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+273.15, celsius*1.8 + 32]