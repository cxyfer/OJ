/*
 * @lc app=leetcode.cn id=1052 lang=cpp
 *
 * [1052] 爱生气的书店老板
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        int n = customers.size(), tot = 0, ans = 0;
        vector<int> s(n + 1);  // prefix sum
        for (int i = 0; i < n; i++) {
            s[i + 1] = s[i] + customers[i] * grumpy[i];
            tot += customers[i] * (1 ^ grumpy[i]);
        }
        for (int i = 0; i <= (n - minutes); i++)
            ans = max(ans, s[i + minutes] - s[i]);
        return tot + ans;
    }
};

class Solution2 {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        int n = customers.size(), tot = 0, cur = 0;
        for (int i = 0; i < n; i++) tot += customers[i] * (1 ^ grumpy[i]);
        for (int i = 0; i < minutes; i++) cur += customers[i] * grumpy[i];
        int ans = cur;
        for (int i = minutes; i < n; i++) {
            cur += customers[i] * grumpy[i] -
                   customers[i - minutes] * grumpy[i - minutes];
            ans = max(ans, cur);
        }
        return tot + ans;
    }
};

// class Solution : public Solution1 {};
class Solution : public Solution2 {};
// @lc code=end