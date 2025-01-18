/*
 * @lc app=leetcode.cn id=402 lang=cpp
 *
 * [402] 移掉 K 位数字
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    /*
        Greedy + Stack
        貪心思路是讓前面的數字盡量小，所以當遇到比前面的數字還小的數字時，就將前面的數字刪除
        將問題轉換成保留 n - k 個數字
    */
    string removeKdigits(string num, int k) {
        int n = num.size();
        int left = n - k; // 將問題轉換成保留 n - k 個數字
        stack<char> st;
        for (char d : num) {
            while (k && !st.empty() && st.top() > d) { // 還能刪且遇到更小的數字
                st.pop();
                k--;
            }
            st.push(d);
        }
        string ans = ""; // 組合答案
        while (st.size() > left) st.pop(); // 刪除多餘的數字
        while (!st.empty()) {
            ans += st.top();
            st.pop();
        }
        reverse(ans.begin(), ans.end());
        while (ans.size() > 1 && ans[0] == '0') ans.erase(ans.begin()); // 刪除前面的 0
        return ans.empty() ? "0" : ans;
    }
};
// @lc code=end

