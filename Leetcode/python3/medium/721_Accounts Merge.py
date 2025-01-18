#
# @lc app=leetcode id=721 lang=python3
# @lcpr version=30204
#
# [721] Accounts Merge
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class DSU: # Disjoint Set Union
    __slots__ = ['n', 'pa']

    def __init__(self, n: int):
        self.n = n
        self.pa = list(range(n)) # 父節點

    def find(self, x: int) -> int:
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.pa[py] = px
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mail_to_name = {}
        mail_to_idx = {} # 將 mail 字串映射到數字編號
        idx = 0
        for name, *mails in accounts:
            for mail in mails:
                if mail not in mail_to_idx:
                    mail_to_idx[mail] = idx
                    idx += 1
                mail_to_name[mail] = name

        dsu = DSU(idx)
        for name, *mails in accounts: # 將同一個人的 mail 連接起來
            idx0 = mail_to_idx[mails[0]]
            for mail in mails[1:]:
                dsu.union(idx0, mail_to_idx[mail])

        idx_to_mails = defaultdict(list) # 同一個人的所有 mail
        for mail, idx in mail_to_idx.items(): 
            idx = dsu.find(idx)
            idx_to_mails[idx].append(mail)
        
        ans = []
        for _, mails in idx_to_mails.items():
            name = mail_to_name[mails[0]]
            ans.append([name] + sorted(mails))
        return ans
# @lc code=end



#
# @lcpr case=start
# [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]\n
# @lcpr case=end

# @lcpr case=start
# [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]\n
# @lcpr case=end

#

