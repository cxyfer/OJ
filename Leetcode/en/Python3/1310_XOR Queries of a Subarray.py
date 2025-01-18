# @algorithm @lc id=1435 lang=python3 
# @title xor-queries-of-a-subarray


from en.Python3.mod.preImport import *
# @test([1,3,4,8],[[0,1],[1,2],[0,3],[3,3]])=[2,7,14,8]
# @test([4,8,2,10],[[2,3],[1,3],[0,0],[0,3]])=[8,0,4,4]
class Solution:
    """
        XOR Prefix Sum
    """
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        s = [0] * (n + 1) # s[i] = arr[0] ^ arr[1] ^ ... ^ arr[i-1]
        for i, x in enumerate(arr):
            s[i + 1] = s[i] ^ x
        return [s[r + 1] ^ s[l] for l, r in queries]