/*
 * @lc app=leetcode.cn id=3703 lang=cpp
 * @lcpr version=30204
 *
 * [3703] 移除K-平衡子字符串
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string removeSubstring(string s, int k) {
        vector<pair<char, int>> st;
        for (char ch : s) {
            if (st.size() && st.back().first == ch)
                st.back().second += 1;
            else
                st.push_back({ch, 1});
            if (st.size() > 1 && st.back().first == ')' && st.back().second == k && st.front().second >= k) {
                st.pop_back();
                st.back().second -= k;
                if (st.back().second == 0)
                    st.pop_back();
            }
        }
        string ans = "";
        for (auto [ch, v] : st)
            ans += string(v, ch);
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "(())"\n1\n
// @lcpr case=end

// @lcpr case=start
// "(()("\n1\n
// @lcpr case=end

// @lcpr case=start
// "((()))()()()"\n3\n
// @lcpr case=end

 */

