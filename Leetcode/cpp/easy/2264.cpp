/*
 * @lc app=leetcode.cn id=2264 lang=cpp
 * @lcpr version=30204
 *
 * [2264] 字符串中最大的 3 位相同数字
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
// @lc code=start
class Solution {
public:
    string largestGoodInteger(string num) {
        int n = num.size();
        string ans = "";
        for (int i = 0; i < n;) {
            int j = i;
            while (j < n && num[j] == num[i])
                j++;
            if (j - i >= 3)
                ans = max(ans, num.substr(i, 3));
            i = j;
        }
        return ans;
    }
};
// @lc code=end



/*
// @lcpr case=start
// "6777133339"\n
// @lcpr case=end

// @lcpr case=start
// "2300019"\n
// @lcpr case=end

// @lcpr case=start
// "42352338"\n
// @lcpr case=end

 */

