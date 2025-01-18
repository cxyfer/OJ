/*
 * @lc app=leetcode id=682 lang=cpp
 * @lcpr version=30122
 *
 * [682] Baseball Game
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
class Solution {
public:
    int calPoints(vector<string>& operations) {
        int a, b;
        stack<int> st;
        for (string op : operations) {
            if (op == "+") {
                a = st.top(); st.pop();
                b = st.top(); st.push(a); // push back a
                st.push(a + b);
            } else if (op == "D") {
                st.push(st.top() * 2);
            } else if (op == "C") {
                st.pop();
            } else {
                st.push(stoi(op));
            }
        }
        int ans = 0;
        while (!st.empty()) {
            ans += st.top(); st.pop();
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// ["5","2","C","D","+"]\n
// @lcpr case=end

// @lcpr case=start
// ["5","-2","4","C","D","9","+","+"]\n
// @lcpr case=end

// @lcpr case=start
// ["1","C"]\n
// @lcpr case=end

 */

