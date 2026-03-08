/*
 * @lc app=leetcode id=1980 lang=rust
 *
 * [1980] Find Unique Binary String
 */

// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    pub fn find_different_binary_string(nums: Vec<String>) -> String {
        nums.iter()
            .enumerate()
            .map(|(i, num)| if num.as_bytes()[i] == b'0' { '1' } else { '0' })
            .collect()
    }
}
// @lc code=end
