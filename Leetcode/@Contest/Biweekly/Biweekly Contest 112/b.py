from collections import Counter
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        list1 = list(s1)[:]
        list2 = list(s2)[:]
        
        if len(s1) != len(s2):
            return False
        n = len(s1)
        # 奇數偶數位置的字母不同，則無法通過操作讓兩個字串相等
        cnto1 = Counter(list1[::2])
        cnto2 = Counter(list2[::2])
        cnte1 = Counter(list1[1::2])
        cnte2 = Counter(list2[1::2])
        return cnto1 == cnto2 and cnte1 == cnte2
    
sol = Solution()
print(sol.checkStrings("abcdba", "cabdab"))
print(sol.checkStrings("abe", "bea"))