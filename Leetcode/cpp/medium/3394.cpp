/*
 * @lc app=leetcode.cn id=3394 lang=cpp
 * @lcpr version=30204
 *
 * [3394] 判断网格图能否被切割成块
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution1 {
public:
    bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
        map<double, int> X, Y;
        for (auto& rect : rectangles) {
            X[rect[0] + 0.1] += 1;
            X[rect[2] - 0.1] -= 1;
            Y[rect[1] + 0.1] += 1;
            Y[rect[3] - 0.1] -= 1;
        }

        auto check = [&](map<double, int>& m) -> bool {
            int s = 0, cnt = 0;
            for (auto& [_, c] : m) {
                s += c;
                if (s == 0) cnt += 1;
            }
            return cnt >= 3;
        };

        return check(X) || check(Y);
    }
};

class Solution2 {
public:
    bool checkValidCuts(int n, vector<vector<int>>& rectangles) {
        vector<pair<int, int>> X, Y;
        for (auto& rect : rectangles) {
            X.emplace_back(rect[0], rect[2]);
            Y.emplace_back(rect[1], rect[3]);
        }

        auto check = [&](vector<pair<int, int>>& intervals) -> bool {
            sort(intervals.begin(), intervals.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
                return a.first < b.first;
            });
            int cnt = 0, ed = -1;
            for (auto& [x, y] : intervals) {
                if (ed <= x)
                    cnt++, ed = y;
                else
                    ed = max(ed, y);
            }
            return cnt >= 3;
        };
        
        return check(X) || check(Y);
    }
};

using Solution = Solution1;
// using Solution = Solution2;
// @lc code=end



/*
// @lcpr case=start
// 5\n[[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]\n
// @lcpr case=end

// @lcpr case=start
// 4\n[[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]\n
// @lcpr case=end

// @lcpr case=start
// 4\n[[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]\n
// @lcpr case=end

 */

