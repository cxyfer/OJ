# @algorithm @lc id=605 lang=python3 
# @title can-place-flowers


from en.Python3.mod.preImport import *
# @test([1,0,0,0,1],1)=true
# @test([1,0,0,0,1],2)=false
class Solution:
    """
        計算每段連續0的長度cur， (cur-1)//2 即為可種花的數量
        注意一下開始和結束的邊界條件，開頭和結尾 計算 cur//2 或 ((cur+1)-1)//2
        0,0,1,... 這種開頭的情況
        ...,1,0,0 這種結尾的情況
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cur = 1
        for flower in flowerbed:
            if flower == 1:
                if cur != 0:
                    n -= (cur - 1) // 2
                    cur = 0
            else:
                cur += 1
        if flowerbed[-1] == 0: # 少了最後一段沒減
            n -= cur // 2 # (cur + 1 - 1) // 2
        return n <= 0