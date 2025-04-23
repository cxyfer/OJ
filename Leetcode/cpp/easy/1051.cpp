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
class Solution1 {
public:
    int heightChecker(vector<int>& heights) {
        int n = heights.size();
        vector<int> expected = heights;
        sort(expected.begin(), expected.end());
        int ans = 0;
        for (int i = 0; i < n; i++)
            ans += heights[i] != expected[i];
        return ans;
    }
};

class Solution2 {
public:
    int heightChecker(vector<int>& heights) {
        int n = heights.size();
        vector<int> cnt(101, 0);
        for (int x : heights) cnt[x]++;
        int ans = 0, s = 0;
        for (int x = 0; x < 101; x++)
            while (cnt[x]--)
                ans += heights[s++] != x;
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end

