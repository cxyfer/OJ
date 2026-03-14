/*
 * @lc app=leetcode id=1009 lang=rust
 *
 * [1009] Complement of Base 10 Integer
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn bitwise_complement(n: i32) -> i32 {
        n ^ ((1 << (32 - n.max(1).leading_zeros())) - 1)
    }
}
// @lc code=end

