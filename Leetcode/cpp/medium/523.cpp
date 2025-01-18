/*
 * @lc app=leetcode.cn id=523 lang=cpp
 *
 * [523] 连续的子数组和
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        return solve1(nums, k);
        // return solve2(nums, k);
    }
    bool solve1(vector<int>& nums, int k) {
        int n = nums.size();
        int s = 0;
        unordered_map<int, int> pos;
        pos[0] = -1;
        for (int i = 0; i < n; i++) {
            s = (s + nums[i]) % k;
            if (pos.count(s)) {
                if (i - pos[s] > 1) {
                    return true;
                }
            } else {
                pos[s] = i;
            }
        }
        return false;
    }
    bool solve2(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> s(n + 1, 0); // prefix sum
        for (int i = 1; i <= n; i++) s[i] = (s[i - 1] + nums[i - 1]) % k;
        unordered_set<int> pos;
        for (int i = 2; i <= n; i++) {
            pos.insert(s[i - 2]);
            if (pos.count(s[i])) return true;
        }
        return false;
    }
};
// @lc code=end