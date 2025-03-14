/*
 * @lc app=leetcode id=3340 lang=cpp
 *
 * [3340] Check Balanced String
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    bool isBalanced(string num) {
        int n = num.size();
        vector<int> cnt(2);
        for (int i = 0; i < n; i++)
            cnt[i & 1] += num[i] - '0';
        return cnt[0] == cnt[1];
    }
};

class Solution2 {
public:
    bool isBalanced(string num) {
        int tot = 0;
        for (int i = 0; i < num.size(); i++)
            tot += (i & 1) ? num[i] - '0' : -(num[i] - '0');
        return tot == 0;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end

