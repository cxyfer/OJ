/*
 * @lc app=leetcode.cn id=1945 lang=cpp
 *
 * [1945] 字符串转化后的各位数字之和
 */

// @lc code=start
class Solution {
public:
    int getLucky(string s, int k) {
        int ans = 0, tmp = 0;
        for (char ch : s) {
            tmp = ch - 'a' + 1;
            while (tmp > 0) {
                ans += tmp % 10;
                tmp /= 10;
            }
        }
        while (ans >= 10 && --k > 0) {
            tmp = ans;
            ans = 0;
            while (tmp > 0) {
                ans += tmp % 10;
                tmp /= 10;
            }
        }
        return ans;
    }
};
// @lc code=end

