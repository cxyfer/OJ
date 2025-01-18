/*
 * @lc app=leetcode.cn id=1405 lang=cpp
 *
 * [1405] 最长快乐字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        priority_queue<pair<int, char>> hp; // Max Heap
        hp.push({a, 'a'});
        hp.push({b, 'b'});
        hp.push({c, 'c'});
        string ans = "";
        while (hp.top().first > 0) {
            auto [x, ch_x] = hp.top();
            hp.pop();
            if (ans.size() >= 2 && ans.back() == ch_x && ans[ans.size() - 2] == ch_x) {
                auto [y, ch_y] = hp.top();
                hp.pop();
                if (y <= 0) break;
                ans += ch_y;
                hp.push({y - 1, ch_y});
                hp.push({x, ch_x});
            } else {
                ans += ch_x;
                hp.push({x - 1, ch_x});
            }
        }
        return ans;
    }
};
// @lc code=end

int main() {
    Solution sol = Solution();
    cout << sol.longestDiverseString(1, 1, 7) << endl;
    return 0;
}