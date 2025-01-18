/*
 * @lc app=leetcode id=3143 lang=cpp
 *
 * [3143] Maximum Points Inside the Square
 */

// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    int maxPointsInsideSquare(vector<vector<int>>& points, string s) {
        // return solve2(points, s);
        return solve3(points, s);
    }
    int solve2(vector<vector<int>>& points, string s) {
        map<int, vector<char>> pos;
        for (int i = 0; i < s.size(); i++) {
            int x = points[i][0], y = points[i][1];
            pos[max(abs(x), abs(y))].push_back(s[i]);
        }
        vector<bool> vis(26, false);
        int ans = 0;
        for (auto p : pos) {
            cout << p.first << " ";
            for (char ch : p.second) {
                cout << ch << " ";
            }
            cout << endl;
            bool flag = true;
            for (char ch : p.second) {
                if (vis[ch - 'a']) {
                    flag = false;
                    break;
                }
                vis[ch - 'a'] = true;
            }
            if (!flag) break;
            ans += p.second.size();
        }
        return ans;
    }
    int solve3(vector<vector<int>>& points, string s) {
        map<int, int> mask; // sort by distance
        for (int i = 0; i < s.size(); i++) {
            int x = points[i][0], y = points[i][1], c = s[i] - 'a';
            int d = max(abs(x), abs(y));
            if (mask[d] & (1 << c)) { // already exists
                mask[d] |= 1 << 26; // mark as invalid
            } else {
                mask[d] |= 1 << c; // add tag
            }
        }
        int u = 1 << 26; // union
        for (auto p : mask) {
            if (p.second & u) {
                break;
            }
            u |= p.second;
        }
        return __builtin_popcount(u) - 1;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    Solution sol;
    // [[2,2],[-1,-2],[-4,4],[-3,1],[3,-3]]
    // "abdca"
    vector<vector<int>> points = {{2,2},{-1,-2},{-4,4},{-3,1},{3,-3}};
    string s = "abdca";
    cout << sol.maxPointsInsideSquare(points, s) << endl; // 2
    points = {{1,1},{-2,-2},{-2,2}};
    s = "abb";
    cout << sol.maxPointsInsideSquare(points, s) << endl; // 1
    points = {{1,1},{-1,-1},{2,-2}};
    s = "ccd";
    cout << sol.maxPointsInsideSquare(points, s) << endl; // 0
    return 0;
}
