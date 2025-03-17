/*
 * @lc app=leetcode.cn id=1963 lang=cpp
 *
 * [1963] 使字符串平衡的最小交换次数
 */


// @lcpr-template-start
#include <bits/stdc++.h>
using namespace std;
// @lcpr-template-end
/*
    https://gdst.dev/posts/LC-1963/
*/
// @lc code=start
class Solution {
public:
    int minSwaps(string s) {
        int cnt = 0;  // 未配對的 '[' 數量
        for (char ch : s) {
            if (ch == '[')  cnt++;
            else if (cnt) cnt--;
        }
        return (cnt + 1) / 2;
    }
};
// @lc code=end

