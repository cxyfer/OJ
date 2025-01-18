/*
 * @lc app=leetcode.cn id=1894 lang=cpp
 *
 * [1894] 找到需要补充粉笔的学生编号
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        int n = chalk.size();
        long long s = accumulate(chalk.begin(), chalk.end(), 0ll);
        k %= s;
        for (int i = 0; i < n; ++i) {
            if (k < chalk[i]) return i;
            k -= chalk[i];
        }
        return 0;
    }
};

class Solution2 {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        int n = chalk.size();
        vector<long long> s(n + 1);
        for (int i = 0; i < n; ++i) s[i + 1] = s[i] + chalk[i];
        return upper_bound(s.begin(), s.end(), k % s[n]) - s.begin() - 1;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};

// @lc code=end

