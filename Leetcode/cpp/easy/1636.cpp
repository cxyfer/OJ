/*
 * @lc app=leetcode.cn id=1636 lang=cpp
 *
 * [1636] 按照频率将数组升序排序
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        sort(nums.begin(), nums.end(), [&](int a, int b) {
            if (cnt[a] == cnt[b]) return a > b;
            return cnt[a] < cnt[b];
        });
        return nums;
    }
};
// @lc code=end

