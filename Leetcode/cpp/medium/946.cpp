/*
 * @lc app=leetcode id=946 lang=cpp
 * @lcpr version=30122
 *
 * [946] Validate Stack Sequences
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        Stack
    */
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int i = 0;
        stack<int> st;
        for (int x: pushed) {
            st.push(x);
            while (!st.empty() && st.top() == popped[i]) {
                st.pop();
                i++;
            }
        }
        return st.empty();
    }
};
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4,5]\n[4,5,3,2,1]\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3,4,5]\n[4,3,5,1,2]\n
// @lcpr case=end

 */

