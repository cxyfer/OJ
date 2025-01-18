/*
 * @lc app=leetcode.cn id=3158 lang=cpp
 *
 * [3158] 求出出现两次数字的 XOR 值
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int duplicateNumbersXOR(vector<int>& nums) {
        // return solve1(nums);
        return solve2(nums);
    }
    int solve1(vector<int>& nums) {
        int ans = 0;
        unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        for (auto it = cnt.begin(); it != cnt.end(); it++) {
            if (it->second == 2) ans ^= it->first;
        }
        return ans;
    }
    int solve2(vector<int>& nums) {
        int ans = 0;
        long long st = 0;
        for (int x : nums) {
            if (st & (1LL << x)) ans ^= x;
            else st |= (1LL << x);
        }
        return ans;
    }
};
// @lc code=end

