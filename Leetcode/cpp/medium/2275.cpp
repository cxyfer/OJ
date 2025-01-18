/*
 * @lc app=leetcode.cn id=2275 lang=cpp
 *
 * [2275] 按位与结果大于零的最长组合
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    int largestCombination(vector<int>& candidates) {
        int ans = 0, cur = 0;
        for (int b = 0; b < 24; b++) {
            cur = 0;
            for (int x : candidates) {
                if ((x >> b) & 1) cur++;
            }
            ans = max(ans, cur);
        }
        return ans;
    }
};

class Solution2 {
public:
    int largestCombination(vector<int>& candidates) {
        vector<int> cnt(24);
        for (int x : candidates) {
            while (x) {
                int lb = x & -x;
                x -= lb;
                cnt[__builtin_ctz(lb)]++;
            }
        }
        return *max_element(cnt.begin(), cnt.end());
    }
};

class Solution : public Solution2 {};
// @lc code=end

