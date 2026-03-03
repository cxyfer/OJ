/*
 * @lc app=leetcode id=1929 lang=rust
 *
 * [1929] Concatenation of Array
 */


// @lcpr-template-start
struct Solution;
// @lcpr-template-end
// @lc code=start
impl Solution {
    // 注意傳入的 nums 要 mutable 才能直接 extend
    pub fn get_concatenation(mut nums: Vec<i32>) -> Vec<i32> {
        nums.extend(nums.clone());
        nums
    }
}
// @lc code=end