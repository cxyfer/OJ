#
# @lc app=leetcode id=726 lang=python3
# @lcpr version=30204
#
# [726] Number of Atoms
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        i = 0
        st = [Counter()]
        while i < n:
            if formula[i] == '(':
                st.append(Counter())
                i += 1
            elif formula[i] == ')':
                i += 1
                j = i
                while j < n and formula[j].isdigit():
                    j += 1
                mul = int(formula[i:j] or 1)
                i = j
                cnt = st.pop()
                for k in cnt:
                    st[-1][k] += cnt[k] * mul
            else:
                j = i + 1
                while j < n and formula[j].islower():
                    j += 1
                elem = formula[i:j]
                i = j
                while j < n and formula[j].isdigit():
                    j += 1
                mul = int(formula[i:j] or 1)
                i = j
                st[-1][elem] += mul
        cnt = st[0]
        return ''.join(k + (str(v) if v > 1 else '') for k, v in sorted(cnt.items()))
# @lc code=end



#
# @lcpr case=start
# "H2O"\n
# @lcpr case=end

# @lcpr case=start
# "Mg(OH)2"\n
# @lcpr case=end

# @lcpr case=start
# "K4(ON(SO3)2)2"\n
# @lcpr case=end

#

