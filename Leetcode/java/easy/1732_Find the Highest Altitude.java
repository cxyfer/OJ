/*
 * @lc app=leetcode id=1732 lang=java
 *
 * [1732] Find the Highest Altitude
 */


// @lcpr-template-start
// @lc code=start
class Solution {
    public int largestAltitude(int[] gain) {
        int s = 0, ans = 0;
        for (int x : gain) {
            s += x;
            ans = Math.max(ans, s);
        }
        return ans;
    }
}
// @lc code=end

