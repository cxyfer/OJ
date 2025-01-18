/*
 * @lc app=leetcode.cn id=740 lang=cpp
 *
 * [740] 删除并获得点数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const int N = 1e4 + 5;
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        int mx = *max_element(nums.begin(), nums.end());
        vector<int> cnt(mx+1);
        for (int x : nums) cnt[x]++;
        int f0=0, f1=0, f2;
        for (int x = 1; x <= mx; x++) {
            f2 = max(f1, f0 + x * cnt[x]);
            f0 = f1;
            f1 = f2;
        }
        return f1;
    }
};
// @lc code=end

