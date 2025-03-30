/*
 * @lc app=leetcode.cn id=680 lang=cpp
 * @lcpr version=30204
 *
 * [680] 验证回文串 II
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    bool validPalindrome(string s) {
        auto helper = [&](this auto &&helper, int i, int j, bool used) -> bool {
            while (i < j) {
                if (s[i] != s[j]) {
                    if (used) return false;
                    return helper(i + 1, j, true) || helper(i, j - 1, true);
                }
                i++;
                j--;
            }
            return true;
        };
        return helper(0, s.size() - 1, false);
    }
};

class Solution2 {
public:
    bool validPalindrome(string s) {
        auto dfs = [&](this auto &&dfs, int i, int j, bool used) -> bool {
            if (i >= j) return true;
            if (s[i] != s[j]) {
                if (used) return false;
                return dfs(i + 1, j, true) || dfs(i, j - 1, true);
            }
            return dfs(i + 1, j - 1, used);
        };
        return dfs(0, s.size() - 1, false);
    }
};

using Solution = Solution1;
// using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// "aba"\n
// @lcpr case=end

// @lcpr case=start
// "abca"\n
// @lcpr case=end

// @lcpr case=start
// "abc"\n
// @lcpr case=end

 */

