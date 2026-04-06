/*
 * @lc app=leetcode.cn id=874 lang=cpp
 * @lcpr version=30204
 *
 * [874] 模拟行走机器人
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
const vector<pair<int, int>> DIRS = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        int x = 0, y = 0, d = 0;
        int ans = 0;
        
        set<pair<int, int>> obstacle_set;
        for (const auto& obstacle : obstacles) {
            obstacle_set.insert({obstacle[0], obstacle[1]});
        }
        for (const auto& command : commands) {
            if (command < 0) {
                d = (d + (command == -1 ? 1 : 3)) % 4;
            } else {
                for (int i = 0; i < command; i++) {
                    int nx = x + DIRS[d].first, ny = y + DIRS[d].second;
                    if (obstacle_set.count({nx, ny})) {
                        break;
                    }
                    x = nx, y = ny;
                    ans = max(ans, x * x + y * y);
                }
            }
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// [4,-1,3]\n[]\n
// @lcpr case=end

// @lcpr case=start
// [4,-1,4,-2,4]\n[[2,4]]\n
// @lcpr case=end

// @lcpr case=start
// [6,-1,-1,6]\n[]\n
// @lcpr case=end

 */

