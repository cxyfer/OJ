# @algorithm @lc id=1752 lang=python3 
# @title arithmetic-subarrays


from en.Python3.mod.preImport import *
# @test([4,6,5,9,3,7],[0,0,2],[2,3,5])=[true,false,true]
# @test([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10],[0,1,6,4,8,7],[4,4,9,7,9,10])=[false,true,false,false,true,true]
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for left, right in zip(l, r):
            mx = max(nums[left:right+1])
            mn = min(nums[left:right+1])
            if mx == mn: # 全部相等
                ans.append(True)
                continue
            if (mx-mn) % (right-left) != 0: # 公差不為整數
                ans.append(False)
                continue
            d = (mx-mn) // (right-left) # 公差
            flag = True
            for i, num in enumerate(sorted(nums[left:right+1])):
                if num != mn + d * i:
                    flag = False
                    break
            ans.append(flag)
        return ans