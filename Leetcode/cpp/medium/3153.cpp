/*
 * @lc app=leetcode.cn id=3153 lang=cpp
 *
 * [3153] Sum of Digit Differences of All Pairs
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
using LL = long long;
class Solution {
public:
    LL sumDigitDifferences(vector<int>& nums) {
        // return solve1(nums);
        return solve2(nums);
    }
    LL solve1(vector<int>& nums) {
        unordered_map<int, unordered_map<int, int>> cnt;
        for (int x : nums) {
            int d = 0;
            while (x) {
                cnt[d][x % 10]++;
                x /= 10;
                d++;
            }
        }
        LL ans = 0;
        for (auto p : cnt) {
            LL tol = 0;
            for (auto kv : p.second) tol += kv.second;
            for (auto kv : p.second) {
                ans += (LL)(tol - kv.second) * kv.second;
            }
        }
        return ans / 2; // 每對數字會被計算兩次
    }
    LL solve2(vector<int>& nums) {
        LL ans = 0;
        int cnt[9][10] = {0}; // 每個位數中，每個數字出現的次數。由於 nums[i] < 10^9，即最多9位數
        for (int i = 0; i < nums.size(); i++) {
            int x = nums[i], j = 0; 
            while (x) {
                int d = x % 10;
                x /= 10;
                ans += i - cnt[j][d]; // 在第i個數字的第j位，前面有 i - cnt[j][d] 個不同的數字，即為對答案的貢獻
                cnt[j][d]++;
                j++;
            }
        }
        return ans;
    }
};
// @lc code=end

