/*
 * @lc app=leetcode id=2506 lang=cpp
 *
 * [2506] Count Pairs Of Similar Strings
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int similarPairs(vector<string>& words) {
        int ans = 0;
        unordered_map<int, int> cnt;
        for (auto& word : words) {
            int s = 0;
            for (auto& ch : word)
                s |= 1 << (ch - 'a');
            ans += cnt[s]++;
        }
        return ans;
    }
};
// @lc code=end

