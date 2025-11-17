/*
 * @lc app=leetcode.cn id=1513 lang=cpp
 * @lcpr version=30204
 *
 * [1513] 仅含 1 的子串数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int MOD = 1e9 + 7;

class Solution1 {
public:
    int numSub(string s) {
        int ans = 0;
        for (int i = 0, n = s.size(); i < n; ) {
            int st = i++;
            while (i < n && s[i] == s[st])
                i++;
            if (s[st] == '1')
                ans = (ans + (i - st) * (i - st + 1LL) / 2) % MOD;
        }
        return ans;
    }
};

class Solution2 {
public:
    int numSub(string s) {
        int ans = 0;
        int last0 = -1;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '0')
                last0 = i;
            else
                ans = (ans + i - last0) % MOD;
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// "0110111"\n
// @lcpr case=end

// @lcpr case=start
// "101"\n
// @lcpr case=end

// @lcpr case=start
// "111111"\n
// @lcpr case=end

// @lcpr case=start
// "000"\n
// @lcpr case=end

 */

