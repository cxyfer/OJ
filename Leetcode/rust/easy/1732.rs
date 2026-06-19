/*
 * @lc app=leetcode id=1732 lang=rust
 *
 * [1732] Find the Highest Altitude
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        let (mut ans, mut s): (i32, i32) = (0, 0);
        for x in gain {
            s += x;
            ans = ans.max(s);
        }
        ans
    }
}
// @lc code=end

