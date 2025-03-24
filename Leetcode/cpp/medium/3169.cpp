/*
 * @lc app=leetcode.cn id=3169 lang=cpp
 *
 * [3169] 无需开会的工作日
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
 * 1. Merge Intervals
 *    - Similar to 56. Merge Intervals
 * 2. Prefix Sum + Line Sweep
 */
// @lc code=start
class Solution1a {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());

        vector<pair<int, int>> merged;
        for (auto& m : meetings) {
            int x = m[0], y = m[1];
            if (merged.empty() || merged.back().second < x)
                merged.emplace_back(x, y);
            else
                merged.back().second = max(merged.back().second, y);
        }

        int ans = days;
        for (auto& [x, y] : merged)  // [x, y] is invalid
            ans -= y - x + 1;
        return ans;
    }
};

class Solution1b {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());
        int ans = days, st = 0, ed = -1;
        for (auto& m : meetings) {
            int x = m[0], y = m[1];
            if (x > ed) {
                ans -= (ed - st + 1);  // [st, ed] is invalid
                st = x;
                ed = y;
            } else
                ed = max(ed, y);
        }
        ans -= (ed - st + 1);  // [st, ed] is invalid
        return ans;
    }
};

class Solution1c {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());
        int ans = 0, ed = 0;
        for (auto& m : meetings) {
            int x = m[0], y = m[1];
            if (x > ed) {
                ans += x - ed - 1;  // [ed + 1, x - 1] is valid
                ed = y;
            } else
                ed = max(ed, y);
        }
        ans += days - ed;  // [ed + 1, days] is valid
        return ans;
    }
};

class Solution2 {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        map<int, int> mp;
        for (auto& m : meetings) {
            mp[m[0]] += 1;
            mp[m[1] + 1] -= 1;
        }
        int ans = 0, s = 0, pre = 1;
        for (auto& [d, v] : mp) {
            if (s == 0) ans += d - pre;  // [pre, d - 1] is valid
            s += v;
            pre = d;
        }
        ans += days - pre + 1;  // [pre, days] is valid
        return ans;
    }
};

// using Solution = Solution1a;
using Solution = Solution1b;
// using Solution = Solution1c;
// using Solution = Solution2;
// @lc code=end