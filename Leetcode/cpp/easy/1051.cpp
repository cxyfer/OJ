/*
 * @lc app=leetcode.cn id=1051 lang=cpp
 *
 * [1051] 高度检查器
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int heightChecker(vector<int>& heights) {
        // return solve1(heights);
        return solve2(heights);
    }
    int solve1(vector<int>& heights) {
        int n = heights.size();
        vector<int> expected = heights;
        sort(expected.begin(), expected.end());
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (heights[i] != expected[i]) {
                ans++;
            }
        }
        return ans;
    }
    int solve2(vector<int>& heights) {
        int n = heights.size();
        vector<int> cnt(101, 0);
        for (int x : heights) cnt[x]++;
        int ans = 0, s = 0;
        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < cnt[i]; j++) {
                if (heights[s++] != i) ans++;
            }
        }
        return ans;
    }
};
// @lc code=end

