# @algorithm @lc id=3208 lang=python3 
# @title count-beautiful-substrings-ii


from en.Python3.mod.preImport import *
# @test("baeyh",2)=2
# @test("abba",1)=3
# @test("bcdf",1)=0
class Solution:
    """
        k 是/不是 完全平方數的倍數
    """
    def beautifulSubstrings(self, s: str, k: int) -> int:
        
        n = len(s)
        k = 4 * k
        for p in range(int(k**0.5), 1, -1): # k <= 1000
            if k % (p ** 2) == 0:
                k //= p
                break
        # print(k)
            
        ans = 0
        vowels_set = set("aeiou")
        pre_sum = [0]
        for ch in s:
            x = 1 if ch in vowels_set else -1
            pre_sum.append(pre_sum[-1] + x)


        ans = 0
        cnt = Counter([(k - 1, 0)])
        for i in range(n): # 枚舉起點
            p = (i % k, pre_sum[i+1])
            ans += cnt[p]
            cnt[p] += 1
        return ans