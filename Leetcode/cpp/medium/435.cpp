/*
 * @lc app=leetcode.cn id=435 lang=cpp
 * @lcpr version=30204
 *
 * [435] 无重叠区间
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
#include <ranges>

class Solution1 {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int n = intervals.size();
        ranges::sort(intervals, [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });
        vector<int> f(n, 1);
        for (int i = 0; i < n; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (intervals[j][1] <= intervals[i][0]) {
                    f[i] = max(f[i], f[j] + 1);
                    break;
                }
            }
        }
        return n - ranges::max(f);
    }
};

class Solution2 {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int n = intervals.size();
        ranges::sort(intervals, [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        int ans = n;
        int r = -1e9;
        for (auto& interval : intervals) {
            int st = interval[0], ed = interval[1];
            if (st >= r) {
                ans--;
                r = ed;
            }
        }
        return ans;
    }
};

// using Solution = Solution1;
using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// [[1,2],[2,3],[3,4],[1,3]]\n
// @lcpr case=end

// @lcpr case=start
// [ [1,2], [1,2], [1,2] ]\n
// @lcpr case=end

// @lcpr case=start
// [ [1,2], [2,3] ]\n
// @lcpr case=end

 */

