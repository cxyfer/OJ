/*
 * @lc app=leetcode.cn id=3628 lang=cpp
 * @lcpr version=30204
 *
 * [3628] 插入一个字母的最大子序列数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using ll = long long;

class Solution1 {
public:
    long long numOfSubsequences(string s) {
        ll lt = 0, l = 0, t = ranges::count(s, 'T');
        for (char ch : s) {
            if (ch == 'L') l++;
            else if (ch == 'T') t--;
            lt = max(lt, l * t);
        }
        return numDistinct(s, "LCT") + max({lt, numDistinct(s, "LC"), numDistinct(s, "CT")});
    }

    // 115. Distinct Subsequences
    long long numDistinct(string s, string t) {
        int n = s.size(), m = t.size();
        vector<ll> f(m + 1, 0);
        f[0] = 1;
        for (int i = 1; i <= n; ++i)
            for (int j = m; j >= 1; --j)
                if (s[i - 1] == t[j - 1])
                    f[j] += f[j - 1];
        return f[m];
    }
};

class Solution2 {
public:
    long long numOfSubsequences(string s) {
        ll l = 0, lc = 0, lct = 0, c = 0, ct = 0, lt = 0, t = ranges::count(s, 'T');
        for (char ch : s) {
            if (ch == 'L') l++;
            else if (ch == 'C') c++, lc += l;
            else if (ch == 'T') ct += c, lct += lc, t--;
            lt = max(lt, l * t);
        }
        return lct + max({lt, lc, ct});
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// "LMCT"\n
// @lcpr case=end

// @lcpr case=start
// "LCCT"\n
// @lcpr case=end

// @lcpr case=start
// "L"\n
// @lcpr case=end

 */

