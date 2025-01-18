/*
 * @lc app=leetcode.cn id=2751 lang=cpp
 *
 * [2751] 机器人碰撞
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        int n = positions.size();
        vector<int> id(n);
        iota(id.begin(), id.end(), 0);
        sort(id.begin(), id.end(), [&](int i, int j) {
            return positions[i] < positions[j]; // sort by position
        });

        stack<int> st;
        vector<int> left;
        for (int i: id) {
            if (directions[i] == 'R') {
                st.push(i);
            }
            else {
                while (!st.empty() && healths[st.top()] < healths[i]) {
                    healths[i]--;
                    st.pop();
                }
                if (!st.empty()) {
                    if (healths[st.top()] == healths[i]) st.pop();
                    else healths[st.top()]--;
                }
                else {
                    left.push_back(i);
                }
            }
        }

        while (!st.empty()) {
            left.push_back(st.top());
            st.pop();
        }
        sort(left.begin(), left.end());
        vector<int> ans;
        for (int i: left) ans.push_back(healths[i]);
        return ans;
    }
};
// @lc code=end